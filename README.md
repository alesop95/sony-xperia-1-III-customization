# Sony Xperia 1 III Customization (pdx215, LineageOS 22.2)

Progetto personale di documentazione e tooling attorno alla personalizzazione di un Sony
Xperia 1 III (nome in codice pdx215) con LineageOS 22.2. Non è una libreria riusabile: è
l'insieme di runbook, note tecniche e piccoli script che accompagnano la preparazione del
telefono, dallo sblocco del bootloader alla catena audio esterna, passando per fotografia e
gaming emulato. La filosofia di lavoro è documentare e preparare tutto prima, e collegare il
telefono dopo, manualmente: nessuno script tocca il dispositivo da solo.

## Struttura

La conoscenza vive sotto `docs/`, generata dal documento sorgente `.docx` tenuto in locale
(fuori dal versionamento) e divisa in quattro aree: `01-software/` (LineageOS, sblocco
bootloader, root con Magisk), `02-audio/` (concetti di base, cuffie, DAC esterno),
`03-foto-video/` (app fotocamera Sony) e `04-gaming/` (emulazione Switch e 3DS). Dove la
procedura è consolidata, ogni area ha anche un `RUNBOOK.md` curato a mano: una sequenza
lineare con gate di sicurezza, che la rigenerazione automatica non sovrascrive. Gli
strumenti vivono sotto `tools/`, come script deterministici e riutilizzabili.

## Funzionalità

Il tooling copre quattro esigenze concrete. Per la parte software, `tools/android/xperia-preflight.ps1`
e `.sh` eseguono un controllo di sola lettura su slot attivo e stato del bootloader prima di
qualunque passo distruttivo, e `tools/magisk/skeleton/` fornisce uno scheletro di modulo
Magisk. Per le app, `tools/android/install-apks.ps1` e `.sh` installano in batch le APK
tramite ADB (Android Debug Bridge), nell'ordine documentato in `docs/_apk-inventory.md`. Per
l'audio, tre script Python (`tools/audio/spectral-audit.py`, `benchmark-calc.py` e
`track-benchmark.py`, quest'ultimo appoggiato a un database di master in `masters.json`)
valutano la qualità di file musicali ad alta risoluzione confrontandoli con i master
sorgente, per verificare il percorso audio del dispositivo verso un DAC (Digital to Analog
Converter) esterno. Infine `tools/docx-to-md.py` converte il documento Word sorgente nella
documentazione Markdown tracciata in `docs/`, applicando due livelli curati che sopravvivono
alla rigenerazione: annotazioni che iniettano banner di nota e redazioni che neutralizzano
riferimenti non desiderati preservando l'analisi tecnica.

## Stato del progetto

Sono pronti e versionati la documentazione di riferimento delle quattro aree, i runbook di
software, foto/video e gaming, l'inventario delle APK, gli installer, il preflight, gli
strumenti audio con il relativo metodo documentato, e lo scheletro di modulo Magisk. Restano
aperti e vanno trattati con onestà come tali: la scelta del kit audio (DAC esterno e cuffie)
è ancora da confermare, quindi non esiste ancora un runbook della catena di riproduzione, e
tutte le operazioni fisiche sul telefono sono manuali e non ancora eseguite. Il valore del
repository sta nelle note accumulate, nelle checklist e nei piccoli script di verifica, non
in un deliverable confezionato.

## Dipendenze

Gli strumenti Python dipendono da poche librerie dichiarate in `requirements.txt`:
`python-docx` (serve solo per rigenerare i docs dal `.docx`), `numpy` e `soundfile` per
l'analisi audio, e `matplotlib`, opzionale, solo per il grafico dello spettrogramma.
`track-benchmark.py` e `benchmark-calc.py` usano solo la libreria standard e non richiedono
nulla. Restano dipendenze esterne, non Python, documentate nei runbook: ADB e fastboot
(platform-tools) per la parte software e per l'installazione delle APK, e facoltativamente
Spek, SoX o FFmpeg per l'ispezione visiva degli spettrogrammi.

```powershell
python -m pip install --user -r requirements.txt
```

## Materiale locale non versionato

Il documento sorgente `.docx`, la cartella `_notes/` con le APK e le immagini di
configurazione, il file `album_hires_tracklist.md` e la configurazione di redazione
restano fuori dal repository per licenza o per policy, e vivono solo in locale.
