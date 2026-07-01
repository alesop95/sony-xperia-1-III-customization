<#
.SYNOPSIS
    Preflight di sola lettura per Sony Xperia 1 III (pdx215) prima delle operazioni di flashing.

.DESCRIPTION
    Esegue esclusivamente comandi diagnostici non distruttivi via adb e fastboot, fotografa lo
    stato del dispositivo (modalita', slot attivo, stato del bootloader, proprieta' di build) e
    salva il dump completo di "fastboot getvar all" in un log datato sotto _notes/android-logs/
    (cartella ignorata da git). Stampa infine il verdetto dei gate del runbook software.

    Non flasha, non sblocca, non cambia slot: nessun comando modifica il dispositivo.

.PARAMETER PlatformTools
    Percorso opzionale della cartella platform-tools contenente adb.exe e fastboot.exe.
    Se omesso, adb e fastboot vengono cercati nel PATH.

.EXAMPLE
    pwsh -File tools/android/xperia-preflight.ps1
    pwsh -File tools/android/xperia-preflight.ps1 -PlatformTools "C:\platform-tools"
#>
[CmdletBinding()]
param(
    [string]$PlatformTools
)

$ErrorActionPreference = "Stop"

function Resolve-Tool {
    param([string]$Name)
    if ($PlatformTools) {
        $candidate = Join-Path $PlatformTools ("{0}.exe" -f $Name)
        if (Test-Path $candidate) { return $candidate }
        Write-Warning ("{0} non trovato in {1}; provo nel PATH." -f $Name, $PlatformTools)
    }
    $cmd = Get-Command $Name -ErrorAction SilentlyContinue
    if ($cmd) { return $cmd.Source }
    return $null
}

function Invoke-Tool {
    # Esegue lo strumento catturando stdout+stderr (fastboot scrive getvar su stderr).
    param([string]$Exe, [string[]]$ToolArgs)
    try {
        $out = & $Exe @ToolArgs 2>&1 | Out-String
        return $out.Trim()
    } catch {
        return ("ERRORE: {0}" -f $_.Exception.Message)
    }
}

Write-Host "=== Preflight Xperia 1 III (pdx215) - sola lettura ===" -ForegroundColor Cyan

$adb = Resolve-Tool -Name "adb"
$fastboot = Resolve-Tool -Name "fastboot"

if (-not $adb)      { Write-Warning "adb non trovato. Installa platform-tools o passa -PlatformTools." }
if (-not $fastboot) { Write-Warning "fastboot non trovato. Installa platform-tools o passa -PlatformTools." }
if (-not $adb -and -not $fastboot) {
    Write-Host "Nessuno strumento disponibile: impossibile procedere." -ForegroundColor Red
    exit 2
}

# --- rilevamento modalita' ---
$adbDevices = ""
$adbPresent = $false
if ($adb) {
    $adbDevices = Invoke-Tool -Exe $adb -ToolArgs @("devices")
    $adbPresent = ($adbDevices -split "`n" | Where-Object { $_ -match "\t(device|recovery|sideload)\b" }).Count -gt 0
}

$fbDevices = ""
$fbPresent = $false
if ($fastboot) {
    $fbDevices = Invoke-Tool -Exe $fastboot -ToolArgs @("devices")
    $fbPresent = ($fbDevices -split "`n" | Where-Object { $_ -match "\tfastboot\b" }).Count -gt 0
}

Write-Host ""
Write-Host "adb devices:" -ForegroundColor Yellow
Write-Host ($(if ($adbDevices) { $adbDevices } else { "(adb non disponibile)" }))
Write-Host ""
Write-Host "fastboot devices:" -ForegroundColor Yellow
Write-Host ($(if ($fbDevices) { $fbDevices } else { "(fastboot non disponibile)" }))

# --- stato gate ---
$activeSlot = $null
$unlocked = $null

