# Runbook software - Xperia 1 III (pdx215) con LineageOS 22.2

> Procedura operativa ordinata per la parte software. Linearizza in una sequenza eseguibile
> i contenuti delle sezioni di questa cartella, che nel documento sorgente sono sparsi e non
> sequenziali. Ogni fase rimanda alla sezione di riferimento. I comandi sono ripresi
> verbatim dalle sezioni; dove il documento sorgente propone un comando non standard o non
> verificato, qui e' marcato come da verificare invece di essere presentato come certo.

## Come leggere questo runbook

Le operazioni si dividono in due categorie. Quelle marcate manuale avvengono fisicamente sul
telefono o richiedono un'azione umana che l'agente non puo' osservare, e in quei punti conviene
catturare uno screenshot di conferma. Quelle marcate PC sono comandi da terminale sul computer,
con il telefono collegato via cavo USB-C.

Prima di ogni fase potenzialmente distruttiva c'e' un gate, cioe' una condizione da verificare
che deve risultare vera per poter proseguire in sicurezza. Lo strumento `tools/android/xperia-preflight.ps1`
(oppure `.sh` su Linux) esegue le sole verifiche di sola lettura e stampa lo stato dei gate, senza
toccare nulla sul dispositivo.

Il principio di sicurezza di fondo, ripreso dalla sezione sugli slot, e' che il dispositivo ha due
slot di sistema A/B[^ab]: si lascia intatto lo slot attivo con LineageOS funzionante, si flasha la
recovery personalizzata sullo slot passivo, e prima di qualsiasi flash si salva un backup minimo
delle partizioni di avvio. Cosi' un avvio rotto si recupera sempre tornando allo slot buono.

## Fase 0 - Prerequisiti sul PC (PC)

Servono ADB[^adb] e fastboot installati e un cavo USB-C dati. Su Windows i binari stanno nella
cartella platform-tools. Verifica che siano raggiungibili dal terminale.

```powershell
adb version
fastboot --version
```

Riferimento: `03-install-adb-and-fastboot-for-a-sony-xperia-1-iii/README.md`.

## Fase 1 - Opzioni sviluppatore, sblocco OEM, debug USB (manuale)

Sul telefono, in Impostazioni, sezione Sistema, premere sette volte su Build number per sbloccare
le opzioni sviluppatore. Dentro le opzioni sviluppatore attivare lo sblocco OEM[^oem] e il debug
USB. Conviene catturare uno screenshot della schermata con lo sblocco OEM attivo.

Riferimento: `02-factory-reset-and-custom-rom/01-enable-developer-options-oem-usb-debugging.md`.

## Fase 2 - Entrare in fastboot e verificare la connessione (PC)

Con il telefono acceso e il debug USB attivo si entra in bootloader da terminale; in alternativa
si spegne il telefono, si tiene premuto Volume Su e si collega il cavo USB-C fino alla luce blu.

```powershell
adb reboot bootloader
fastboot devices
```

A questo punto lanciare il preflight per fotografare lo stato del dispositivo.

```powershell
pwsh -File tools/android/xperia-preflight.ps1
```

Riferimento: `03-install-adb-and-fastboot-for-a-sony-xperia-1-iii/01-fastboot-mode-pc-usb-cable.md`.

## Fase 3 - Sblocco del bootloader (PC + manuale)

Lo sblocco richiede il codice ufficiale Sony, che si ottiene inserendo l'IMEI[^imei] del telefono
nella pagina Sony Unlock Bootloader e ricevendolo via email. Con il telefono in fastboot si applica
il codice e si riavvia.

```powershell
fastboot oem unlock 0xCODICE
fastboot reboot
```

Gate: il bootloader deve risultare sbloccato. Si verifica con i comandi seguenti, in fastboot.

```powershell
fastboot getvar unlocked
fastboot oem device-info
```

La condizione e' soddisfatta se `unlocked` risponde `yes` oppure se `device-info` mostra
`Device unlocked: true`. Lo stesso esito e' riportato dal preflight.

Riferimento: `03-install-adb-and-fastboot-for-a-sony-xperia-1-iii/01-fastboot-mode-pc-usb-cable.md`,
sezione Check for bootloader (unlock).

