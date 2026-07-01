# Photos and videos

> Percorso primario: applicazioni fotografiche proprietarie Sony (Photography Pro, Cinema Pro, External Monitor), installate dalle APK in `_notes/apks`. Vedi il `RUNBOOK.md` di questa cartella e la sezione `04-tbc-app-proprietarie-sony.md`. Le sezioni GCam (Camera2 API, XML GCam, troubleshooting SELinux) sono marcate LEGACY e conservate solo come riferimento storico.

Esplora sony Xperia 1 III per la fotografia (prendi chat su Copilot privato) e integra con l’altra chat di chatGPT  e Copilot

Ho a disposizione apkpure, che applicazioni posso utilizzare sony Xperia 1 III con serial number QV7812NL8K e con Build number lineage_pdx215-userdebug 15 BP1A.250505.0053439504aa9 e LineageOS version 22.2-20250701-NIGHTLY-pdx215.

Hai uno **Xperia 1 III (pdx215)** con LineageOS 22.2 (Android 15) installato.

Hai uno **Xperia 1 III (pdx215)** con LineageOS 22.2 (Android 15) installato. Quindi:

 Android 15 (API 35) → compatibile con la maggior parte delle app recenti.
 Bootloader sbloccato → spesso permette di installare mod o fotocamere alternative.
 No Sony stock camera app (presumibilmente) → su LineageOS non sempre ci sono tutte le funzionalità foto originali Sony.

**APKs da provare (scaricabili da APKPure o simili)**

**① GCam (Google Camera mod)**

**GCam 8.x o 9.x mod** (Es. da BSG, Shamim, MTSL, Arnova)

Prova APKs specifici con supporto Snapdragon 888 (il tuo SoC).

Abilita HDR+, Night Sight, Astrophotography.

Può migliorare tantissimo la qualità rispetto alla Camera AOSP.

Cerca la versione *BSG GCam 9.2* o *Shamim GCam 8.8* per Android 14-15.

Scarica sempre il config XML giusto per il tuo modello.

**② Open Camera**

App open-source super stabile.

RAW, HDR, controllo ISO, esposizione.

Zero pubblicità.

Non fa miracoli sulla qualità come GCam, ma è molto configurabile.

**③ Footej Camera 2**

Interfaccia semplice.

Scatta RAW.

Controllo manuale su esposizione, ISO, focus.

Non ha la qualità di GCam, ma meglio della stock AOSP camera.

**④ ProShot**

Ottima interfaccia “pro”.

Controlli manuali completi.

Scatto RAW + JPG.

Modalità lunga esposizione.

**⑤ Manual Camera DSLR**

Più basica, ma controlli manuali totali.

Permette di salvare RAW.

Utile per lunghe esposizioni.

**⑥ HedgeCam 2**

Fork di Open Camera.

Qualche funzione extra come supporto multi-camera, se supportato dal tuo device.

**Note importanti per Xperia 1 III su LineageOS:**

**Tele / UltraWide**: molte app (soprattutto GCam) potrebbero non vedere tutte le 3 fotocamere. È un limite degli HAL Camera di AOSP su device Sony.

**Sony Camera app** ufficiale → **NON funziona su LineageOS** (non puoi estrarla da firmware stock senza framework proprietari).

**RAW**: funziona con Open Camera, ProShot ecc., ma la qualità dipende molto dai driver disponibili in LineageOS.

**Video 4K 120fps**: spesso non disponibile fuori da firmware Sony.

**HDR video**: non disponibile su LineageOS.

Prova GCam mod, se riesci a farlo funzionare. Sul tuo Snapdragon 888 è la miglior opzione per qualità pura.

Se non funziona → Open Camera o ProShot sono le migliori alternative.

Vuoi foto in stile “punta e scatta” o ti interessano controlli manuali e RAW? Vuoi usare tutte le 3 fotocamere (wide, ultrawide, tele)? Fammi sapere così posso consigliarti meglio le app più adatte!

Vuoi foto in stile “punta e scatta” o ti interessano controlli manuali e RAW? Vuoi usare tutte le 3 fotocamere (wide, ultrawide, tele)? Fammi sapere così posso consigliarti meglio le app più adatte!

