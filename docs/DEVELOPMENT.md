# Guida allo sviluppo del progetto

> Indice operativo del progetto di personalizzazione del Sony Xperia 1 III (pdx215) con
> LineageOS 22.2. Spiega come e' organizzato, come si usa, in che ordine si opera e cosa e'
> pronto rispetto a cosa e' ancora da decidere. E' il punto di partenza per orientarsi; i
> dettagli vivono nei documenti di area e nei runbook.

## Impianto

Il progetto ha due meta'. La conoscenza vive in `docs/`, generata fedelmente dal documento
sorgente di 201 pagine e divisa in quattro aree: software, audio, foto/video e gaming. Gli
strumenti vivono in `tools/`, come script deterministici e riutilizzabili. La filosofia di lavoro
e' preparare e documentare tutto prima, e collegare il telefono dopo, manualmente: nessuno script
tocca il dispositivo da solo.

Ogni area ha le sue sezioni di riferimento generate dal sorgente, e dove la procedura e'
consolidata anche un `RUNBOOK.md` curato a mano: una sequenza lineare ed eseguibile con gate di
sicurezza, che il generatore non sovrascrive.

## Come si usa

Si parte da `docs/README.md` per orientarsi tra le quattro aree. Per lavorare su un'area si apre
il suo `RUNBOOK.md`, che rimanda alle sezioni di riferimento quando serve approfondire. Quando la
procedura arriva ai passi fisici sul telefono, si eseguono gli strumenti in `tools/`: prima il
preflight di sola lettura, poi l'installazione delle app. I punti visivi sul telefono, che non
sono osservabili dal PC, si verificano con uno screenshot.

## Mappa: area, documenti, strumenti

| Area | Riferimento e runbook | Strumenti |
|---|---|---|
| Software (LineageOS[^lineage], root) | `01-software/` con `RUNBOOK.md` | `tools/android/xperia-preflight.{ps1,sh}` (sola lettura), `tools/magisk/skeleton/` |
| Audio | `02-audio/` (concetti, cuffie, DAC[^dac]) | `tools/audio/benchmark-calc.py` |
| Foto/video (app Sony) | `03-foto-video/` con `RUNBOOK.md`, `_apk-inventory.md` | `tools/android/install-apks.{ps1,sh}` |
| Gaming | `04-gaming/` con `RUNBOOK.md`, `citra-config.ini` | `tools/magisk/skeleton/` |
| Trasversale | `_apk-inventory.md`, `_CONVERSION-REPORT.md` | `tools/docx-to-md.py`, `tools/annotations.json` |

## Ordine operativo

1. Software come fondazione: LineageOS, sblocco bootloader, backup, TWRP, Magisk. Le altre aree
   presuppongono un sistema avviato e, per alcune funzioni, il root. Vedi `01-software/RUNBOOK.md`.
2. Installazione app: le APK Sony (fotocamera), UAPP[^uapp] per l'audio e gli store, con
   `tools/android/install-apks`. Ordine e dipendenze in `_apk-inventory.md`.
3. Uso per area: foto/video con le app Sony, audio con la catena DAC esterno, gaming con gli
   emulatori. Ciascuna area ha il suo runbook o le sue sezioni.

Prima di ogni passo distruttivo lato telefono si esegue `xperia-preflight`, che verifica in sola
lettura slot attivo e stato del bootloader e salva il dump di `getvar all`.

## Stato: pronto e da decidere

E' pronto e versionato: la documentazione di riferimento delle quattro aree, i runbook di
software, foto/video e gaming, l'inventario delle APK, gli installer, il preflight, il calcolatore
audio, lo scheletro di modulo Magisk.

E' ancora da decidere o non finalizzato, e va trattato con onesta' come tale: la scelta del kit
audio (DAC esterno e cuffie) e' segnata TBC[^tbc] e aborted nel materiale sorgente, quindi non
esiste ancora un runbook audio della catena di riproduzione; il calcolatore benchmark ha segnalato
dieci righe in cui il master indicato nel testo non coincide con le colonne bit/sample, in attesa
di un criterio di allineamento; tutte le operazioni fisiche sul telefono sono manuali e non ancora
eseguite.

## Rigenerare la documentazione

I file sotto `docs/` sono l'output della conversione del documento sorgente e non vanno modificati
a mano: si rigenerano con lo script, che e' idempotente.

```powershell
python tools/docx-to-md.py "(TBC) Sony Xperia 1 III (e setup).docx" --out docs
```

Il generatore applica due livelli curati che sopravvivono alla rigenerazione: le annotazioni
(`tools/annotations.json`) iniettano i banner, ad esempio le note LEGACY del percorso GCam, e le
redazioni (`tools/redactions.json`, locale) neutralizzano riferimenti non desiderati preservando
l'analisi tecnica. Ogni conversione riscrive anche `docs/_CONVERSION-REPORT.md` con conteggi,
sezioni marcate dall'autore, mappa immagini e redazioni applicate.

## Materiale locale non versionato

Restano fuori dal repository, per licenza o per policy, e vivono solo in locale: il documento
sorgente `.docx`, la cartella `_notes/` con le APK e le immagini, il file `album_hires_tracklist.md`
e la configurazione di redazione `tools/redactions.json`. Le immagini estratte finiscono in
cartelle `assets/` accanto ai documenti e non sono versionate.

## Prossimi passi possibili

Chiudere la fase di preparazione fissando il criterio per le dieci incongruenze del benchmark
audio; quando il kit audio sara' scelto, scrivere il runbook della catena DAC piu' UAPP; infine,
quando il telefono e' disponibile, avviare i collegamenti partendo dal preflight software.

[^lineage]: *LineageOS* - distribuzione Android open source basata su AOSP, qui nella versione
22.2 per il pdx215.

[^dac]: *DAC*, Digital to Analog Converter - convertitore che trasforma il segnale audio digitale
in analogico; qui un'unita' esterna collegata via USB-C per la massima qualita'.

[^uapp]: *UAPP*, USB Audio Player PRO - app di riproduzione che invia l'audio bit-perfect al DAC
esterno bypassando il mixer di Android.

[^tbc]: *TBC*, to be confirmed - marcatore dell'autore per contenuto non ancora verificato o
deciso.
