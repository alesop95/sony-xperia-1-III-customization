# Fastboot mode (PC + USB cable)

Bisogna collegare un telefono al PC con un cavo USB-C e accedere alla modalità fastboot:

- Spegnere il telefono
- Premere e tenere premuto Volume Su
- Mentre uno tiene premuto si può collegare il cavo USB-C al PC
- Vedrai la luce blu → sei in fastboot mode (si possono lanciare i comandi dal PC)

Then, to reboot a phone into fastboot mode, from terminal run:

adb reboot bootloader

Once in bootloader mode, you can use fastboot commands such as:

fastboot devices

aaaaaa

## LineageOS and phone slots

Il telefono ha due slot di sistema, chiamati “Slot A” (attivo, quello da cui sta usando Android) e “Slot B” passivo, usato per aggiornamenti e modifiche”. Google ha introdotto l’A/B partitioning per aggiornamenti senza rischi: android installa il successivo aggiornamento sullo slot passivo e poi quando uno normalmente riavvia switcha su quello ed è quello che succede in maniera trasparente all’utente medio. Gli slot A/B occupano effettivamente spazio fisico duplicato sul dispositivo e ogni slot ha copie delle partizioni critiche ma non viene duplicato tutto il sistema (ad esempio, i dati utente /data, o la memoria interna con foto/app), ma solo il minimo indispensabile per poter avviare un sistema). Una parte significativa della memoria interna viene "riservata" al sistema A/B. Sui dispositivi con 128GB, parliamo di circa 3-4GB occupati in più per avere queste doppie partizioni.

I dispositivi con schema di partizionamento **A/B** dispongono di due partizioni di sistema. Solo una è attiva per volta; l'altra viene utilizzata per aggiornamenti o come fallback in caso di errore. Durante il flashing manuale di una nuova ROM, è fondamentale flashare **entrambe le partizioni**, operazione possibile via fastboot o durante la fase di installazione:

fastboot --set-active=a

\# oppure

fastboot --set-active=b

Questa procedura si rivelerà necessaria durante l'aggiornamento a una nuova versione maggiore di Android. LineageOS utilizza un sistema **A/B** e supporta due modalità di aggiornamento:

- Minor (security patch, bugfix) – con updater interno (OTA)
- Major (es. versioni Android) – con Sideload via recovery	Lineage Recovery o TWRP

Per ogni versione Major è necessario:

1. Scaricare la nuova build .zip
1. Riavviare in Lineage Recovery
- adb reboot recovery
1. Abilitare la modalità ADB sideload dal menu
1. Eseguire
- adb sideload lineage-xx.zip

Dunque, cosa significa avere LineageOS installato eventualmente su entrambi gli slot? Significa che le partizioni system_a e system_b (e boot_a / boot_b) **contengono la stessa ROM funzionante**. Di solito questo succede:

**automaticamente** se ricevi **aggiornamenti OTA**

**manualmente** se le hai flashate tu su entrambi

Per verificare quale slot è attivo e cosa c’è nei due (prima di fare danni) se non si può fare da da recovery TWRP se non è stata ancora installata, da **ADB/fastboot (da PC). Dunque** 

Col telefono in **fastboot mode**, digita da terminale:

fastboot --getvar current-slot

dirà “a” o “b” e poi con:

	fastboot getvar all 

si possono vedere TUTTI i dettagli, anche cosa contiene boot_a, system_a, ecc.

Se hai installato **LineageOS tramite un pacchetto .zip da recovery**, e **non hai ricevuto aggiornamenti OTA**, allora molto probabilmente **hai solo uno slot "pieno"** (A o B).

Gli aggiornamenti **OTA ufficiali** usano lo schema A/B:

Scrivono sullo slot passivo

Poi switchano

Così se qualcosa va male, torni indietro

Se hai installato Lineage solo manualmente allora soltanto uno solo dei due **slot avrà la ROM.**

### Check for a working ROM in a slot

Se switchi su slot B (passivo), il sistema da cui parti deve essere installato anche su slot B per avviarsi correttamente. Se su slot B non c’è nulla o è “vuoto”, il telefono NON partirà correttamente.

Non è un problema perché entrambi gli slot hanno tutto per avviare android (una partizione boot, una partizione system, una recovery). Quando si attiva lo slot B, quel sistema diventa semplicemente il principale senza essere un “backup” o una zona limitata è come avere due sistemi gemelli da cui scegliere. Qui si vuole sfruttare questa tecnologia per fare modifiche in sicurezza (come flashare TWRP o Magisk).

