# Installare Magisk

Per installare Magisk serve **bootloader sbloccato** (cosa che *hai già fatto*, visto che usi LineageOS). Si installa tramite:

- fastboot flash + boot patching
- Oppure direttamente da recovery personalizzata (es. TWRP, Lineage Recovery)
   - La scelta più semplice per lo specifico caso di installare Magisk è Lineage Recovery

Si avvia poi il sistema e si installa Magisk App. L’app gestisce poi tutto: root, moduli, aggiornamenti.

## fastboot flash + boot patching (aborted)

Si sblocca il bootloader (l’hai già fatto per LineageOS) e si connette il telefono al PC in modalità fastboot. Prima si flasha la recovery di Magisk temporanea per patchare il boot, poi si avvia nel sistema, si apre Magisk App e si completa l’installazione.

Questo ha il vantaggio di essere un approccio più pulito, systemless, con meno rischi. Tuttavia, procedere con il metodo via recovery personalizzata in questo caso è più lineare perché:

- Tu hai già LineageOS installato (quindi hai Lineage Recovery o puoi facilmente installare TWRP).
- Basta copiare il file .zip di Magisk nel telefono, avviare la recovery → flashare → fatto.

Questo metodo è più semplice, non richiede un PC con comandi fastboot complicati, ed è più sicuro per un utente non esperto.

## Da recovery personalizzata

Con LineageOS si può utilizzare Lineage Recovery, quindi già pronto o facilmente installabile e non serve  né il PC né comandi fastboot avanzati.

- Da recovery si può flashare direttamente il pacchetto Magisk .zip
- Riavvii ed è pronto

Tuttavia, è da considerare l’opzione di installare TWRP perché è migliore per fare backup completi. Un backup completo in TWRP si chiama “Nandroid Backup” e crea un’immagine completa del tuo stato attuale. Lineage Recovery è minimal e non supporta Nandroid backup completi, solo installazione ZIP e wipe.

Dunque, se si vuole sperimentare, installare Magisk o tweak senza paura e poter sempre tornare indietro con 2 tocchi andiamo passo-passo in modo molto semplice, cosa significa usare recovery personalizzata (TWRP), come installarla e perché è utile per fare backup, flash di ZIP come Magisk e molto altro. I passaggi concettuali sono:

![](assets/img-0000.png)

La standard (stock o Lineage Recovery) permette solo di installare ZIP e fare Wipe (reset selettivo) ovvero può cancellare solo alcune parti (cache, system, data, ecc.) ma non backup completi. TWRP è una recovery potenziata, con interfaccia touch, file manager, backup (Nandroid), ripristino e molto altro. Il flusso consigliato è:

- Installa TWRP
- Entra in TWRP e fai un backup completo
- Flasha Magisk sotto TWRP
- Se qualcosa va male → ripristini il backup in un click

Per arrivare a TWRP su Xperia 1 III (pdx215) serve oltre al bootloader sbloccato anche un PC Windows /Linux con adb e fastboot e un cavo USB-C.

### Verifica slot attivo e backup minimi essenziali PRIMA di TWRP

Prima di eseguire il comando fastboot --set-active=other che verrà visto in seguito, è intelligente effettuare i backup minimi essenziali PRIMA di flashare TWRP li fai da PC, NON da TWRP. 0Innanzitutto, serve salvare almeno tre partizioni.

fastboot getvar current-slot

\# Supponiamo sia "a"

fastboot flash boot boot_a.img

fastboot flash vbmeta vbmeta_a.img

fastboot flash dtbo dtbo_a.img

Salva questi file PRIMA di flashare qualsiasi cosa.

**Come si fa a salvarli?**

Devi estrarre le partizioni attuali (puoi scaricarle da LineageOS ufficiale o fare il dump tu con dd via adb/fastboot, ma è più comodo scaricarle già pronte).

Non si vuole flashare TWRP sullo slot attivo, ma si vuole **flashare TWRP sullo slot passivo** per mantenere integro il sistema attivo, e prima fare un **backup “minimo vitale” delle partizioni di avvio**. In questo senso si vuole flashare TWRP su quello passivo e conservare quello attivo come backup.

**Flashare TWRP nello slot passivo (es. b)**, lasciando intatto il tuo LineageOS nello slot attivo (es. a), e fare un **backup delle partizioni di boot del tuo slot attivo**, così in caso di problemi puoi sempre ripristinarle.

