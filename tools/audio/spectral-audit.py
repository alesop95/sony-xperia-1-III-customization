#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
spectral-audit.py - Analisi spettrale quantitativa per verificare l'autenticita' di un file audio.

Complementare a track-benchmark.py: mentre quello ragiona su metadati e dimensione (bitrate atteso),
questo apre i campioni reali e misura il contenuto in frequenza, che e' la prova definitiva. Smaschera
due falsificazioni tipiche:

  1. Upsample / hi-res fasullo: un file dichiarato a 96 o 192 kHz il cui contenuto spettrale si ferma
     ben sotto la propria frequenza di Nyquist (Fs/2). Se l'energia collassa nel rumore gia' a ~22 kHz,
     il materiale proviene quasi certamente da una sorgente 44.1/48 kHz risamplata: la banda alta e'
     vuota, riempita solo dall'interpolazione.
  2. Profondita' di bit gonfiata: un contenitore a 24 bit i cui campioni usano di fatto solo i 16 bit
     alti (gli 8 bit bassi sono sempre zero), cioe' un 16 bit impacchettato in 24.

Metodo di signal processing (vedi il documento di accompagnamento in
docs/02-audio/spectral-analysis-metodo.md):

  - PSD media stile Welch: segmentazione con finestra di Hann, sovrapposizione 50%, media del modulo
    quadro della rFFT sui segmenti. Riduce la varianza della stima rispetto a una singola FFT e da'
    una stima stabile dello spettro medio del brano.
  - Cutoff effettivo: massima frequenza in cui la PSD (in dB rispetto al picco, dopo lisciatura)
    supera una soglia di piano (default -80 dB). Confrontato con Fs/2 rivela la banda realmente
    occupata.
  - Frazioni di energia in bande [0-20k], [20k-22.05k], [>22.05k]: l'energia oltre 22.05 kHz e' la
    firma di contenuto genuino oltre la banda del CD.
  - Profondita' di bit reale: OR bit a bit dei campioni interi; il numero di LSB sempre a zero da' i
    bit inutilizzati.

Per l'ispezione visiva rapida resta ottimo Spek (open source); questo strumento aggiunge la misura
numerica e un verdetto deterministico, piu' un PNG dello spettrogramma.

Dipendenze: numpy, soundfile (decodifica FLAC/WAV/AIFF), matplotlib (solo per il PNG, opzionale).

Uso:
    python spectral-audit.py traccia.flac
    python spectral-audit.py traccia.flac --png spettro.png --seconds 90
    python spectral-audit.py traccia.flac --no-plot