Ma come faccio a sapere cosa c’è su slot B prima di switchare? Su android in modalità normale si può aprire un terminale ADB con un telefono collegato al PC e digitare:

	adb shell getprop ro.boot.slot_suffix

E risponde con _a o _b a seconda dello slot *attivo* in quel momento. Per verificare invece il contenuto dello slot passivo (per forza l’altro slot), e quindi per sapere se c’è una ROM funzionante nello slot passivo (quello non attivo), bisogna fare fare un controllo da fastboot. Mettendo quindi il telegono in modalità fastboot (si è visto: spento + volume Su + collegamento USB) da PC bisogna digitare:

	fastboot getvar all

e cercare una riga come “current-slot: a”. E poi verificare lo slot “other” per forza mettendolo prima come attivo:

	fastboot --set-active=other

E poi riavviando:

	fastboot reboot

Perché se il telefono si avvia normalmente c’è LineageOS (o un sistema) su slot B. Se invece il telefono resta in bootloop o va in recovery, allora slot B è “vuoto” o non funzionante.

### Backup del boot dello slot attivo via fastboot

Prima di flashare TWRP o qualsiasi cosa, puoi fare un backup del boot *dello slot attivo* via fastboot:

	fastboot boot boot.img

O, se supportato dal dispositivo (meglio) fare:

	fastboot dump boot boot_backup.img

Se non funziona neanche questo si può estrarre il boot.img dalla ROM di LineageOS scaricata dal sito ufficiale.

fastboot getvar current-slot 

\# Supponiamo sia "a" 

fastboot flash boot boot_a.img 

fastboot flash vbmeta vbmeta_a.img 

fastboot flash dtbo dtbo_a.img 

Quello che voglio backuppare è il boot. 

Quindi fammi capire, 

		partire da qui

Se LineageOS è attivo solo su uno slot (es. a), allora:

Quando vuoi **tornare al boot perfettamente funzionante**, ti servono almeno queste 3 partizioni

- Boot: contiene il kernel e l’initramfs (cioè il cuore dell’OS)
- vbmeta: firma di sicurezza per il verified boot
- dtbo	contiene il device tree overlay (serve per compatibilità hardware)

sono le partizioni dello slot attivo assumendo che LineageOS è attivo solo su uno slot e io ho il culo parato quindi sempre ripristinare l’avvio di LineageOS perfettamente

## Check for bootloader (unlock)

Una volta che sono state abilitate le opzioni da sviluppatore (e il blocco OEM) bisogna anche ottenere il codice di sblocco da Sony andando su Sony Unlock Bootloader [https://developer.sony.com/open-source/aosp-on-xperia-open-devices/get-started/unlock-bootloader](https://developer.sony.com/open-source/aosp-on-xperia-open-devices/get-started/unlock-bootloader) e inserendo l’IMEI del telefono per ottenere il codice di sblocco via mail.

Dopo aver installato ADB e fastboot sul PC, si può collegare il telefono in modalità fastboot e sbloccare il bootloader. Aprendo il terminale digitare:

	fastboot oem unlock 0xCODICE

dove CODICE è proprio quello ottenuto da Sony. Riavviando il telefono con:

	fastboot reboot

Il bootloader è sbloccato. Per essere sicuri si può cercare dentro Opzioni sviluppatore ma se non si vede la voce Sblocco OEM, è probabile che:

Il bootloader sia già sbloccato (in questo caso la voce sparisce o è disabilitata).

Oppure il sistema (LineageOS) ha rimosso o nascosto questa voce.

Per sicurezza si può anche collega il telefono al PC con ADB e Fastboot installati e lanciare il comando da terminale:

	adb reboot bootloader

e:

	fastboot getvar unlocked

e se risponde con unlocked: yes, significa che è sbloccato. Inoltre, sempre sul PC si può sempre usare questo comando:

fastboot oem device-info

se si vede qualcosa come:

(bootloader) Device unlocked: true

Allora il bootloader è sbloccato. Anche dopo aver fatto un factory reset (per cui è necessario nuovamente abilitare le opzioni da sviluppatore) si può andare su Power menu > Advanced restart (“When unlocked, include options in the power menu for restarting into recovery or bootloader”) cosa che adesso è stata riattivata anche
