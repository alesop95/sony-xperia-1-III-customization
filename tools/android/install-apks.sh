#!/usr/bin/env bash
# Installa via ADB le APK attive del progetto sul Sony Xperia 1 III, nell'ordine di dipendenza.
#
# Usa "adb install -r" e prosegue anche se una singola installazione fallisce, riepilogando gli
# esiti. Le APK legacy (GCam) sono escluse salvo --include-legacy. Richiede un dispositivo collegato
# con debug USB attivo.
#
# Uso:
#   ./install-apks.sh [--include-legacy] [--apk-dir DIR] [--platform-tools DIR]

set -u

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
APK_DIR="$REPO_ROOT/_notes/apks"
PLATFORM_TOOLS=""
INCLUDE_LEGACY=0

while [ $# -gt 0 ]; do
    case "$1" in
        --include-legacy) INCLUDE_LEGACY=1; shift ;;
        --apk-dir) APK_DIR="$2"; shift 2 ;;
        --platform-tools) PLATFORM_TOOLS="$2"; shift 2 ;;
        *) echo "Argomento sconosciuto: $1"; exit 2 ;;
    esac
done

# Ordine di installazione dell'insieme attivo (dipendenze prima).
ACTIVE_ORDER=(
    "com.sonymobile.cameracommon.permission_1.5.A.0.0.apk"
    "Camera_common_3.2.apk"
    "Photography_Pro_1.3.2.A.1.0.apk"
    "Cinema_Pro_1.7.1.A.0.10.apk"
    "com.sonymobile.extmonitorapp_7.0.A.0.8-14680072.apk"
    "com.extreamsd.usbaudioplayerpro--7016.apk"
    "APKPure_v3.20.51_apkpure.com.apk"
    "com.huawei.appmarket.2311221502.apk"
)
LEGACY=("MGC_8.1.101_A9_GV1zfix_MGC.apk")

# Risoluzione di adb.
if [ -n "$PLATFORM_TOOLS" ] && [ -x "$PLATFORM_TOOLS/adb" ]; then
    ADB="$PLATFORM_TOOLS/adb"
else
    ADB="$(command -v adb 2>/dev/null || true)"
fi
if [ -z "$ADB" ]; then
    echo "adb non trovato. Installa platform-tools o passa --platform-tools."; exit 2
fi
if [ ! -d "$APK_DIR" ]; then
    echo "Cartella APK non trovata: $APK_DIR"; exit 2
fi

STATE="$("$ADB" get-state 2>&1 | tr -d '\r')"
if [ "$STATE" != "device" ]; then
    echo "Nessun dispositivo pronto (stato adb: '$STATE')."
    echo "Collega il telefono, abilita il debug USB e autorizza il PC, poi riprova."
    exit 3
fi

LIST=("${ACTIVE_ORDER[@]}")
[ "$INCLUDE_LEGACY" -eq 1 ] && LIST+=("${LEGACY[@]}")

declare -a SUMMARY
FAILED=0
for name in "${LIST[@]}"; do
    path="$APK_DIR/$name"
    if [ ! -f "$path" ]; then
        echo "[SKIP] non trovato: $name"
        SUMMARY+=("MANCANTE  $name")
        continue
    fi
    echo "[INSTALL] $name"
    out="$("$ADB" install -r "$path" 2>&1)"
    if echo "$out" | grep -q "Success"; then
        echo "  OK"
        SUMMARY+=("OK        $name")
    else
        echo "  FALLITO: $(echo "$out" | tail -1)"
        SUMMARY+=("FALLITO   $name")
        FAILED=1
    fi
done

echo ""
echo "=== Riepilogo ==="
printf '%s\n' "${SUMMARY[@]}"
if [ "$FAILED" -eq 1 ]; then
    echo "Alcune installazioni sono fallite. La permission camera Sony e' nota per poter fallire: vedi 03-foto-video/RUNBOOK.md."
fi