"""

import argparse
import os
import sys

import numpy as np

try:
    import soundfile as sf
except ImportError:
    print("Manca 'soundfile'. Installa con: python -m pip install --user soundfile")
    sys.exit(2)

LOSSY_CUTOFFS = [16000, 17500, 19000, 20000, 20500, 21000, 22050]


def read_excerpt(path, max_seconds):
    """Legge un estratto centrato (float64, mono downmix) e ne ritorna anche info e int per i bit."""
    info = sf.info(path)
    fs = info.samplerate
    total = info.frames
    want = int(max_seconds * fs) if max_seconds else total
    want = min(want, total)
    start = max(0, (total - want) // 2)

    with sf.SoundFile(path) as f:
        f.seek(start)
        data = f.read(want, dtype="float64", always_2d=True)
    mono = data.mean(axis=1)

    ints = None
    if info.subtype and info.subtype.startswith("PCM"):
        with sf.SoundFile(path) as f:
            f.seek(start)
            ints = f.read(want, dtype="int32", always_2d=True)
    return fs, info, mono, ints


def welch_psd(x, fs, nperseg):
    if len(x) < nperseg:
        nperseg = 1 << int(np.floor(np.log2(max(256, len(x)))))
    win = np.hanning(nperseg)
    step = nperseg // 2
    acc = None
    n = 0
    for s in range(0, len(x) - nperseg + 1, step):
        seg = x[s:s + nperseg] * win
        p = np.abs(np.fft.rfft(seg)) ** 2
        acc = p if acc is None else acc + p
        n += 1
    if n == 0:
        seg = np.zeros(nperseg)
        seg[:len(x)] = x
        acc = np.abs(np.fft.rfft(seg * win)) ** 2
        n = 1
    psd = acc / n
    freqs = np.fft.rfftfreq(nperseg, 1.0 / fs)
    return freqs, psd


def spectral_rolloff(freqs, psd, p):
    """Frequenza sotto cui si concentra la frazione p dell'energia (rolloff percentile).
    Robusto ai singoli bin di rumore ad alta frequenza, a differenza del massimo bin
    sopra soglia: stima in modo stabile dove finisce davvero il contenuto."""
    c = np.cumsum(psd)
    if c[-1] <= 0:
        return 0.0
    idx = int(np.searchsorted(c, p * c[-1]))
    idx = min(idx, len(freqs) - 1)
    return float(freqs[idx])


def band_fraction(freqs, psd, lo, hi):
    m = (freqs >= lo) & (freqs < hi)
    tot = psd.sum()
    return float(psd[m].sum() / tot) if tot > 0 else 0.0


def effective_bits(ints):
    """Numero di bit realmente usati, da OR bit a bit dei campioni interi (dtype int32)."""
    if ints is None:
        return None
    u = (ints.astype(np.int64) & 0xFFFFFFFF).astype(np.uint32)
    orv = int(np.bitwise_or.reduce(u.reshape(-1)))
    if orv == 0:
        return 0
    # bit meno significativo settato -> LSB inutilizzati sotto di esso
    trailing = (orv & -orv).bit_length() - 1
    return 32 - trailing


def near_any(value, targets, tol=400):
    return [t for t in targets if abs(value - t) <= tol]


def make_png(mono, fs, out_png, nperseg=4096):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except Exception as e:
        print("PNG non generato (matplotlib assente):", e)
        return
    step = nperseg // 4
    win = np.hanning(nperseg)
    cols = []
    for s in range(0, max(1, len(mono) - nperseg + 1), step):
        seg = mono[s:s + nperseg] * win
        cols.append(20 * np.log10(np.abs(np.fft.rfft(seg)) + 1e-9))
    S = np.array(cols).T
    freqs = np.fft.rfftfreq(nperseg, 1.0 / fs)
    dur = len(mono) / fs
    vmax = S.max()
    plt.figure(figsize=(11, 5))
    plt.imshow(S, origin="lower", aspect="auto",
               extent=[0, dur, 0, freqs[-1] / 1000.0],
               vmin=vmax - 120, vmax=vmax, cmap="magma")
    plt.colorbar(label="dB")
    plt.axhline(22.05, color="cyan", lw=0.6, ls="--")
    plt.ylabel("Frequenza [kHz]")
    plt.xlabel("Tempo [s]")
    plt.title("Spettrogramma - %s (Fs=%d Hz, Nyquist=%.1f kHz)" % (os.path.basename(out_png), fs, fs / 2000.0))
    plt.tight_layout()
    plt.savefig(out_png, dpi=110)
    plt.close()
    print("Spettrogramma salvato:", out_png)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--seconds", type=float, default=120, help="secondi da analizzare (0 = tutto)")
    ap.add_argument("--nperseg", type=int, default=16384, help="lunghezza finestra FFT per la PSD")
    ap.add_argument("--rolloff", type=float, default=0.999, help="percentile di energia per il cutoff")
    ap.add_argument("--png", default=None, help="percorso PNG dello spettrogramma")
    ap.add_argument("--no-plot", action="store_true", help="non generare il PNG")
    args = ap.parse_args()

    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    if not os.path.exists(args.file):
        print("File non trovato:", args.file)
        sys.exit(2)

    fs, info, mono, ints = read_excerpt(args.file, args.seconds)
    nyq = fs / 2.0
    freqs, psd = welch_psd(mono, fs, args.nperseg)
    cutoff = spectral_rolloff(freqs, psd, args.rolloff)

    e_20 = band_fraction(freqs, psd, 20000, nyq)
    e_2205 = band_fraction(freqs, psd, 22050, nyq)
    ebits = effective_bits(ints)

    print("=== Analisi spettrale ===")
    print("File           :", os.path.basename(args.file))
    print("Formato        : Fs=%d Hz, canali=%d, subtype=%s" % (fs, info.channels, info.subtype))
    print("Durata totale  : %.1f s (analizzati %.1f s centrali)" % (info.frames / fs, len(mono) / fs))
    print("Nyquist (Fs/2) : %.2f kHz" % (nyq / 1000.0))
    print("Cutoff (rolloff %.1f%%): %.2f kHz (%.1f%% di Nyquist)"
          % (100.0 * args.rolloff, cutoff / 1000.0, 100.0 * cutoff / nyq if nyq else 0))
    print("Energia >20 kHz   : %.3e   (frazione del totale)" % e_20)
    print("Energia >22.05 kHz: %.3e" % e_2205)
    if ebits is not None:
        print("Profondita' bit reale: ~%d bit (contenitore: %s)" % (ebits, info.subtype))

    print("\n=== Verdetto ===")
    verdicts = []
    if fs > 48000 and cutoff < 22500:
        verdicts.append("SOSPETTO UPSAMPLE: contenuto limitato alla banda del CD (~%.1f kHz) in un file a "
                         "%d Hz. La banda alta e' vuota: probabile risampling da 44.1/48 kHz."
                         % (cutoff / 1000.0, fs))
    hits = near_any(cutoff, LOSSY_CUTOFFS) if cutoff < 0.97 * nyq else []
    if hits:
        verdicts.append("Cutoff a %.1f kHz vicino a valori tipici di transcodifica lossy (%s). Verifica in "
                        "Spek se il taglio e' netto (brickwall) come MP3/AAC."
                        % (cutoff / 1000.0, ", ".join("%.2f" % (h / 1000.0) for h in hits)))
    if e_2205 < 1e-4 and fs > 48000:
        verdicts.append("Energia ultrasonica (>22.05 kHz) trascurabile: nessun contenuto genuino oltre la "
                        "banda CD.")
    if ebits is not None and info.subtype == "PCM_24" and ebits <= 16:
        verdicts.append("PROFONDITA' GONFIATA: contenitore 24 bit ma solo ~%d bit realmente usati "
                        "(16 bit impacchettato in 24)." % ebits)
    if not verdicts:
        if fs > 48000 and cutoff >= 0.9 * min(nyq, 24000) and e_2205 >= 1e-4:
            verdicts.append("COERENTE: contenuto esteso verso Nyquist ed energia genuina oltre 22.05 kHz, "
                            "compatibile con un hi-res autentico.")
        else:
            verdicts.append("Nessuna anomalia evidente dai soli indicatori; incrocia con lo spettrogramma.")

    for v in verdicts:
        print(" -", v)

    print("\nNota: il cutoff e le bande sono indicatori robusti ma non infallibili. Alcune registrazioni "
          "genuine hanno poca energia in alta frequenza (strumentazione, microfonaggio); un brickwall netto "
          "resta il segno piu' affidabile di transcodifica lossy. Incrocia sempre con l'ispezione visiva.")

    if not args.no_plot:
        out_png = args.png or (os.path.splitext(args.file)[0] + "-spectrogram.png")
        make_png(mono, fs, out_png)


if __name__ == "__main__":
    main()
