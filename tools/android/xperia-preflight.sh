#!/usr/bin/env bash
# Preflight di sola lettura per Sony Xperia 1 III (pdx215) prima delle operazioni di flashing.
#
# Esegue solo comandi diagnostici non distruttivi via adb e fastboot, fotografa lo stato del
# dispositivo (modalita', slot attivo, stato del bootloader, proprieta' di build) e salva il dump
# di "fastboot getvar all" in un log datato sotto _notes/android-logs/ (ignorata da git). Stampa
# il verdetto dei gate del runbook software. Non flasha, non sblocca, non cambia slot.
#
# Uso:
#   ./xperia-preflight.sh                       # adb/fastboot dal PATH
#   ./xperia-preflight.sh /path/to/platform-tools

set -u

PLATFORM_TOOLS="${1:-}"

resolve_tool() {
    local name="$1"
    if [ -n "$PLATFORM_TOOLS" ] && [ -x "$PLATFORM_TOOLS/$name" ]; then
        echo "$PLATFORM_TOOLS/$name"; return 0
    fi
    command -v "$name" 2>/dev/null || true
}

ADB="$(resolve_tool adb)"
FASTBOOT="$(resolve_tool fastboot)"

echo "=== Preflight Xperia 1 III (pdx215) - sola lettura ==="

[ -z "$ADB" ]      && echo "WARN: adb non trovato (installa platform-tools o passa il percorso)."
[ -z "$FASTBOOT" ] && echo "WARN: fastboot non trovato (installa platform-tools o passa il percorso)."
if [ -z "$ADB" ] && [ -z "$FASTBOOT" ]; then
    echo "Nessuno strumento disponibile: impossibile procedere."; exit 2
fi

ADB_DEVICES=""; ADB_PRESENT=0
if [ -n "$ADB" ]; then
    ADB_DEVICES="$("$ADB" devices 2>&1)"
    echo "$ADB_DEVICES" | grep -Eq '	(device|recovery|sideload)\b' && ADB_PRESENT=1
fi

FB_DEVICES=""; FB_PRESENT=0
if [ -n "$FASTBOOT" ]; then
    FB_DEVICES="$("$FASTBOOT" devices 2>&1)"
    echo "$FB_DEVICES" | grep -Eq '	fastboot\b' && FB_PRESENT=1
fi

echo ""
echo "adb devices:"
echo "${ADB_DEVICES:-(adb non disponibile)}"
echo ""
echo "fastboot devices:"
echo "${FB_DEVICES:-(fastboot non disponibile)}"

ACTIVE_SLOT=""
UNLOCKED="unknown"

if [ "$ADB_PRESENT" -eq 1 ]; then
    echo ""
    echo "Proprieta' (Android/recovery via adb):"
    echo "  Modello       : $("$ADB" shell getprop ro.product.model 2>&1 | tr -d '\r')"
    echo "  Android       : $("$ADB" shell getprop ro.build.version.release 2>&1 | tr -d '\r')"
    echo "  LineageOS     : $("$ADB" shell getprop ro.lineage.version 2>&1 | tr -d '\r')"
    echo "  Build display : $("$ADB" shell getprop ro.build.display.id 2>&1 | tr -d '\r')"
    SLOT="$("$ADB" shell getprop ro.boot.slot_suffix 2>&1 | tr -d '\r')"
    echo "  Slot attivo   : $SLOT"
    ACTIVE_SLOT="${SLOT#_}"
fi

if [ "$FB_PRESENT" -eq 1 ]; then
    echo ""
    echo "Stato bootloader (fastboot):"
    CUR_SLOT="$("$FASTBOOT" getvar current-slot 2>&1)"
    UNL="$("$FASTBOOT" getvar unlocked 2>&1)"
    DEV_INFO="$("$FASTBOOT" oem device-info 2>&1)"
    echo "  current-slot  : $(echo "$CUR_SLOT" | grep -i current-slot | head -1)"
    echo "  unlocked      : $(echo "$UNL" | grep -i unlocked | head -1)"
    echo "  oem device-info:"
    echo "$DEV_INFO" | sed 's/^/    /'

    SLOT_MATCH="$(echo "$CUR_SLOT" | grep -oE 'current-slot:[[:space:]]*[ab]' | grep -oE '[ab]$' | head -1)"
    [ -n "$SLOT_MATCH" ] && ACTIVE_SLOT="$SLOT_MATCH"
    if echo "$UNL" | grep -qiE 'unlocked:[[:space:]]*yes' || echo "$DEV_INFO" | grep -qiE 'Device unlocked:[[:space:]]*true'; then
        UNLOCKED="yes"
    elif echo "$UNL" | grep -qiE 'unlocked:[[:space:]]*no' || echo "$DEV_INFO" | grep -qiE 'Device unlocked:[[:space:]]*false'; then
        UNLOCKED="no"
    fi

    SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
    LOG_DIR="$REPO_ROOT/_notes/android-logs"
    mkdir -p "$LOG_DIR"
    STAMP="$(date +%Y%m%d-%H%M%S)"
    LOG_FILE="$LOG_DIR/getvar-all-$STAMP.txt"
    "$FASTBOOT" getvar all > "$LOG_FILE" 2>&1
    echo ""
    echo "Dump 'getvar all' salvato in: $LOG_FILE"
fi

echo ""
echo "=== Gate del runbook ==="
case "$UNLOCKED" in
    yes) echo "  [OK] Bootloader sbloccato." ;;
    no)  echo "  [NO] Bootloader BLOCCATO: completa la Fase 3 prima di flashare." ;;
    *)   echo "  [?] Bootloader: stato sconosciuto (entra in fastboot per verificare)." ;;
esac
if [ -n "$ACTIVE_SLOT" ]; then
    echo "  [OK] Slot attivo individuato: $ACTIVE_SLOT"
else
    echo "  [?] Slot attivo non determinato."
fi
echo ""
echo "Nota: questo strumento non modifica il dispositivo. I passi di flash restano manuali."
