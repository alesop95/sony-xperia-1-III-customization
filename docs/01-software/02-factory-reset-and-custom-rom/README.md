# Factory reset and custom ROM

Se anche si fa un factory reset del telefono dalle opzioni base di un menu Android, l’installazione di una ROM customizzata rimane effettivamente lì. Difatti, un factory reset non cancella il sistema operativo installato sul telefono.

Inoltre, sebbene a seguito di un factory reset, alcune applicazioni, comprese quelle di sistema, potrebbero non essere più disponibili. Tuttavia, la recovery personalizzata Lineage Recovery rimane installata, accessibile tramite combinazione di tasti fisici o da terminale con il comando:

	adb reboot recovery

Questo se è stato intallato ADB e fastboot su un sistema operativo per accedere a queste funzionalità per il telefono.

Un factory reset di fatto fa “soltanto” queste cose:

- cancella TUTTI i dati utente:
- app installate
- account Google o altri account
- foto, video, documenti salvati nella memoria interna (se scegli di cancellare tutto)
- impostazioni di sistema personalizzate

Ma NON tocca il sistema operativo (la ROM installata). Dunque, se si installa LineageOS sopra il sistema operativo originale, dopo l’installazione, LineageOS sostituisce completamente il sistema originale Sony. Quando si fa fai un factory reset, il telefono ripulisce solo i tuoi **dati personali**, ma rimane comunque LineageOS installato. In pratica:

| **Factory reset cancella** | **Factory reset NON cancella** |
| --- | --- |
| App utente | Il sistema operativo installato |
| Account (Google, ecc.) | Recovery modificata (es. TWRP) |
| Impostazioni personalizzate | Bootloader sbloccato |
| File utente (se selezionato) | ROM LineageOS |

Per tornare alla ROM originale servirebbe scaricare il firmware ufficiale Sony, flashare il firmware via tool (es. Xperia Flash Tool, Newflasher) ed eventualmente ribloccare il bootloader (opzionale, ma utile per sicurezza o app bancarie). Questa procedura **non si fa con un semplice factory reset**, è una procedura più complessa.

Dopo il factory reset comunque sono stati ri-attivate (è necessario rifarlo) le “Developer options”.

## Contenuti

- [Enable developer options, OEM, USB debugging](01-enable-developer-options-oem-usb-debugging.md)
- [The sideload](02-the-sideload.md)
