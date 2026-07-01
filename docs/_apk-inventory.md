# Inventario APK e asset di sviluppo

> Mappa di tutto il materiale binario in `_notes/` (cartella ignorata da git): a cosa serve
> ogni APK, a quale area appartiene, in che ordine si installa e cosa e' legacy. I package name
> sono estratti dai manifest delle APK; dove l'estrazione non e' univoca sono marcati da
> confermare. L'installazione usa comunque il file APK, non il package, quindi questi valori
> servono solo per verifica e disinstallazione. Lo script `tools/android/install-apks.ps1`
> (oppure `.sh`) installa l'insieme attivo nell'ordine corretto.

## Applicazioni attive

| File in `_notes/apks` | Pacchetto | Versione | Area | Ruolo | Ordine install |
|---|---|---|---|---|---|
| `com.sonymobile.cameracommon.permission_1.5.A.0.0.apk` | `com.sonymobile.cameracommon.permission` | 1.5.A.0.0 | foto/video | Permessi condivisi delle fotocamere Sony; dipendenza delle app Sony. Nota: in passato ha dato problemi di installazione (vedi runbook). | 1 |
| `Camera_common_3.2.apk` | `com.sonymobile.cameracommon` | 3.2 | foto/video | Libreria comune delle fotocamere Sony; dipendenza di Photography Pro e Cinema Pro. | 2 |
| `Photography_Pro_1.3.2.A.1.0.apk` | da confermare (Photo Pro Sony) | 1.3.2.A.1.0 | foto/video | Fotografia professionale: modalita' manuale, ISO/shutter/focus, RAW, tuning ISP Sony. App primaria per le foto. | 3 |
| `Cinema_Pro_1.7.1.A.0.10.apk` | da confermare (Cinema Pro Sony) | 1.7.1.A.0.10 | foto/video | Video professionale (profili CineAlta). App primaria per i video. | 4 |
| `com.sonymobile.extmonitorapp_7.0.A.0.8-14680072.apk` | `com.sonymobile.extmonitorapp` | 7.0.A.0.8 | foto/video | External Monitor: usa il telefono come monitor/registratore via USB-C verso HDMI con scheda di acquisizione. | 5 |
| `com.extreamsd.usbaudioplayerpro--7016.apk` | `com.extreamsd.usbaudioplayerpro` | build 7016 | audio | USB Audio Player PRO (UAPP): playback bit-perfect verso DAC esterno, bypassa il mixer Android. App chiave del setup audio. | 6 |
| `APKPure_v3.20.51_apkpure.com.apk` | `com.apkpure.aegon` | 3.20.51 | utility/store | Store alternativo per scaricare app sul dispositivo. | 7 |
| `com.huawei.appmarket.2311221502.apk` | `com.huawei.appmarket` | 2311221502 | utility/store | Huawei AppGallery: store alternativo. | 8 |

## Materiale legacy (non installato dal percorso primario)

| File | Area | Stato | Nota |
|---|---|---|---|
| `_notes/apks/MGC_8.1.101_A9_GV1zfix_MGC.apk` | foto/video | LEGACY | Modded Google Camera (GCam). Sostituita dalle app Sony. |
| `_notes/settings/xperia1iii_bsg_8.1.101_*.xml` (3 file) | foto/video | LEGACY | Preset di configurazione per la GCam (BSG). Validi solo con MGC. |

## Asset non APK

| File | Tipo | Uso |
|---|---|---|
| `_notes/apks/config.ini` | config Citra | Appartiene al gaming (emulatore 3DS Citra MMJ), non a foto/video: collocato per errore nella cartella apks. Vedi area gaming. |
| `_notes/digital image resources/digital image fundamentals.pdf` | riferimento | Teoria di elaborazione dell'immagine digitale (riferimento, non operativo). |
| `_notes/digital image resources/Digital image processing.txt` | riferimento | Link alla risorsa video sulla scienza della fotografia. |

## Installazione

Le APK si installano da PC con il telefono collegato e il debug USB attivo, tramite ADB. Lo script
dedicato gestisce l'ordine e prosegue anche se una singola installazione fallisce.

```powershell
pwsh -File tools/android/install-apks.ps1
```

In alternativa, una singola APK si installa con il comando seguente, dove `-r` reinstalla mantenendo
i dati se l'app e' gia' presente.

```powershell
adb install -r "_notes/apks/Photography_Pro_1.3.2.A.1.0.apk"
```

Il dettaglio di sequenza, dipendenze e problemi noti per le app fotografiche e' nel runbook
`03-foto-video/RUNBOOK.md`.
