# USB OTG verification in LineageOS

Per verificare che USB OTG sia attivo in LineageOS, bisogna controllare due aspetti fondamentali:

- Verifica sul sito del produttore o nella scheda tecnica del dispositivo se supporta USB OTG.
- Se LineageOS è stato compilato per quel dispositivo con un kernel che supporta l'host USB, allora OTG è generalmente attivo per impostazione predefinita.

LineageOS **non include di default** un interruttore esplicito per USB OTG, ma su alcune versioni o build personalizzate potresti trovare l'opzione qui:

- Impostazioni > Archiviazione (o "Archiviazione e USB")
- Collega un dispositivo USB (es. una chiavetta OTG): se l'OTG è attivo e supportato, il dispositivo verrà montato automaticamente come unità esterna

Sempre da ADB (o shell root) si può fare:

	ls /dev/block/sd*

Oppure:

	dmesg | grep -i usb

Se OTG è attivo e funziona, si vederanno righe tipo “[xxxxx] usb 1-1: new high-speed USB device number ...”.

In alcune versioni recenti di LineageOS la verifica è anche attiva dentro le opzioni sviluppatore. Non esiste un vero e proprio "interruttore" OTG in LineageOS standard. Se:

- Il kernel lo supporta
- Il dispositivo lo supporta
- Il dispositivo viene rilevato collegandolo

Allora USB OTG è attivo. In caso contrario, il problema è a livello di kernel, hardware, o alimentazione insufficiente.

Il Sony Xperia 1 III (modello pdx215) in particolare supporta ufficialmente USB OTG. I dati che lo confermano sono:

- Porta USB-C 3.1 Gen 1 (supporta USB Host Mode)
- Sony ha incluso supporto OTG nella ROM stock
- Il SoC Snapdragon 888 ha supporto OTG via USB Host nativo

E il supporto hardware è presente attivo. Inoltre, per la build specifica Build number lineage_pdx215-userdebug 15 BP1A.250505.0053439504aa9 che spiega esserci Android 15 con LineageOS versione 22.2-20250701-NIGHTLY-pdx215, lo stato attuale del supporto OTG nella LineageOS ufficiale per Xperia 1 III è che Il kernel usato nel port ufficiale di LineageOS per Xperia 1 III include:

- CONFIG_USB_OTG=y
- CONFIG_USB_OTG_FSM=y
- Supporto per usb-host attivo

Dunque, il kernel LineageOS ufficiale per questo dispositivo include il supporto OTG. Si possono anche semplicemente usare app come USB OTG Checker (di JWork - nome pacchetto consigliato “com.faitaujapon”) o USB Host Diagnostics (di Chainfire). Queste verificano la presenza del supporto OTG a livello kernel e API.

Controllando con USB OTG Checker si accede ad una schermata in cui dice “ANDROID COMPATIBLE USB OTG”.