Allora cosa mi perdo se non le uso tutte e tre? comunque vorrei un utilizzo da immortalare momenti di vacanza ma con qualità e comunque non perdermi la possibilità di avere appunto la possibilità di fare le foto in RAW

Ti spiego un po’ le differenze e cosa comporta usare solo alcune fotocamere o tutte e tre, e come bilanciare qualità, semplicità e RAW per le tue vacanze.

**1. Usare tutte e tre le fotocamere (wide, ultrawide, tele)**

**Pro:**

**Massima versatilità:**

Wide (standard): ottimo per quasi tutte le situazioni.

Ultrawide: per panorami, spazi ampi, foto di gruppo.

Tele: per zoom ottico, ritratti con sfocatura naturale (bokeh).

Ti permette di coprire ogni tipo di scena senza perdere qualità (senza zoom digitale).

**Contro:**

Su LineageOS + app non Sony, spesso non c’è supporto completo per passare tra le fotocamere multiple.

Potresti non riuscire a fare switching automatico o scattare RAW da tutte.

Alcune app (come GCam mod) potrebbero vedere solo la wide principale, quindi perdi tele e ultrawide.

**2. Usare solo la fotocamera wide principale**

**Pro:**

Funziona al 100% in quasi tutte le app.

Spesso la fotocamera principale ha il sensore migliore (più megapixel, stabilizzazione).

Puoi facilmente scattare in RAW.

Più semplice da gestire in app di terze parti.

**Contro:**

Meno versatilità in scene panoramiche o con zoom ottico.

Se vuoi zoom, devi fare zoom digitale (qualità inferiore).

**3. Uso per vacanze: qualità + facilità d’uso + RAW**

**Consiglio pratico:**

Punta sulla **fotocamera principale** per la maggior parte degli scatti, così hai la massima qualità e RAW garantito.

Porta con te un’app che supporta il RAW (Open Camera o ProShot sono perfette).

Usa l’ultrawide solo se l’app la supporta e ti serve davvero un panorama ampio.

Se ti interessa fare zoom ottico per ritratti o dettagli, prova GCam mod (se supporta tele).

Alternativamente, scatta wide e poi ritaglia in post se serve un po’ di zoom.

**4. App consigliate per il tuo scenario**

**Open Camera:** supporta scatti RAW, semplice, affidabile, buona qualità, più facile usare la wide.

**ProShot:** ottimi controlli manuali, RAW, ottima per chi vuole un po’ più di controllo e qualità.

**GCam mod:** se la trovi compatibile, ti migliora molto HDR, colori, foto in bassa luce, e potenzialmente ha supporto tele/ultrawide.

**Footej Camera 2:** per un compromesso fra facilità d’uso e RAW.

**Cosa perdi se non usi tutte e tre le fotocamere?**

**Perdita di versatilità**:
Non potrai cambiare obiettivo (ultrawide o tele) per adattarti meglio alla scena.

Se vuoi una foto panoramica, senza ultrawide sei costretto a fare più scatti o foto più “ristrette”.

Se vuoi zoomare senza perdere qualità, senza tele fai solo zoom digitale (che degrada la qualità).

**Qualità specifica per scenario**:
Le tre fotocamere sono ottimizzate per scopi diversi, quindi se usi solo la wide, potresti non ottenere la migliore resa in tutte le situazioni.

Tele per ritratti nitidi con sfondo sfocato.

Ultrawide per paesaggi e interni spaziosi.

Wide per foto generali e dettagli.

**Però…**

La **fotocamera wide principale** è quella con il sensore migliore e qualità più alta in generale.

Se scatti solo con quella, avrai comunque ottime foto, anche RAW, e buona qualità complessiva.

Se invece usi tele e ultrawide, ottieni più opzioni e qualità ottimizzata in specifici casi d’uso.

**In pratica**

**Perdere potenzialità e qualità** significa principalmente **perdere la capacità di scattare in modo ottimale certe foto (zoom, panorami ampi, ritratti)**, non che la qualità della wide sarà brutta o scadente.

Quindi, se la tua priorità è fare belle foto in vacanza senza complicazioni, usare la wide + RAW è più che sufficiente.

Se invece vuoi la massima versatilità e qualità in ogni situazione, allora sì, usare tutte e tre le fotocamere è meglio.