Questo mi permette comunque di ripristinare il mio telefono esattamente com'era perchè i dati comunque sono conservati sul dispositivo?   **Sì**, se lasci intatto lo **slot attivo** (es. a) e **flashi solo nello slot passivo** (b), **i tuoi dati, app e sistema rimangono intatti**. Il backup delle partizioni serve solo a **ripristinare l’avvio**, non i dati (che restano dove sono).

I backup minimi essenziali PRIMA di flashare TWRP li fai da PC, NON da TWRP. 0Innanzitutto, serve salvare almeno tre partizioni come visto nella sezione relativa al backup del boot dello slot attivo via fastboot.

(vedi se ci sono altre cose sopra da mettere su questa sezione)

### Installazione e avvio TWRP per Xperia 1 III (pdx215)

Innanzitutto, serve la TWRP compatibile con *pdx215*. Un utente su XDA ha rilasciato una build affidabile [https://www.reddit.com/r/SonyXperia/comments/13jpnns/twrp_recovery_for_the_xperia_1_iii](https://www.reddit.com/r/SonyXperia/comments/13jpnns/twrp_recovery_for_the_xperia_1_iii) per cui bisogna scaricare il file .img (es. twrp-3.7.0-pdx215.img). Quindi bisogna scaricare la TWRP compatibile con pdx215 (es. da XDA o SonyBasement)

Dopodichè bisogna trasferirlo nella cartella platform-tools sul PC e collegare un telefono al PC con un cavo USB-C e accedere alla modalità fastboot.

Bisogna poi aprire il terminale nella cartella platform-tools con un terminale nel PC nella cartella con TWRP .img e digitare:

	fastboot --set-active=other

Questo perché quando si flasha qualcosa nella partizione boot, è meglio farlo nello slot passivo, così se qualcosa va storto si può sempre tornare allo slot attivo. In questo caso è per flashare TWRP nello slot opposto per sicurezza così si può testare TWRP e tornare indietro. Quindi per capire, si sta impostando lo slot “other”, si flasha poi TWRP (prossimo comando) e poi si avvia in recovery e se tutto funziona si può rimanere lì altrimenti se qualcosa non va si può forzare il boot dallo slot precedente. Dopo aver switchato da Slot A a Slot B (con fastboot --set-active=other), e installato TWRP o Magisk, si può continuare ad usare normalmente Android dallo Slot B. LineageOS è installato su entrambi gli slot oppure soltanto su uno in base alle azioni fatte in passato. Entrare nello slot alternativo permette LI’ dentro di flashare Magisk, fare backup e avviare Android da lì e QUELLO diventerà il sistema attivo con LineageOS + Magisk + TWRP se lì però LineageOS c’è. Posso usare lo slot B (dopo lo switch) solo se LineageOS è installato lì - vedere anche sezione where is LineageOS installed?. In questo senso può non essere mai necessario tornare allo Slot A perché se tutto funziona (con LineageOS che parte e TWRP che è accessibile) si può continuare ad usare lo slot alternativo come normale, ricevere aggiornamenti che verranno scritti su slot A e aggiornare Lineage OS via recovery come sempre.

Dunque, per fare il flash:

	fastboot flash boot twrp-3.7.0-pdx215.img

Per installare TWRP. Infatti, il fil fastboot flash è importante per tenere TWRP in modo stabile sul dispositivo. Altrimenti con un semplice fastboot boot twrp-3.7.0-pdx215.img avrebbe avviato TWRP solo in RAM e in quanto tale sarebbe stato temporaneo e sarebbe sparito al riavvio. Fastboot boot avvia solo TWRP in RAM, ma non lo installa. Noi invece lo flasciamo nella partizione boot → TWRP rimane permanente finché non flasci di nuovo

In seguito, digitare:

fastboot reboot recovery

Per avviare direttamente nella recovery per non sovrascriverla. Questo fa partire TWRP immediatamente, così viene inizializzata e non viene sovrascritta. A questo punto partirà TWRP e sei pronto per fare backup, installare Magisk ecc.

Poi *telefono spento* → premi **Volume Giù + Power** per entrare in TWRP

Se si vede l’interfaccia Touch (Install, backup, Wipe, Advanced) e si vede qualcosa come [https://github.com/sonybasement/twrp_android_sony_pdx215](https://github.com/sonybasement/twrp_android_sony_pdx215) significa che funziona tutto.

Riavvii in Android

 Se funziona tutto → resti tranquillamente su B

 Se non funziona → torni allo slot A con un comando

Se qualcosa non parte, bisogna rientrare in fastboot e switchare di nuovo sullo slot con il sistema operativo funzionante:

fastboot --set active-a

Questo è *obbligatorio* se LineageOS non parte dopo il flash, TWRP non funziona o semplicemente si vuole tornare esatttamente alla configurazione precedente.

In altre parole, in generale, si potrebbe usare lo slot B anche se LineageOS è installato solo nello slot A purchè vengano copiati manualmente boot + system anche nello slot B oppure verificare se sono già lì (cosa che ti spiego sotto). Se non lo fai e attivi lo slot B a caso → il telefono potrebbe non avviarsi dopo il riavvio. MA NON È UN PROBLEMA: torni in fastboot e dici fastboot --set-active=a per riprendere da dove eri. Niente panico.

### Uso di TWRP per backup completo (Nandroid backup)

In TWRP, fai un **backup Nandroid** completo (è nelle opzioni Backup). Quindi una volta in TWRP, vai su:

**Backup** → seleziona *Boot, System, Data*

Trascina per confermare → parte il backup completo

Quando torni: rivedrai uno ZIP contenente il backup.
In caso di problemi:

Avvia TWRP

Vai su **Restore** → scegli il backup e ripristina

Se tutto è a posto, continui con … Magisk

### Installazione vera Magisk

#### Base

**Installazione Magisk da TWRP (base):**

Copia il file Magisk-v##.zip nella memoria del telefono

Riavvia in TWRP (Volume Giù + Power)

Vai su **Install**, selezioni Magisk-v##.zip, e swipe per installare

Riavvia nel sistema e applicazione Magisk sarà pronta

#### Magisk .zip + apk aggiornato

  Guida passo-passo per flash sotto TWRP

  Moduli consigliati (termico, GPU, ecc.)

#### (TBC) Installazione Magisk da Lineage recovery

È possibile installare Magisk da Lineage Recovery, senza bisogno di TWRP. Per questo basta soltanto avere:

- Lineage Recovery installata
- Magisk ZIP (v26.x o superiore) o .apk rinominato in .zip
- PC con adb

Pertanto, si può quindi:

1. Scaricare Magisk v26+ da GitHub [https://github.com/topjohnwu/Magisk](https://github.com/topjohnwu/Magisk)
1. Rinominare il file .apk in .zip (es. mv Magisk-v26.4.apk Magisk-v26.4.zip)
1. Riavviare in recovery

adb reboot recovery

1. Abilitare ADB sideload e inviare il file

adb sideload Magisk-v26.4.zip

1. Riavviare il sistema. A questo punto l'app Magisk sarà visibile e il root attivo.

Il metodo è testato e stabile su **Lineage Recovery**, a patto che la build supporti init.d o init.rc patchabili. Alcune versioni di LineageOS (o Recovery) limitano o rendono non modificabili questi script per motivi di sicurezza o stabilità. In quei casi, Magisk non riesce a eseguire il root correttamente perché SELinux è troppo restrittivo.

Con la versione LineageOS 22.2-20250701-NIGHTLY-pdx215 Magisk ha bisogno di patchare script di avvio (init.d o init.rc) per avviare i suoi servizi (root, moduli, Zygisk). SELinux e il sistema di sicurezza Android possono impedire di scrivere o eseguire questi script. In alcune versioni di LineageOS, soprattutto NIGHTLY, SELinux è più restrittivo, e blocca le modifiche. Bisogna quindi controllare DOPO aver installato MAgisk:

- Se dopo il reboot Magisk funziona e vedi lo status verde (root attivo)  tutto OK.
- Se Magisk è installato ma non ottieni root, o i moduli non funzionano  SELinux sta impedendo le modifiche a init.d/init.rc.

In questo caso bisogna attuare una soluzione alternativa:

- Patchare il boot image manualmente con Magisk (magisk-patched.img)
- Flashare con:
- fastboot flash boot_a magisk-patched.img
- fastboot flash boot_b magisk-patched.img

