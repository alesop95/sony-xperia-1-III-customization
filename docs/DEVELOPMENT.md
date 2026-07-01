# Guida allo sviluppo del progetto

> Indice operativo del progetto di personalizzazione del Sony Xperia 1 III (pdx215) con LineageOS 22.2. Spiega come e' organizzato, come si usa, in che ordine si opera e cosa è pronto rispetto a cosa e' ancora da decidere. E' il punto di partenza per orientarsi; i dettagli vivono nei documenti di area e nei runbook.

## Impianto

Il progetto ha due meta'. La conoscenza vive in `docs/`, generata fedelmente dal documento sorgente di 201 pagine e divisa in quattro aree: software, audio, foto/video e gaming. Gli strumenti vivono in `tools/`, come script deterministici e riutilizzabili. La filosofia di lavoro e' preparare e documentare tutto prima, e collegare il telefono dopo, manualmente: nessuno script tocca il dispositivo da solo.

Ogni area ha le sue sezioni di riferimento generate dal sorgente, e dove la procedura e'
consolidata anche un `RUNBOOK.md` curato a mano: una sequenza lineare ed eseguibile con gate di sicurezza, che il generatore non sovrascrive.

## Come si usa

Si parte da `docs/README.md` per orientarsi tra le quattro aree. Per lavorare su un'area si apre il suo `RUNBOOK.md`, che rimanda alle sezioni di riferimento quando serve approfondire. Quando la procedura arriva ai passi fisici sul telefono, si eseguono gli strumenti in `tools/`: prima il preflight di sola lettura, poi l'installazione delle app. I punti visivi sul telefono, che non sono osservabili dal PC, si verificano con uno screenshot.

## Mappa: area, documenti, strumenti

| Area                                 | Riferimento e runbook                                                    | Strumenti                                                                                     |
| ------------------------------------ | ------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------- |
| Software (LineageOS[^lineage], root) | `01-software/` con `RUNBOOK.md`                                          | `tools/android/xperia-preflight.{ps1,sh}` (sola lettura), `tools/magisk/skeleton/`            |
| Audio                                | `02-audio/` (concetti, cuffie, DAC[^dac]), `spectral-analysis-metodo.md` | `tools/audio/benchmark-calc.py`, `track-benchmark.py` (+ `masters.json`), `spectral-audit.py` |
| Foto/video (app Sony)                | `03-foto-video/` con `RUNBOOK.md`, `_apk-inventory.md`                   | `tools/android/install-apks.{ps1,sh}`                                                         |
| Gaming                               | `04-gaming/` con `RUNBOOK.md`, `citra-config.ini`                        | `tools/magisk/skeleton/`                                                                      |
| Trasversale                          | `_apk-inventory.md`, `_CONVERSION-REPORT.md`                             | `tools/docx-to-md.py`, `tools/annotations.json`                                               |

## Ordine operativo

1. Software come fondazione: LineageOS, sblocco bootloader, backup, TWRP, Magisk. Le altre aree presuppongono un sistema avviato e, per alcune funzioni, il root. Vedi `01-software/RUNBOOK.md`.
2. Installazione app: le APK Sony (fotocamera), UAPP[^uapp] per l'audio e gli store, con `tools/android/install-apks`. Ordine e dipendenze in `_apk-inventory.md`.
3. Uso per area: foto/video con le app Sony, audio con la catena DAC esterno, gaming con gli emulatori. Ciascuna area ha il suo runbook o le sue sezioni.

Prima di ogni passo distruttivo lato telefono si esegue `xperia-preflight`, che verifica in sola lettura slot attivo e stato del bootloader e salva il dump di `getvar all`.

## Stato: pronto e da decidere

E' pronto e versionato: la documentazione di riferimento delle quattro aree, i runbook di software, foto/video e gaming, l'inventario delle APK, gli installer, il preflight, gli strumenti audio (calcolatore benchmark, track-benchmark con database dei master, analizzatore spettrale) con il relativo metodo documentato, e lo scheletro di modulo Magisk.

