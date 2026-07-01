#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
benchmark-calc.py - Ricalcola le colonne derivate della tabella benchmark album e segnala
le incongruenze dei dati.

La tabella (album_hires_tracklist.md) elenca album hi-res con i parametri del master scelto.
Tre colonne sono derivate e qui vengono ricalcolate in modo deterministico dalle formule
documentate nella sezione audio "Calculation for benchmark to download":

    PCM bitrate [kbps]      = bit_depth * sample_rate_kHz * channels
    FLAC estimated [kbps]   = PCM bitrate * 0.55
    Dimension estimated [MB]= FLAC kbps * duration_min * 60 / 8 / 1000

Lo script non modifica le colonne di input (bit depth, sample rate, canali, durata), i campi
manuali (Downloaded?, Notes e le colonne della fonte) ne' la stima del DR. Ricalcola solo le tre colonne
derivate e riscrive la tabella preservando tutto il resto verbatim.

Inoltre confronta il testo della colonna Benchmark (es. "24/96", "16/44.1") con le colonne
bit depth e sample rate: se non coincidono, lo segnala come incongruenza da verificare a mano,
perche' la scelta del master corretto e' una decisione umana, non automatica.

Uso:
    python benchmark-calc.py [PATH] [--check]

    PATH    file markdown (default: album_hires_tracklist.md nella radice del repo)
    --check non riscrive il file, stampa solo il report
"""

import argparse
import io
import os
import re
import sys

FLAC_FACTOR = 0.55

PCM_COL = "PCM bitrate [kbps]"
FLAC_COL = "FLAC estimated [kbps]"
MB_COL = "Dimension estimated [MB]"
BIT_COL = "Bit Depth"
SR_COL = "Sample rate [kHz]"
CH_COL = "Channels"
DUR_COL = "Duration [min]"
BENCH_COL = "Benchmark"
ARTIST_COL = "Artist"
ALBUM_COL = "Album"


def fmt_num(x):
    """Formato compatto: niente decimali inutili, massimo 4 cifre decimali."""
    r = round(x, 4)
    if r == int(r):
        return str(int(r))
    s = ("%.4f" % r).rstrip("0").rstrip(".")
    return s


def parse_float(s):
    s = (s or "").strip().replace(",", ".")
    m = re.search(r"-?\d+(?:\.\d+)?", s)
    return float(m.group(0)) if m else None


def split_row(line):
    # rimuove i pipe di bordo e divide le celle
    cells = line.split("|")
    if cells and cells[0].strip() == "":
        cells = cells[1:]
    if cells and cells[-1].strip() == "":
        cells = cells[:-1]
    return [c.strip() for c in cells]


def is_separator(line):
    return bool(re.match(r"^\s*\|?\s*:?-{3,}", line)) and set(line.strip()) <= set("|-: ")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path", nargs="?", default=None)
    ap.add_argument("--check", action="store_true", help="non riscrive, stampa solo il report")
    args = ap.parse_args()

    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    path = args.path
    if not path:
        repo_root = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
        path = os.path.join(repo_root, "album_hires_tracklist.md")

    if not os.path.exists(path):
        print("File non trovato:", path)
        sys.exit(2)

    with io.open(path, encoding="utf-8-sig") as fh:
        lines = fh.read().split("\n")

    # individua header e separatore della tabella
    header_idx = None
    for i, line in enumerate(lines):
        if line.strip().startswith("|") and BENCH_COL in line and PCM_COL in line:
            header_idx = i
            break
    if header_idx is None:
        print("Tabella non trovata (header con", PCM_COL, "mancante).")
        sys.exit(2)

    headers = split_row(lines[header_idx])
    col = {name: idx for idx, name in enumerate(headers)}
    for required in (BIT_COL, SR_COL, CH_COL, DUR_COL, PCM_COL, FLAC_COL, MB_COL):
        if required not in col:
            print("Colonna mancante nell'header:", required)
            sys.exit(2)

    sep_idx = header_idx + 1
    if sep_idx >= len(lines) or not is_separator(lines[sep_idx]):
        print("Riga separatrice della tabella non trovata sotto l'header.")
        sys.exit(2)

    warnings = []
    recomputed = 0
    changed = 0

    for i in range(sep_idx + 1, len(lines)):
        line = lines[i]
        if not line.strip().startswith("|"):
            break  # fine tabella
        cells = split_row(line)
        if len(cells) < len(headers):
            cells += [""] * (len(headers) - len(cells))

        label = "%s - %s" % (cells[col.get(ARTIST_COL, 1)], cells[col.get(ALBUM_COL, 2)])
        bit = parse_float(cells[col[BIT_COL]])
        sr = parse_float(cells[col[SR_COL]])
        ch = parse_float(cells[col[CH_COL]])
        dur = parse_float(cells[col[DUR_COL]])

        if None in (bit, sr, ch, dur):
            warnings.append("[dati incompleti] %s: bit/sample/canali/durata non leggibili" % label)
            continue

        pcm = bit * sr * ch
        flac = pcm * FLAC_FACTOR
        mb = flac * dur * 60.0 / 8.0 / 1000.0

        for c, val in ((PCM_COL, pcm), (FLAC_COL, flac), (MB_COL, mb)):
            new = fmt_num(val)
            if cells[col[c]] != new:
                changed += 1
            cells[col[c]] = new
        recomputed += 1

        # incongruenza fra testo Benchmark e colonne bit/sample
        bench = cells[col[BENCH_COL]]
        m = re.search(r"(\d{2})\s*/\s*(\d+(?:\.\d+)?)", bench)
        if m:
            b_bit = float(m.group(1))
            b_sr = float(m.group(2))
            if abs(b_bit - bit) > 0.01 or abs(b_sr - sr) > 0.01:
                warnings.append(
                    "[incongruenza master] %s: Benchmark dice %s/%s ma le colonne sono %s/%s"
                    % (label, fmt_num(b_bit), fmt_num(b_sr), fmt_num(bit), fmt_num(sr))
                )

        lines[i] = "| " + " | ".join(cells) + " |"

    # report
    print("Righe ricalcolate:", recomputed)
    print("Celle derivate aggiornate:", changed)
    print("Incongruenze segnalate:", len(warnings))
    for w in warnings:
        print("  -", w)

    if args.check:
        print("\n(--check: file non modificato)")
        return

    with io.open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    print("\nFile aggiornato:", path)


if __name__ == "__main__":
    main()
