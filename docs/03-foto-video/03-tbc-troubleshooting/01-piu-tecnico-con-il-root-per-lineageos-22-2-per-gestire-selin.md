# Più tecnico con il root per LineageOS 22.2 per gestire SELinux

> LEGACY - troubleshooting del percorso GCam, abbandonato in favore delle app proprietarie Sony. Conservato come riferimento storico. Per il percorso attuale vedi `../../RUNBOOK.md`.

**ottenere i permessi root su LineageOS**

** Passaggi per ottenere il root con Magisk su LineageOS**

**1. Scarica Magisk**

Scarica l’ultima versione di **Magisk APK** da GitHub ufficiale.

Rinomina il file .apk in .zip (es: Magisk-v27.0.apk → Magisk-v27.0.zip).

**2. Riavvia in recovery (TWRP o recovery Lineage)**

Spegni il telefono.

Avvia in recovery (di solito **Power + Volume Su**).

Se hai **TWRP** o la **recovery Lineage**, vai su **Install > seleziona il file Magisk.zip > Swipe per flashare**.

**3. Riavvia il sistema**

Dopo il flash, riavvia il telefono normalmente.

**4. Apri Magisk Manager**

Se non è già installato, reinstalla l’APK di Magisk.

Aprilo e verifica che lo **stato sia “Root attivo”**.

**5. Torna su Termux**

Ora, apri Termux e digita:

Dovrebbe comparire il prompt root (#) e una richiesta di permesso da Magisk.

 Vuoi che ti aiuti a verificare se hai già una recovery compatibile o a scaricare quella giusta per il tuo Xperia 1 III?

Posso cercarti il file .img corretto per TWRP o Lineage Recovery e guidarti nel flash passo passo. Fammi sapere!

Mettere SELinux in permissive per test. non ho capito perchè su apkpure mi fa solo un request update ma non un download

**ChatGPT ha detto:**

Ah, perfetto, ti spiego bene la questione SELinux e l’app per cambiarlo - e perché su APKPure ti fa solo “Request Update” senza scaricare:

**SELinux Mode Changer su APKPure**

**“Request Update”** su APKPure spesso significa che l’app NON è pubblicata direttamente lì o è una versione “placeholder” che ti invita ad aggiornare o scaricare altrove.

Alcune app di sistema o root, come SELinux Mode Changer, NON sono sempre disponibili su APKPure per questioni di permessi o policy.

**Come fare per SELinux Mode Changer**

**Scarica da fonti alternative affidabili**

Puoi trovare APK di SELinux Mode Changer su siti come APKMirror o XDA (attento però alle fonti per sicurezza).

Oppure ti posso fornire direttamente il link di una versione sicura.

**Requisiti**

Per usare SELinux Mode Changer devi avere il telefono **rootato** (o almeno accesso superuser).

Se non hai root, NON potrai cambiare SELinux da Enforcing a Permissive.

Il root su LineageOS è opzionale, quindi se non l’hai fatto probabilmente non hai i permessi necessari.

**Cosa significa SELinux Enforcing vs Permissive**

**Enforcing** = sistema blocca le azioni non consentite (più sicuro, ma più restrittivo).

**Permissive** = sistema permette tutto, ma registra i “blocchi” (utile per testare se un’app crasha per permessi).

**Quindi, se non hai root…**

Non puoi cambiare SELinux da app o senza root.

È normale che app come SELinux Mode Changer non funzionino o non si installino correttamente.

Questo può essere il motivo per cui GCam crasha su LineageOS Nightly (alcune funzioni camera richiedono permessi o moduli che la ROM non concede).

Opzioni alternative per te:

Se vuoi, posso aiutarti a capire se puoi abilitare root su LineageOS (se vuoi provarlo).

Se no, la soluzione più pratica è usare Open Camera o una versione di GCam compatibile senza bisogno di SELinux permissive.

come abilito il root e quindi poi SELinux Mode Changer?

**ChatGPT ha detto:**

Perfetto, vuoi abilitare il root su LineageOS 22.2 sul tuo Sony Xperia 1 III per poter gestire SELinux e magari migliorare la compatibilità della GCam. Ti spiego passo passo come fare!

**1. Prerequisiti importanti**

**Backup:** prima di tutto, fai un backup completo dei tuoi dati. Rooting può causare perdita dati o problemi se fatto male.

**Sblocco bootloader:** per rootare, il bootloader deve essere sbloccato (immagino già lo sia se usi LineageOS).

**PC con ADB e Fastboot:** ti servirà un PC per collegare il telefono via USB e usare comandi.

**2. Installa Magisk per ottenere root**

Magisk è il sistema più usato per root su LineageOS perché consente root “systemless” (modifiche senza alterare la partizione di sistema).

**Passaggi principali:**

**Step 1: Scarica Magisk**

Vai sul sito ufficiale Magisk: [https://github.com/topjohnwu/Magisk/releases](https://github.com/topjohnwu/Magisk/releases)

Scarica l’ultima versione in formato ZIP e il file APK (per gestire il root da telefono).

**Step 2: Prepara il file boot.img**

Serve estrarre l’immagine boot.img dal firmware della tua ROM LineageOS 22.2 (la tua build lineage_pdx215-userdebug 15 ...).

Puoi trovarla nel file zip della ROM o scaricarla dal sito LineageOS.

Usa un tool come 7zip per aprire il zip ROM e estrarre boot.img.

**Step 3: Patch del boot.img con Magisk**

Copia boot.img sul telefono.

Installa e apri l’app Magisk APK sul telefono.

Nel menu dell’app, scegli “Install” > “Select and Patch a File” e seleziona boot.img.

L’app creerà un file magisk_patched.img nella cartella Download.

**Step 4: Flasha il boot.img patchato**

Copia magisk_patched.img sul PC.

Riavvia il telefono in modalità fastboot (di solito Volume Su + Power, ma varia).

Sul PC, apri terminale o cmd e digita:

nginx

CopiaModifica

fastboot flash boot magisk_patched.img

fastboot reboot

**Step 5: Verifica root**

Al riavvio, apri l’app Magisk Manager.

Se tutto è andato bene, vedi che il root è attivo.

Puoi anche scaricare e usare “Root Checker” dal web per verificarlo.

**3. Cambia SELinux in Permissive**

Ora che hai root, puoi installare SELinux Mode Changer (cerco un APK affidabile e te lo passo).

Apri l’app e cambia SELinux da Enforcing a Permissive.

Riavvia il telefono per applicare le modifiche.

**4. Prova di nuovo GCam**

Dopo aver messo SELinux in Permissive, prova a far partire GCam.

Spesso così non crasha più e funziona bene.

**Attenzione e consigli**

Root e modifica SELinux possono rendere il telefono meno sicuro. Usa con cautela.

Le Nightly ROM possono avere bug imprevisti dopo il root.

Se qualcosa va storto, puoi sempre riflashare la ROM da zero.

Se vuoi, ti posso aiutare a recuperare il boot.img esatto, a scaricare Magisk e a fare ogni passaggio con comandi precisi.