## Fase 4 - Mappare gli slot e salvare lo stato (PC)

Prima di toccare le partizioni si registra quale slot e' attivo e si salva il dump completo di
`getvar all`, utile come riferimento per sapere cosa contengono `boot_a`, `system_a` e cosi' via.

```powershell
fastboot getvar current-slot
fastboot getvar all
```

In Android normale, con telefono collegato, lo slot attivo si legge anche cosi'.

```powershell
adb shell getprop ro.boot.slot_suffix
```

Il preflight salva automaticamente il dump di `getvar all` in un file di log datato sotto
`_notes/android-logs/` (cartella ignorata da git), cosi' resta una fotografia consultabile.

Riferimento: `03-install-adb-and-fastboot-for-a-sony-xperia-1-iii/01-fastboot-mode-pc-usb-cable.md`,
sezione LineageOS and phone slots.

## Fase 5 - Backup minimo vitale delle partizioni di avvio (PC)

Prima di flashare qualsiasi cosa servono almeno tre partizioni dello slot attivo, sufficienti a
ripristinare l'avvio: boot, che contiene kernel e initramfs; vbmeta, la firma del verified boot;
dtbo, il device tree overlay per la compatibilita' hardware.

Nota di verifica: il documento sorgente propone `fastboot dump boot boot_backup.img` come metodo di
estrazione, ma fastboot non espone in modo affidabile la lettura delle partizioni e questo comando
non e' standard. Il metodo affidabile, da preferire, e' procurarsi i file gia' pronti per la build
in uso (`22.2-20250701-NIGHTLY-pdx215`) estraendoli dalla ROM ufficiale LineageOS, oppure ottenerli
da un Nandroid[^nandroid] backup fatto in TWRP nella Fase 7. I comandi di flash che usano questi
file, e che servono in ripristino, sono quelli sotto.

```powershell
fastboot getvar current-slot
# supponiamo lo slot attivo sia "a"
fastboot flash boot boot_a.img
fastboot flash vbmeta vbmeta_a.img
fastboot flash dtbo dtbo_a.img
```

Gate: i tre file boot, vbmeta e dtbo dello slot attivo sono salvati e conservati prima di proseguire.

Riferimento: `03-install-adb-and-fastboot-for-a-sony-xperia-1-iii/01-fastboot-mode-pc-usb-cable.md`,
sezione Backup del boot dello slot attivo via fastboot.

## Fase 6 - Flashare TWRP sullo slot passivo (PC)

Serve la TWRP compatibile con pdx215, ad esempio `twrp-3.7.0-pdx215.img`, copiata nella cartella
platform-tools. Si passa allo slot passivo, si flasha TWRP nella partizione boot e si riavvia
direttamente in recovery per non sovrascriverla. Il flash, a differenza di `fastboot boot`, rende
TWRP permanente fino al flash successivo.

```powershell
fastboot --set-active=other
fastboot flash boot twrp-3.7.0-pdx215.img
fastboot reboot recovery
```

Gate: TWRP si avvia e mostra l'interfaccia touch con Install, Backup, Wipe, Advanced.

Rollback: se LineageOS non parte dallo slot passivo o TWRP non funziona, si rientra in fastboot e si
torna allo slot con il sistema funzionante.

```powershell
fastboot --set-active=a
```

Riferimento: `04-root-permissions-with-magisk/02-installare-magisk.md`, sezioni Verifica slot attivo
e Installazione e avvio TWRP.

## Fase 7 - Backup completo Nandroid in TWRP (manuale)

In TWRP, dal menu Backup, selezionare Boot, System e Data e confermare con lo swipe. Questo produce
l'immagine completa dello stato attuale, ripristinabile dal menu Restore. Conviene catturare uno
screenshot della schermata di backup completata.

Riferimento: `04-root-permissions-with-magisk/02-installare-magisk.md`, sezione Uso di TWRP per
backup completo.

## Fase 8 - Installare Magisk (PC + manuale)

Magisk richiede il bootloader sbloccato, gia' ottenuto. Il documento valuta due metodi e indica come
piu' lineare quello da recovery; qui si adotta come metodo principale la recovery, con due varianti.