ricapitoliamo considerando che la mia priorità è fare belle foto in vacanza senza complicazioni, usare la wide + RAW e quindi capire l'app migliore di tutte da poter scaricare da apkpure

**Miglior app per te: Open Camera**

**Perché Open Camera?**

È gratuita e open source, senza pubblicità.

Supporta pienamente il RAW su dispositivi che lo consentono (come il tuo Xperia 1 III).

Ha modalità “auto” semplici, ma anche controlli manuali se vuoi (ISO, esposizione, focus).

È stabile, leggera e compatibile con quasi tutti i telefoni Android e custom ROM come LineageOS.

Supporta il formato DNG per RAW.

Puoi salvare facilmente JPG + RAW.

Consente di configurare molte impostazioni per ottimizzare foto in vacanza senza impazzire.

Quindi al massimo valuterei GCam mod: la migliore in qualità se funziona sul tuo device, ma spesso complicata da configurare e non garantita su LineageOS. Se mi dici che in linea teorica sarebbe migliore di Open Camera la valuto

**ChatGPT ha detto:**

Esatto, in linea teorica la **GCam mod** è quasi sempre migliore di Open Camera in termini di qualità fotografica pura, soprattutto per:

**HDR avanzato** (migliore gestione delle luci e ombre)

**Night Sight** (foto in bassa luce più nitide e luminose)

**Elaborazione AI** (più dettagli, colori più vivi)

**Zoom digitale migliorato** grazie a super risoluzione computazionale

A volte supporto parziale per tele e ultrawide

**Però ecco i “ma” importanti per il tuo caso su LineageOS Xperia 1 III:**

La GCam mod **non è ufficiale Sony**, quindi l’integrazione con le fotocamere multiple (tele/ultrawide) può non funzionare o essere limitata.

Spesso richiede configurazioni manuali (config XML da importare).

Su ROM custom (come LineageOS) può non funzionare al 100% o crashare.

Occorre trovare la versione giusta (modder giusto, versione corretta per Snapdragon 888 + Android 15).

**Cosa fare se vuoi provare GCam:**

Provo a cercarti la versione GCam mod più aggiornata e affidabile per il tuo Snapdragon 888 + Android 15 (Xperia 1 III).

Ti fornisco un file di configurazione XML per la migliore resa.

Ti guido nell’installazione e configurazione.

erfetto! Ecco cosa ti propongo: ti cerco subito la versione GCam mod più aggiornata e compatibile con Snapdragon 888 e Android 15, adatta al tuo Xperia 1 III su LineageOS.

Poi ti fornisco anche il file di configurazione XML per ottimizzare la resa e ti spiego passo passo come installarla e configurarla.

Fammi un attimo cercare...

Perfetto, procediamo con l'installazione e la configurazione della GCam mod per il tuo Sony Xperia 1 III con Snapdragon 888 e Android 15 (LineageOS). Questa versione dovrebbe offrire una qualità fotografica superiore rispetto a Open Camera, soprattutto per HDR, Night Sight e dettagli in condizioni di scarsa illuminazione.

 Passo 1: Scarica l'APK della GCam mod

Una versione consigliata per dispositivi con Snapdragon 888 è la MGC_8.8.224_A11_V14a_snap.apk. Questa versione è stata segnalata come compatibile con Android 15 e offre buone prestazioni senza necessità di configurazioni avanzate.

