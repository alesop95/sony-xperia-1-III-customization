# (TBC) App proprietarie Sony

> Percorso primario per foto/video. Le APK Sony sono in `_notes/apks`; per installazione e uso ordinati vedi `../RUNBOOK.md`.

Open Camera si basa solo su Camera API 2, quindi può usare i 3 sensori e salvare in RAW, ma non ha accesso al tuning Sony, al postprocessing proprietario e alle funzioni avanzate come Eye AF o 70mm crop clean. Se si vuole la massima qualità fotografica su Xperia (soprattutto in condizioni difficili), usare le app Sony. Se si desidera un’app open-source funzionale con accesso RAW e multiscatto, Open Camera va bene ma è limitata dal punto di vista qualitativo.

| **Caratteristica** | **Open Camera (API 2)** | **App Sony Proprietarie** |
| --- | --- | --- |
| RAW | Sì | Sì |
| Controllo manuale (ISO, shutter, focus) | Sì | Sì |
| Accesso diretto a ISP e tuning hardware | ❌ | ✅ |
| Qualità low-light, HDR, Bokeh, Eye AF, Zeiss tuning | ❌ | ✅ |
| Supporto multiframe & algoritmi Sony | ❌ | ✅ |
| UI e profili professionali (CineAlta) | ❌ | ✅ |

Per ottenere il massimo dall’hardware fotografico dell’Xperia, è consigliato l’utilizzo delle applicazioni fotografiche proprietarie Sony, estratte direttamente dalla ROM ufficiale. Le principali sono:

Cinema Pro (registrazione video professionale)

Camera Pro (modalità manuale e RAW)

Monitor (per l’utilizzo del telefono come monitor HDMI tramite adattatore USB-C → HDMI con scheda di acquisizione)

Queste app si basano su librerie proprietarie che consentono l’accesso pieno alle funzionalità del sensore Sony, comprese le ottimizzazioni per autofocus, scatti in condizioni di bassa luminosità e supporto RAW. Una versione modificata e funzionante senza root dell’app **Photo Pro** è disponibile a questo indirizzo: [https://xdaforums.com/t/mod-no-root-photopro-1-6-a-0-27-with-70mm-lens-working.4644947/](https://xdaforums.com/t/mod-no-root-photopro-1-6-a-0-27-with-70mm-lens-working.4644947/). È la cosa più importante. App alternative come **Open Camera** (es. versione 1.54.1) supportano l’API Camera2 e l’accesso ai tre moduli ottici, ma non garantiscono le stesse prestazioni in termini di qualità d’immagine.

![](assets/img-0039.png)  ![](assets/img-0040.png)  ![](assets/img-0041.png)

Everything worked fine except for com.sonymobile.cameracommon.permission_1.5.A.0.0.