Metodo principale, da Lineage Recovery via sideload: si scarica Magisk da GitHub, si rinomina il file
`.apk` in `.zip`, si riavvia in recovery, si abilita ADB sideload dal menu e si invia il file dal PC.

```powershell
# rinominare l'apk in zip (esempio)
# mv Magisk-v26.4.apk Magisk-v26.4.zip
adb reboot recovery
adb sideload Magisk-v26.4.zip
```

Variante, da TWRP: copiare `Magisk-v##.zip` nella memoria del telefono, riavviare in TWRP con Volume
Giu' piu' Power, andare in Install, selezionare lo zip e fare swipe per installare. Al riavvio l'app
Magisk e' presente.

Riferimento: `04-root-permissions-with-magisk/02-installare-magisk.md`, sezioni Da recovery
personalizzata, Base e Installazione Magisk da Lineage recovery.

## Fase 9 - Verifica root e gestione di SELinux (manuale + PC)

Dopo il riavvio si apre l'app Magisk. Se mostra lo stato verde, il root e' attivo e la procedura e'
conclusa. Se Magisk risulta installato ma il root non e' attivo o i moduli non funzionano, la causa
tipica su build NIGHTLY e' SELinux[^selinux] troppo restrittivo che blocca le modifiche agli script
di avvio. La soluzione alternativa e' patchare manualmente il boot image con Magisk e flashare il
risultato su entrambi gli slot.

```powershell
fastboot flash boot_a magisk-patched.img
fastboot flash boot_b magisk-patched.img
```

Gate: stato verde in Magisk, root attivo.

Riferimento: `04-root-permissions-with-magisk/02-installare-magisk.md`, sezione Installazione vera
Magisk, e `02-factory-reset-and-custom-rom/02-the-sideload.md`.

## Fase 10 - Verifica USB OTG (PC + manuale)

Il pdx215 supporta ufficialmente USB OTG[^otg] e il kernel del port LineageOS lo abilita. Non esiste
un interruttore dedicato: si verifica collegando una periferica e controllando che venga montata,
oppure da shell.

```powershell
adb shell ls /dev/block/sd*
adb shell "dmesg | grep -i usb"
```

In alternativa si usa un'app come USB OTG Checker. Una riga di `dmesg` del tipo
`usb 1-1: new high-speed USB device number ...` conferma il rilevamento.

Riferimento: `05-usb-otg-verification-in-lineageos.md`.

## Appendice - Ripristino del Google Play Store

Se dopo un reset o un'installazione pulita manca il Play Store, si sideloadano le GApps. Il pacchetto
indicato e' MindTheGapps, compatibile con LineageOS. Si riavvia in recovery, si abilita ADB sideload
e si invia lo zip dal PC.

```powershell
adb sideload nomefile.zip
```

Riferimento: `02-factory-reset-and-custom-rom/02-the-sideload.md`, sezione Re-installare il Google
Play store.

[^ab]: *A/B partitioning* - schema con due copie delle partizioni critiche (boot, system, ...), una
attiva e una passiva, pensato per aggiornamenti senza rischio e fallback.

[^adb]: *ADB*, Android Debug Bridge - strumento a riga di comando per comunicare con un dispositivo
Android collegato; *fastboot* e' il suo equivalente per la modalita' bootloader.

[^oem]: *OEM*, Original Equipment Manufacturer - qui la voce Sblocco OEM autorizza lo sblocco del
bootloader.

[^imei]: *IMEI*, International Mobile Equipment Identity - identificativo univoco del telefono,
richiesto da Sony per generare il codice di sblocco.

[^nandroid]: *Nandroid backup* - immagine completa dello stato del dispositivo creata da una recovery
come TWRP, ripristinabile integralmente.

[^selinux]: *SELinux*, Security-Enhanced Linux - sistema di controllo degli accessi del kernel; in
modalita' restrittiva puo' impedire a Magisk di modificare gli script di avvio.

[^otg]: *USB OTG*, On-The-Go - modalita' host che permette al telefono di pilotare periferiche USB
collegate, ad esempio un DAC o una chiavetta.