[https://www.reddit.com/r/NOTHING/comments/1hlz4d8/gcam](https://www.reddit.com/r/NOTHING/comments/1hlz4d8/gcam)

Una versione consigliata per dispositivi con Snapdragon 888 è la MGC_8.8.224_A11_V14a_snap.apk. Questa versione è stata segnalata come compatibile con Android 15 e offre buone prestazioni senza necessità di configurazioni avanzate.

https://www.reddit.com/r/NOTHING/comments/1hlz4d8/gcam

Però un utente reddit dice "It's the 2nd option on that page" che però è MGC_8.8.224_A11_V14a_MGC.apk (com.android.mgc)

quale devo prendere per il mio Sony Xperia 1 III con serial number QV7812NL8K e con Build number lineage_pdx215-userdebug 15 BP1A.250505.0053439504aa9 e LineageOS version 22.2-20250701-NIGHTLY-pdx215

**Le due versioni che hai menzionato:**

**MGC_8.8.224_A11_V14a_snap.apk**

Contiene “snap” nel nome, indica versione ottimizzata per chipset Snapdragon.

Probabilmente la scelta più adatta per il tuo Xperia 1 III (Snapdragon 888).

**MGC_8.8.224_A11_V14a_MGC.apk (com.android.mgc)**

Versione “standard” senza indicazione specifica per Snapdragon.

Potrebbe funzionare, ma forse non ottimizzata per il tuo SoC.

**Cosa ti consiglio?**

**Prima prova la versione “snap”**, cioè la **MGC_8.8.224_A11_V14a_snap.apk**, perché è specificamente pensata per Snapdragon 888 e dovrebbe offrirti stabilità e prestazioni migliori su LineageOS Android 15.

Se hai problemi (crash, qualità foto bassa), allora prova la versione “standard” **MGC_8.8.224_A11_V14a_MGC.apk**.

**Perché?**

La versione con “snap” è buildata tenendo conto delle peculiarità del SoC Snapdragon, che influenza driver e compatibilità fotocamera.

La versione “standard” è più generica, può essere meno ottimizzata ma a volte più stabile su certi dispositivi.

**Ulteriore consiglio:**

Se trovi un file XML di configurazione dedicato per Xperia 1 III (pdx215) o Snapdragon 888, usalo su entrambe le versioni per massimizzare la resa.

Verifica che Camera2 API sia abilitata (su LineageOS di solito lo è) perché senza quella GCam non funziona correttamente.

L’app è stata installata con APKCombo Installer che poi dopo “Camera” ha detto “do you want to install this app?”

**Passo 2: Configura la GCam mod per il tuo Xperia 1 III**

Dopo aver installato l'APK, è consigliabile importare un file di configurazione (XML) specifico per il tuo dispositivo. Questo ottimizza le impostazioni per ottenere la migliore qualità fotografica possibile.

**Come importare il file XML:**

Scarica il file XML compatibile con il tuo dispositivo.

Apri l'app GCam.

Vai nelle impostazioni (icona dell'ingranaggio).

Seleziona "Importa configurazione XML" e scegli il file precedentemente scaricato.

Scarica il file XML e salvalo nella cartella GCam/Configs7/ nella memoria interna del telefono (se la cartella non c’è, creala).

Apri l’app GCam, fai doppio tap sull’area nera vicino al pulsante di scatto.

Dovrebbe apparire il menu di configurazione con il file XML.

Seleziona il file e clicca su “Restore” o “Applica”.

L’app si riavvierà con le nuove impostazioni ottimizzate.

**Passo 3: Impostazioni consigliate per l'uso quotidiano**

**Modalità HDR+**: abilitare automatico per migliorare la gamma dinamica delle foto.

**Night Sight**: Utilizzata per scatti in condizioni di scarsa illuminazione o notturne

**Salvataggio in formato RAW (DNG)**: abilitare per avere maggiore flessibilità in post-produzione.

**Controllo manuale di ISO ed esposizione**: Abilitato se desideri un controllo più preciso sulle tue foto.

**Passo 4: Verifica e ottimizza**

Scatta alcune foto in diverse condizioni di luce per verificare le prestazioni.

Se noti problemi come crash o scarsa qualità, prova a utilizzare una versione diversa dell'APK o a regolare le impostazioni.

Assicurati che la **Camera2 API** sia abilitata nel tuo dispositivo; altrimenti, la GCam potrebbe non funzionare correttamente.

Puoi aiutarmi a trovare un file XML specifico per il tuo Xperia 1 III o fornirti ulteriori dettagli su come ottimizzare le impostazioni per ottenere i migliori risultati fotografici. Contestualmente fammi vedere come Camera2 API sia abilitata (su LineageOS di solito lo è)

## Contenuti

- [Verificare che Camers2 API è abilitata con LineageOS](01-verificare-che-camers2-api-e-abilitata-con-lineageos.md)
- [Trovare un file XML di configurazione per GCam per Xperia 1 III (pdx215)](02-trovare-un-file-xml-di-configurazione-per-gcam-per-xperia-1.md)
- [(TBC) Troubleshooting](03-tbc-troubleshooting/README.md)
- [(TBC) App proprietarie Sony](04-tbc-app-proprietarie-sony.md)
