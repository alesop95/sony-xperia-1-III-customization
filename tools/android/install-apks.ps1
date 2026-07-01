<#
.SYNOPSIS
    Installa via ADB le APK attive del progetto sul Sony Xperia 1 III, nell'ordine di dipendenza.

.DESCRIPTION
    Installa l'insieme attivo di APK da _notes/apks rispettando l'ordine (permessi e libreria
    comune Sony prima delle app fotografiche). Usa "adb install -r" e prosegue anche se una singola
    installazione fallisce, riepilogando esiti alla fine. Le APK legacy (GCam) sono escluse salvo
    -IncludeLegacy. Richiede un dispositivo collegato con debug USB attivo.

.PARAMETER ApkDir
    Cartella con le APK. Default: _notes/apks nella radice del repository.

.PARAMETER PlatformTools
    Cartella platform-tools con adb.exe. Se omessa, adb viene cercato nel PATH.

.PARAMETER IncludeLegacy
    Se presente, installa anche le APK marcate legacy (GCam MGC).

.EXAMPLE
    pwsh -File tools/android/install-apks.ps1
#>
[CmdletBinding()]
param(
    [string]$ApkDir,
    [string]$PlatformTools,
    [switch]$IncludeLegacy
)

$ErrorActionPreference = "Stop"

$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..")).Path
if (-not $ApkDir) { $ApkDir = Join-Path $repoRoot "_notes\apks" }

# Ordine di installazione dell'insieme attivo (dipendenze prima).
$activeOrder = @(
    "com.sonymobile.cameracommon.permission_1.5.A.0.0.apk",
    "Camera_common_3.2.apk",
    "Photography_Pro_1.3.2.A.1.0.apk",
    "Cinema_Pro_1.7.1.A.0.10.apk",
    "com.sonymobile.extmonitorapp_7.0.A.0.8-14680072.apk",
    "com.extreamsd.usbaudioplayerpro--7016.apk",
    "APKPure_v3.20.51_apkpure.com.apk",
    "com.huawei.appmarket.2311221502.apk"
)
$legacy = @("MGC_8.1.101_A9_GV1zfix_MGC.apk")

# Risoluzione di adb.
$adb = $null
if ($PlatformTools) {
    $candidate = Join-Path $PlatformTools "adb.exe"
    if (Test-Path $candidate) { $adb = $candidate }
}
if (-not $adb) {
    $cmd = Get-Command adb -ErrorAction SilentlyContinue
    if ($cmd) { $adb = $cmd.Source }
}
if (-not $adb) {
    Write-Host "adb non trovato. Installa platform-tools o passa -PlatformTools." -ForegroundColor Red
    exit 2
}

if (-not (Test-Path $ApkDir)) {
    Write-Host ("Cartella APK non trovata: {0}" -f $ApkDir) -ForegroundColor Red
    exit 2
}

# Verifica dispositivo collegato.
$state = (& $adb get-state 2>&1 | Out-String).Trim()
if ($state -ne "device") {
    Write-Host ("Nessun dispositivo pronto (stato adb: '{0}')." -f $state) -ForegroundColor Red
    Write-Host "Collega il telefono, abilita il debug USB e autorizza il PC, poi riprova."
    exit 3
}

$list = @() + $activeOrder
if ($IncludeLegacy) { $list += $legacy }

$results = @()
foreach ($name in $list) {
    $path = Join-Path $ApkDir $name
    if (-not (Test-Path $path)) {
        Write-Host ("[SKIP] non trovato: {0}" -f $name) -ForegroundColor Yellow
        $results += [pscustomobject]@{ Apk = $name; Esito = "MANCANTE" }
        continue
    }
    Write-Host ("[INSTALL] {0}" -f $name) -ForegroundColor Cyan
    $out = (& $adb install -r "$path" 2>&1 | Out-String)
    if ($out -match "Success") {
        Write-Host "  OK" -ForegroundColor Green
        $results += [pscustomobject]@{ Apk = $name; Esito = "OK" }
    } else {
        Write-Host ("  FALLITO: {0}" -f ($out.Trim())) -ForegroundColor Red
        $results += [pscustomobject]@{ Apk = $name; Esito = "FALLITO" }
    }
}

Write-Host ""
Write-Host "=== Riepilogo ===" -ForegroundColor Cyan
$results | Format-Table -AutoSize
if ($results | Where-Object { $_.Esito -eq "FALLITO" }) {
    Write-Host "Alcune installazioni sono fallite. La permission camera Sony e' nota per poter fallire: vedi 03-foto-video/RUNBOOK.md." -ForegroundColor Yellow
}
