# Runbook gaming - emulazione 3DS (Citra MMJ)

> Percorso operativo per l'emulazione, ripreso dalle sezioni gaming di questa cartella. Copre
> l'emulazione 3DS con Citra MMJ, che e' la parte piu' sviluppata nel materiale; l'emulazione
> Switch (Strato) e' solo introdotta nelle sezioni e non ha ancora una procedura consolidata.
> Riferimenti: `02-emulazione-3ds/02-installazione-citra-mmj-modded-citra.md`.

## Prerequisiti

LineageOS avviato, debug USB attivo, ADB sul PC. Citra MMJ non e' tra le APK in `_notes/apks`
(quella cartella contiene la sua sola `config.ini`): l'APK si scarica da APKPure, F-Droid o GitHub,
ad esempio tramite lo store APKPure gia' previsto nell'inventario.

## Fase 1 - Installare Citra MMJ

Dopo aver scaricato l'APK (fork modificato di Citra, build di riferimento 99a89d290 del 20 giugno
2024, arm64-v8a, Android 7.0+), si installa da PC.

```powershell
adb install -r "Citra_MMJ.apk"
```

## Fase 2 - Deploy della configurazione ottimizzata

La configurazione ottimizzata per l'Xperia 1 III e' pronta in `citra-config.ini` accanto a questo
runbook. Le build recenti di Citra MMJ usano una directory nella root interna del dispositivo, non
in `Android/data`. Si copia il file al percorso seguente.

```powershell
adb push "docs/04-gaming/citra-config.ini" "/sdcard/citra-emu/config/config.ini"
```

La struttura attesa nella root interna comprende anche `citra-emu/shaders/`, `citra-emu/load/textures/`,
`citra-emu/cheats/`, `citra-emu/nand/`, `citra-emu/sdmc/`. I parametri chiave della config sono il
rendering hardware con shader JIT, il fattore di risoluzione 3 (circa 720p, adatto al display) e il
filtro lineare; per giochi leggeri si puo' salire a `ResolutionFactor=4` (1080p).

## Fase 3 - Texture pack, upscaling, shader, cheat

Le texture pack HD vanno in `/citra-emu/load/textures/<ID_GIOCO>/`, dove l'ID gioco si legge nel
titolo della finestra o nel log avviando il gioco. Nell'app, in Graphics, Advanced, si attiva Use
Custom Textures, e opzionalmente Texture Filter Linear, Enable Hardware Shader e Shader JIT. I cheat
sono file `.txt` da caricare; le mod (patch 60 FPS, traduzioni, QoL) in `.ips` o `.xdelta` vanno in
`/Android/data/org.citra.citra_mmj/files/citra-emu/patches/`.

Il dettaglio completo, con le fonti per texture, mod e cheat, e' nella sezione
`02-emulazione-3ds/02-installazione-citra-mmj-modded-citra.md`.

## Fase 4 - Moduli Magisk per le prestazioni (richiede root)

Il materiale cita quattro moduli Magisk per spingere l'emulazione: Adreno Boost (driver ottimizzati),
Thermal Daemon Off (disattiva il throttling termico), LKT oppure NFSInjector (scheduler I/O e CPU),
GPU Turbo Boost. Questi moduli sono di terze parti e vanno reperiti dalle rispettive fonti: il
materiale non ne include i file, quindi qui non vengono forniti contenuti inventati. Per impacchettare
o adattare un modulo si parte dallo scheletro in `tools/magisk/skeleton/`. Il root via Magisk e'
prerequisito e si ottiene con il runbook software, fase 8.

Nota: disattivare il throttling termico e forzare la GPU aumenta il calore e il consumo; va valutato
caso per caso e non e' privo di rischi sul lungo periodo.