E' ancora da decidere o non finalizzato, e va trattato con onesta' come tale: la scelta del kit audio (DAC esterno e cuffie) e' segnata TBC[^tbc] e aborted nel materiale sorgente, quindi non esiste ancora un runbook audio della catena di riproduzione; tutte le operazioni fisiche sul telefono sono manuali e non ancora eseguite.

## Rigenerare la documentazione

I file sotto `docs/` sono l'output della conversione del documento sorgente e non vanno modificati a mano: si rigenerano con lo script, che e' idempotente.

```powershell
python tools/docx-to-md.py "(TBC) Sony Xperia 1 III (e setup).docx" --out docs
```

Il generatore applica due livelli curati che sopravvivono alla rigenerazione: le annotazioni (`tools/annotations.json`) iniettano i banner, ad esempio le note LEGACY del percorso GCam, e le redazioni (`tools/redactions.json`, locale) neutralizzano riferimenti non desiderati preservando l'analisi tecnica. Ogni conversione riscrive anche `docs/_CONVERSION-REPORT.md` con conteggi, sezioni marcate dall'autore, mappa immagini e redazioni applicate.

## Dipendenze e riproducibilita'

Gli strumenti Python dipendono da poche librerie, dichiarate in `requirements.txt` alla radice e versionate apposta perche' un clone da GitHub sia riproducibile su un'altra macchina. Dopo il clone si installano cosi'.

```powershell
python -m pip install --user -r requirements.txt
```

Il file elenca `python-docx` (serve solo per rigenerare i docs dal .docx), `numpy` e `soundfile` (analisi audio) e `matplotlib` (opzionale, solo per il PNG dello spettrogramma). Gli strumenti `track-benchmark.py` e `benchmark-calc.py` usano solo la libreria standard e non richiedono nulla.

Alcune dipendenze non sono Python e restano esterne, documentate nei runbook: ADB e fastboot (platform-tools) per la parte software e per l'installazione delle APK; facoltativamente Spek, SoX o FFmpeg per l'ispezione visiva degli spettrogrammi. Non arrivano con il clone e si installano a parte.

## Materiale locale non versionato

Restano fuori dal repository, per licenza o per policy, e vivono solo in locale: il documento sorgente `.docx`, la cartella `_notes/` con le APK e le immagini, il file `album_hires_tracklist.md` e la configurazione di redazione `tools/redactions.json`. Le immagini estratte finiscono in cartelle `assets/` accanto ai documenti e non sono versionate.

## Prossimi passi possibili

Sono aperti tre fili tracciati. Primo, collaudare `track-benchmark.py` e `spectral-audit.py` su tracce reali: e' il controllo end-to-end degli strumenti audio su materiale vero, in attesa che siano disponibili dei file da analizzare. Secondo, scrivere il runbook della catena DAC piu' UAPP una volta scelto il kit audio, oggi ancora TBC nel materiale sorgente. Terzo, avviare i collegamenti col telefono partendo dal preflight software, quando il dispositivo e' disponibile.

Nota di stato: l'allineamento delle dieci righe del benchmark audio al master indicato e' stato completato con `benchmark-calc.py --align`.

[^lineage]: *LineageOS* - distribuzione Android open source basata su AOSP, qui nella versione 22.2 per il pdx215.

[^dac]: *DAC*, Digital to Analog Converter - convertitore che trasforma il segnale audio digitale in analogico; qui un'unita' esterna collegata via USB-C per la massima qualita'.

[^uapp]: *UAPP*, USB Audio Player PRO - app di riproduzione che invia l'audio bit-perfect al DAC esterno bypassando il mixer di Android.

[^tbc]: *TBC*, to be confirmed - marcatore dell'autore per contenuto non ancora verificato o deciso.
