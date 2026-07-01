#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
track-benchmark.py - Benchmark di qualita' deterministico per una traccia/album.

Dato il master di riferimento di un pezzo (formato bit/sample rate/canali) e la durata,
calcola in modo deterministico il bitrate PCM teorico, il range FLAC realistico e la
dimensione attesa. Se gli si passa la dimensione o il bitrate reale di un file, emette un
verdetto di autenticita': stabilisce se quel file e' plausibilmente di quella qualita' o se
e' compatibile con un formato piu' basso (tipico upsample o fake hi-res).

Le formule e i criteri anti-fake provengono dalla sezione audio
`docs/02-audio/02-calculation-for-benchmark-to-download` e da
`docs/02-audio/01-useful-concepts/05-so-what-really-defines-the-quality.md`:

    PCM [kbps]        = bit_depth * sample_rate_kHz * channels
    FLAC realistico   = PCM * [0.45 .. 0.65]   (compressione tipica della musica reale)
    Dimensione [MB]   = FLAC_kbps * durata_min * 60 / 8 / 1000
    bitrate reale     = dimensione_MB * 8000 / (durata_min * 60)

Il "miglior master" per un pezzo non e' un calcolo ma conoscenza del mondo reale: vive in un
database curato (`masters.json`), che si semina dalla tabella album con --seed. Per un pezzo non
in database si passa il formato a mano con --format.

Uso:
    # cerca il master nel DB e mostra il benchmark atteso
    python track-benchmark.py "Pink Floyd" "Dark Side" --duration 42:00

    # verdetto di autenticita' su un file reale
    python track-benchmark.py "Daft Punk" "Random Access Memories" --duration 74:00 --size 2800

    # formato esplicito, senza DB
    python track-benchmark.py --format 24/192 --duration 6:53 --size 190

    # rigenera il database dei master dalla tabella album (file locale)
    python track-benchmark.py --seed album_hires_tracklist.md