if ($adbPresent) {
    Write-Host ""
    Write-Host "Proprieta' (Android/recovery via adb):" -ForegroundColor Yellow
    $model  = Invoke-Tool -Exe $adb -ToolArgs @("shell", "getprop", "ro.product.model")
    $rel    = Invoke-Tool -Exe $adb -ToolArgs @("shell", "getprop", "ro.build.version.release")
    $lineage = Invoke-Tool -Exe $adb -ToolArgs @("shell", "getprop", "ro.lineage.version")
    $disp   = Invoke-Tool -Exe $adb -ToolArgs @("shell", "getprop", "ro.build.display.id")
    $slot   = Invoke-Tool -Exe $adb -ToolArgs @("shell", "getprop", "ro.boot.slot_suffix")
    Write-Host ("  Modello       : {0}" -f $model)
    Write-Host ("  Android       : {0}" -f $rel)
    Write-Host ("  LineageOS     : {0}" -f $lineage)
    Write-Host ("  Build display : {0}" -f $disp)
    Write-Host ("  Slot attivo   : {0}" -f $slot)
    if ($slot) { $activeSlot = $slot.TrimStart("_") }
}

if ($fbPresent) {
    Write-Host ""
    Write-Host "Stato bootloader (fastboot):" -ForegroundColor Yellow
    $curSlot = Invoke-Tool -Exe $fastboot -ToolArgs @("getvar", "current-slot")
    $unl     = Invoke-Tool -Exe $fastboot -ToolArgs @("getvar", "unlocked")
    $devInfo = Invoke-Tool -Exe $fastboot -ToolArgs @("oem", "device-info")
    Write-Host ("  current-slot  : {0}" -f $curSlot)
    Write-Host ("  unlocked      : {0}" -f $unl)
    Write-Host "  oem device-info:"
    Write-Host ($devInfo -split "`n" | ForEach-Object { "    " + $_ } | Out-String).TrimEnd()

    if ($curSlot -match "current-slot:\s*([ab])") { $activeSlot = $Matches[1] }
    if ($unl -match "unlocked:\s*yes" -or $devInfo -match "Device unlocked:\s*true") { $unlocked = $true }
    elseif ($unl -match "unlocked:\s*no" -or $devInfo -match "Device unlocked:\s*false") { $unlocked = $false }

    # --- salvataggio getvar all ---
    $repoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..")).Path
    $logDir = Join-Path $repoRoot "_notes\android-logs"
    if (-not (Test-Path $logDir)) { New-Item -ItemType Directory -Path $logDir -Force | Out-Null }
    $stamp = Get-Date -Format "yyyyMMdd-HHmmss"
    $logFile = Join-Path $logDir ("getvar-all-{0}.txt" -f $stamp)
    $all = Invoke-Tool -Exe $fastboot -ToolArgs @("getvar", "all")
    Set-Content -Path $logFile -Value $all -Encoding UTF8
    Write-Host ""
    Write-Host ("Dump 'getvar all' salvato in: {0}" -f $logFile) -ForegroundColor Green
}

# --- verdetto gate ---
Write-Host ""
Write-Host "=== Gate del runbook ===" -ForegroundColor Cyan
if ($null -eq $unlocked) {
    Write-Host "  [?] Bootloader: stato sconosciuto (entra in fastboot per verificare)."
} elseif ($unlocked) {
    Write-Host "  [OK] Bootloader sbloccato." -ForegroundColor Green
} else {
    Write-Host "  [NO] Bootloader BLOCCATO: completa la Fase 3 prima di flashare." -ForegroundColor Red
}
if ($activeSlot) {
    Write-Host ("  [OK] Slot attivo individuato: {0}" -f $activeSlot) -ForegroundColor Green
} else {
    Write-Host "  [?] Slot attivo non determinato."
}
Write-Host ""
Write-Host "Nota: questo strumento non modifica il dispositivo. I passi di flash restano manuali."
