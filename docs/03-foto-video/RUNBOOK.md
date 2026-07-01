# Runbook foto/video - app proprietarie Sony

> Percorso operativo primario per foto e video sull'Xperia 1 III. Si basa sulle applicazioni
> proprietarie Sony estratte dalla ROM ufficiale, presenti come APK in `_notes/apks`, perche'
> sono le uniche ad accedere pienamente all'ISP[^isp] e al tuning hardware del sensore. Il
> percorso GCam, documentato nelle sezioni numerate di questa cartella, e' marcato legacy e
> conservato solo come riferimento storico. Riferimento concettuale: `04-tbc-app-proprietarie-sony.md`.

## Perche' le app Sony e non GCam o Open Camera

Open Camera e GCam si appoggiano alla sola Camera2 API[^cam2]: usano i tre sensori e salvano in
RAW[^raw], ma non accedono al tuning Sony, al postprocessing proprietario, ne' a funzioni come Eye
AF[^af], il crop 70mm pulito o i profili CineAlta. Per la massima qualita', soprattutto in
condizioni difficili, si usano le app Sony. Il dettaglio del confronto e' nella sezione
`04-tbc-app-proprietarie-sony.md`.

## Insieme delle app e dipendenze

Le app fotografiche Sony dipendono da due pacchetti condivisi che vanno installati prima: la
libreria comune delle fotocamere e il pacchetto dei permessi. L'inventario completo, con package e
versioni, e' in `../_apk-inventory.md`.

| App | File APK | Ruolo |
|---|---|---|
| Camera common | `Camera_common_3.2.apk` | Libreria comune (dipendenza). |
| Camera common permission | `com.sonymobile.cameracommon.permission_1.5.A.0.0.apk` | Permessi condivisi (dipendenza). |
| Photography Pro | `Photography_Pro_1.3.2.A.1.0.apk` | Foto professionali: manuale, RAW, tuning Sony. |
| Cinema Pro | `Cinema_Pro_1.7.1.A.0.10.apk` | Video professionali (profili CineAlta). |
| External Monitor | `com.sonymobile.extmonitorapp_7.0.A.0.8-14680072.apk` | Telefono come monitor/registratore via USB-C verso HDMI. |

## Prerequisiti

Serve LineageOS gia' avviato sul telefono, il debug USB attivo (Fase 1 del runbook software) e ADB
sul PC. Le APK sono in `_notes/apks`. Lo sblocco del bootloader o il root non sono necessari per
queste app, salvo l'eventuale variante mod indicata sotto.

## Fase 1 - Installare dipendenze e app (PC)

Il modo piu' rapido e' lo script dedicato, che installa l'insieme attivo nell'ordine corretto e
prosegue anche se una singola APK fallisce.

```powershell
pwsh -File tools/android/install-apks.ps1
```

In alternativa, installazione manuale nell'ordine di dipendenza.

```powershell
adb install -r "_notes/apks/com.sonymobile.cameracommon.permission_1.5.A.0.0.apk"
adb install -r "_notes/apks/Camera_common_3.2.apk"
adb install -r "_notes/apks/Photography_Pro_1.3.2.A.1.0.apk"
adb install -r "_notes/apks/Cinema_Pro_1.7.1.A.0.10.apk"
adb install -r "_notes/apks/com.sonymobile.extmonitorapp_7.0.A.0.8-14680072.apk"
```

## Fase 2 - Problema noto della permission camera (PC)

Il documento sorgente registra che tutto si installava correttamente tranne
`com.sonymobile.cameracommon.permission`. Se l'installazione di quel pacchetto fallisce, si procede
comunque con le altre app e si verifica se Photography Pro e Cinema Pro funzionano lo stesso: spesso
il permesso e' gia' concesso dal sistema o non bloccante. Questo punto resta da verificare sul
dispositivo reale; l'esito va annotato.

Gate: Photography Pro e Cinema Pro si avviano e accedono ai tre moduli ottici.

## Fase 3 - Variante mod no-root di Photo Pro (opzionale)

Se la build estratta dalla ROM non si avvia correttamente su LineageOS, il documento indica una
versione modificata e funzionante senza root di Photo Pro, con la lente 70mm attiva, reperibile su
xdaforums (PhotoPro 1.6.A.0.27 mod no-root). E' un'alternativa, non il percorso predefinito: si usa
solo se l'APK ufficiale da' problemi.

## Fase 4 - Uso professionale (manuale)

Photography Pro offre il controllo manuale completo, ISO, tempo di scatto e fuoco, lo scatto RAW e
il tuning Sony dei tre sensori. Cinema Pro registra video con i profili professionali CineAlta.
External Monitor trasforma il telefono in monitor o registratore esterno collegandolo via USB-C a
una sorgente HDMI[^hdmi] tramite una scheda di acquisizione, utile come monitor di campo o per
registrare un segnale esterno.

Per i riscontri visivi su queste app conviene catturare uno screenshot della schermata pertinente,
dato che l'aspetto e il comportamento a runtime non sono osservabili dal PC.

## Materiale legacy

Le sezioni `01-verificare-che-camers2-api...`, `02-trovare-un-file-xml-di-configurazione-per-gcam...`
e `03-tbc-troubleshooting/` riguardano il percorso GCam abbandonato e sono marcate LEGACY. La APK
`MGC_8.1.101_A9_GV1zfix_MGC.apk` e i preset `_notes/settings/xperia1iii_bsg_8.1.101_*.xml` valgono
solo per quel percorso e non vengono installati dallo script.

[^isp]: *ISP*, Image Signal Processor - blocco hardware che elabora il segnale grezzo del sensore;
le app Sony vi accedono direttamente, le app basate solo su Camera2 no.

[^cam2]: *Camera2 API* - interfaccia Android standard per la fotocamera; da' accesso a sensori e RAW
ma non al tuning proprietario del produttore.

[^raw]: *RAW* - formato che conserva i dati grezzi del sensore senza compressione con perdita,
massima latitudine in post-produzione.

[^af]: *AF*, Auto Focus - messa a fuoco automatica; *Eye AF* la specializza sul riconoscimento
dell'occhio del soggetto.

[^hdmi]: *HDMI*, High-Definition Multimedia Interface - standard per il trasporto di audio e video
digitali; qui acquisito sul telefono tramite adattatore USB-C e scheda di acquisizione.