"""

import argparse
import io
import json
import os
import re
import sys

FLAC_LOW = 0.45
FLAC_HIGH = 0.65
FLAC_POINT = 0.55

# formati di riferimento per stimare a quale qualita' reale corrisponde un bitrate
REF_FORMATS = [(16, 44.1), (16, 48.0), (24, 44.1), (24, 48.0),
               (24, 88.2), (24, 96.0), (24, 176.4), (24, 192.0)]

DEFAULT_DB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "masters.json")


def parse_float(s):
    s = (s or "").strip().replace(",", ".")
    m = re.search(r"-?\d+(?:\.\d+)?", s)
    return float(m.group(0)) if m else None


def fmt_num(x):
    r = round(x, 3)
    if r == int(r):
        return str(int(r))
    return ("%.3f" % r).rstrip("0").rstrip(".")


def parse_duration_to_min(dur, minutes):
    if minutes is not None:
        return minutes
    if not dur:
        return None
    dur = dur.strip()
    if ":" in dur:
        parts = dur.split(":")
        try:
            parts = [float(p) for p in parts]
        except ValueError:
            return None
        if len(parts) == 2:
            return parts[0] + parts[1] / 60.0
        if len(parts) == 3:
            return parts[0] * 60 + parts[1] + parts[2] / 60.0
        return None
    return parse_float(dur)


def parse_format(fmt):
    """"24/96" -> (24.0, 96.0)."""
    m = re.match(r"\s*(\d+(?:\.\d+)?)\s*/\s*(\d+(?:\.\d+)?)\s*$", fmt or "")
    if not m:
        return None
    return float(m.group(1)), float(m.group(2))


def split_row(line):
    cells = line.split("|")
    if cells and cells[0].strip() == "":
        cells = cells[1:]
    if cells and cells[-1].strip() == "":
        cells = cells[:-1]
    return [c.strip() for c in cells]


# ---------------------------------------------------------------------------
def seed(tracklist_path, db_path):
    with io.open(tracklist_path, encoding="utf-8-sig") as fh:
        lines = fh.read().split("\n")
    header_idx = None
    for i, line in enumerate(lines):
        if line.strip().startswith("|") and "Album" in line and "Bit Depth" in line:
            header_idx = i
            break
    if header_idx is None:
        print("Tabella non trovata in", tracklist_path)
        sys.exit(2)
    headers = split_row(lines[header_idx])
    col = {name: idx for idx, name in enumerate(headers)}

    def cell(cells, name):
        return cells[col[name]] if name in col and col[name] < len(cells) else ""

    masters = []
    for line in lines[header_idx + 2:]:
        if not line.strip().startswith("|"):
            break
        c = split_row(line)
        if len(c) < len(headers):
            continue
        artist = cell(c, "Artist")
        album = cell(c, "Album")
        if not artist and not album:
            continue
        masters.append({
            "artist": artist,
            "album": album,
            "year": cell(c, "Year"),
            "master": cell(c, "Benchmark"),
            "bit": parse_float(cell(c, "Bit Depth")),
            "sr": parse_float(cell(c, "Sample rate [kHz]")),
            "channels": parse_float(cell(c, "Channels")) or 2,
            "dr": cell(c, "DR estimated (dB)"),
        })
    with io.open(db_path, "w", encoding="utf-8") as fh:
        json.dump({"masters": masters}, fh, ensure_ascii=False, indent=2)
    print("Database master scritto:", db_path, "-", len(masters), "voci")


def load_masters(db_path):
    if not os.path.exists(db_path):
        return []
    with io.open(db_path, encoding="utf-8") as fh:
        return json.load(fh).get("masters", [])


def find_master(masters, query):
    q = query.lower().strip()
    hits = [m for m in masters
            if q in ("%s %s" % (m.get("artist", ""), m.get("album", ""))).lower()]
    return hits


def dr_note(dr_str):
    nums = [float(x) for x in re.findall(r"\d+(?:\.\d+)?", dr_str or "")]
    if not nums:
        return None
    mid = sum(nums) / len(nums)
    if mid >= 13:
        q = "eccellente, molto dinamico"
    elif mid >= 11:
        q = "buono"
    elif mid >= 8:
        q = "medio"
    else:
        q = "compresso (loudness war)"
    return "DR %s -> %s" % (dr_str, q)


def matching_ref_formats(actual_kbps, ch):
    out = []
    for bit, sr in REF_FORMATS:
        pcm = bit * sr * ch
        if pcm * FLAC_LOW <= actual_kbps <= pcm * FLAC_HIGH:
            out.append("%d/%s" % (bit, fmt_num(sr)))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("query", nargs="*", help="artista e/o album da cercare nel DB")
    ap.add_argument("--artist", default="")
    ap.add_argument("--album", default="")
    ap.add_argument("--format", default=None, help="formato esplicito, es. 24/96 (bypassa il DB)")
    ap.add_argument("--channels", type=float, default=2)
    ap.add_argument("--duration", default=None, help="durata mm:ss (o hh:mm:ss)")
    ap.add_argument("--minutes", type=float, default=None, help="durata in minuti (decimale)")
    ap.add_argument("--size", type=float, default=None, help="dimensione reale del file in MB")
    ap.add_argument("--bitrate", type=float, default=None, help="bitrate reale del file in kbps")
    ap.add_argument("--flac-low", type=float, default=FLAC_LOW)
    ap.add_argument("--flac-high", type=float, default=FLAC_HIGH)
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--seed", default=None, help="rigenera il DB dalla tabella album indicata")
    args = ap.parse_args()

    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    if args.seed:
        seed(args.seed, args.db)
        return

    bit = sr = None
    ch = args.channels
    dr = None
    master_label = None
    src = None

    if args.format:
        f = parse_format(args.format)
        if not f:
            print("Formato non valido:", args.format, "(atteso es. 24/96)")
            sys.exit(2)
        bit, sr = f
    else:
        query = " ".join(args.query) or ("%s %s" % (args.artist, args.album)).strip()
        if not query:
            print("Indica un artista/album (o usa --format). Es: track-benchmark.py \"Pink Floyd\" \"Dark Side\"")
            sys.exit(2)
        masters = load_masters(args.db)
        hits = find_master(masters, query)
        if not hits:
            print("Nessun master per '%s' nel database (%s)." % (query, args.db))
            print("Passa il formato a mano con --format 24/96, oppure aggiungilo al DB.")
            sys.exit(3)
        if len(hits) > 1:
            print("Piu' corrispondenze per '%s':" % query)
            for m in hits:
                print("  -", m.get("artist"), "-", m.get("album"), "(", m.get("master"), ")")
            print("Restringi la ricerca.")
            sys.exit(3)
        m = hits[0]
        bit, sr, ch = m.get("bit"), m.get("sr"), m.get("channels") or ch
        dr = m.get("dr")
        master_label = "%s - %s (%s)" % (m.get("artist"), m.get("album"), m.get("year"))
        src = m.get("master")

    if bit is None or sr is None:
        print("Formato del master mancante o non leggibile.")
        sys.exit(2)

    minutes = parse_duration_to_min(args.duration, args.minutes)

    pcm = bit * sr * ch
    flac_lo = pcm * args.flac_low
    flac_hi = pcm * args.flac_high
    flac_mid = pcm * FLAC_POINT

    print("=== Benchmark di qualita' ===")
    if master_label:
        print("Master (da DB):", master_label)
        if src:
            print("  edizione     :", src)
    print("Formato        : %s/%s, %s canali" % (fmt_num(bit), fmt_num(sr), fmt_num(ch)))
    if dr:
        note = dr_note(dr)
        if note:
            print("Dinamica       :", note)
    print("PCM teorico    : %s kbps" % fmt_num(pcm))
    print("FLAC realistico: %s - %s kbps (punto ~%s)" % (fmt_num(flac_lo), fmt_num(flac_hi), fmt_num(flac_mid)))

    if minutes:
        def mb(kbps):
            return kbps * minutes * 60.0 / 8.0 / 1000.0
        print("Durata         : %s min" % fmt_num(minutes))
        print("Dimensione attesa (FLAC): %s - %s MB" % (fmt_num(mb(flac_lo)), fmt_num(mb(flac_hi))))

    # verdetto di autenticita'
    actual = None
    if args.bitrate is not None:
        actual = args.bitrate
    elif args.size is not None and minutes:
        actual = args.size * 8000.0 / (minutes * 60.0)
    elif args.size is not None and not minutes:
        print("\nPer valutare la dimensione serve anche la durata (--duration).")

    if actual is not None:
        print("\n=== Verdetto di autenticita' ===")
        print("Bitrate reale del file: %s kbps" % fmt_num(actual))
        if flac_lo <= actual <= flac_hi:
            print("PLAUSIBILE: compatibile con un FLAC %s/%s autentico." % (fmt_num(bit), fmt_num(sr)))
        elif actual > flac_hi:
            print("SOPRA IL RANGE: piu' grande dell'atteso. Possibile bassa compressione o traccia "
                  "molto densa; non indica un fake, ma verifica l'origine.")
        else:
            print("SOTTO IL RANGE: SOSPETTO. Il bitrate e' troppo basso per un %s/%s autentico."
                  % (fmt_num(bit), fmt_num(sr)))
            comp = matching_ref_formats(actual, ch)
            if comp:
                print("  Il bitrate reale e' compatibile con: %s" % ", ".join(comp))
                print("  Probabile upsample o rietichettatura da un formato piu' basso.")
            else:
                print("  Non compatibile nemmeno con i formati di riferimento: verifica il file "
                      "(potrebbe essere lossy travestito da FLAC).")
        print("\nNota: analisi da metadati e dimensione. La prova definitiva del contenuto reale "
              "e' lo spettrogramma (taglio in frequenza), non deducibile da qui.")


if __name__ == "__main__":
    main()
