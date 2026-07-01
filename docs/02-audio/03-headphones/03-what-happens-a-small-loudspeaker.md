# What happens… a small loudspeaker!

Driver ad alta impedenza richiedono bobine con più avvolgimenti, quindi maggiore resistenza R e induttanza L. La forza che muove il diaframma viene dalla ben nota legge di Lorentz:

Con: 

- : intensità del campo magnetico
- : corrente nella bobina
- : lunghezza totale del filo immerso nel campo

Se la bobina ha più spire (alta impedenza), aumenta  e quindi comunque si ha maggiore forza a parità di corrente. La tensione necessaria per ottenere quella corrente è data dalla legge di Ohm.

La distorsione armonica in un driver è spesso legata all’escursione non lineare del diaframma. Driver ad alta impedenza sono spesso usati in trasduttori più grandi, dove:

- la massa mobile è più elevata
- il campo magnetico è più uniforme lungo l’escursione
- le forze elastiche di richiamo (sospensioni) sono più controllate

E quindi ci sono minori distorsioni a parità di SPL (livello di pressione sonora). La formula prima può essere pertanto pensata come una:

Dove  varia con la posizione della bobina e quindi dando una forza non lineare e causando distorsione armonica.

È sensato parlare di escursione non lineare in una cuffia, con movimenti di pochi mm  perché la dimensione assoluta dell’escursione non è ciò che determina la distorsione, ma la linearità della forza rispetto allo spostamento. Anche su escursioni di 0,5mm, se  non è costante, la forza generata non sarà lineare rispetto alla corrente. Se la molla meccanica di ritorno (la sospensione) non è lineare, l’escursione crea distorsioni armoniche. A livelli SPL elevati (anche in cuffie), si può entrare in regime non lineare con distorsione armonica misurabile. Alcune cuffie premium includono voice coil simmetrici per ridurre le distorsioni da escursione minima.

Quindi sì, nonostante la corsa sia breve, le tolleranze ridottissime e i materiali non perfettamente lineari rendono la distorsione da escursione un problema reale anche nelle cuffie [https://www.klippel.de/test-objects/micro-speakers-and-headphone-drivers.html](https://www.klippel.de/test-objects/micro-speakers-and-headphone-drivers.html). 

Inoltre, anche se l’escursione è limitata (< 1 mm), sia Bl(x) che Kms(x) hanno curvature non perfettamente lineari, sufficiente per generare distorsioni analizzabili (>90 dB SPL) [https://www.klippel.de/fileadmin/klippel/Files/Know_How/Application_Notes/AN_24_Telecomm_Driver.pdf](https://www.klippel.de/fileadmin/klippel/Files/Know_How/Application_Notes/AN_24_Telecomm_Driver.pdf). La posizione e il campo magnetico non sono uniformi in tutta la corsa del coil: gli effetti sono reali e misurabili anche su piccole dimensioni. Bisogna quindi considerare che la distorsione armonica non è assolutamente l’unico fattore di distorsione da tenere in considerazione [https://www.youtube.com/watch?v=i1sa50hzEcM](https://www.youtube.com/watch?v=i1sa50hzEcM). 

## A little more in speaker non-linearities

Provando ad essere un po' più rigorosi e tecnici sui principali fenomeni di distorsione nelle cuffie ci sarebbero da considerare anche altri fattori [https://www.klippel.de/fileadmin/_migrated/content_uploads/Klippel_Nonlinearity_Poster.pdf](https://www.klippel.de/fileadmin/_migrated/content_uploads/Klippel_Nonlinearity_Poster.pdf), [https://www.klippel.de/fileadmin/klippel/Files/News/Micro-speakers%20-%20Hybrids%20between%20headphones%20and%20loudspeakers.pdf](https://www.klippel.de/fileadmin/klippel/Files/News/Micro-speakers%20-%20Hybrids%20between%20headphones%20and%20loudspeakers.pdf): 

- L’intermodulazione (IMD)
- La non linearità del fattore di forza Bl(x)
- La non linearità della rigidità meccanica Kms(x)

La distorsione IMD si verifica quando due o più toni a frequenze diverse interagiscono nel driver, generando componenti a frequenze somma e differenza, che non appartengono agli armonici dei segnali originari [https://en.wikipedia.org/wiki/Intermodulation](https://en.wikipedia.org/wiki/Intermodulation). Nel driver, è causata da non linearità come Bl(x) o induttanza Le(x,i) e anche da resistenza meccanica dipendente dalla velocità Rms(v). L’IMD è percepibile come colorazione o “ruggine” nell’inviluppo del segnale ad alta frequenza, specialmente quando un tono grave modula uno acuto. Misure specifiche IMD su cuffie sono rare nella letteratura pubblica. Un documento AES dimostra misure comparabili tra modelli (“Headphone A, B…”) con IMD variabile sopra 1 kHz, ma i dettagli dei valori su modelli commerciali non sono resi noti [https://www.listeninc.com/wp/media/2023/06/AES137_Headphone_Distortion_Audibility.pdf](https://www.listeninc.com/wp/media/2023/06/AES137_Headphone_Distortion_Audibility.pdf).

Per le altre due non-linearità, quella del fattore di forza esprime come la forza magnetica cambia con lo spostamento del voice coil (bobina). Questo perché se Bl diminuisce allontanandosi da x=0, si introduce distorsione armonica e IMD. La rigidità della sospensione anche è fonte di non linearità, perché la stiffness (Kms) varia con la posizione (spesso asimmetrica), causando distorsione armonica, spostamenti DC (offset) e IMD. La rigidità non lineare Kms(x) produce **compressione del segnale**, rigonfiamenti e alterazioni della curva SPL rispetto a un modello lineare [https://www.klippel.de/fileadmin/klippel/Files/Know_How/Application_Notes/AN_24_Telecomm_Driver.pdf](https://www.klippel.de/fileadmin/klippel/Files/Know_How/Application_Notes/AN_24_Telecomm_Driver.pdf), [https://www.klippel.de/know-how/measurements/mechanical-vibration/voice-coil-displacement.html](https://www.klippel.de/know-how/measurements/mechanical-vibration/voice-coil-displacement.html). Come effetti combinati, le asimmetrie di Bl(x) o Kms(x) causano offset DC nella posizione del coil, peggiorando così le distorsioni successive e rendendo instabile la risposta.

È difficile trovare misurazioni Klippel su modelli di cuffie specifici (es. Sennheiser HD600, Beyerdynamic), perché la maggior parte delle analisi Klippel riguardano micro‑altoparlanti o trasduttori generici. Misurazioni estese di Bl(x), Kms(x), IMD su cuffie consumer non sono pubbliche – l’industria è molto riservata. I driver per in-ear o monitor in‑ear componente usano balanced-armature [https://www.klippel.de/test-objects/balanced-armature-transducer.html](https://www.klippel.de/test-objects/balanced-armature-transducer.html), con misure su T(x), Kms(x), ma non collegati a modelli venduti al consumatore finale.

aaaaaaaaaaaaaaaaaa.

Si scarica APK Combo Installer dal sito ufficiale perché permette di installare anche altri formati che non siano .apk

Si scarica l’.apk di apk pure e da DENTRO l’applicazione si scarica “Seeker” 

(mettere qui ragionamenti che è solo un fonte digitale)

Qui tutti i ragionamenti su quello che si trova su una fonte hi-res 

	Chatgpt (1)

	Chatgpt (2)

Poi mettere in mezzo USB audio player (cerca un modo per scaricare la maledetta app)

Cerca tutte le opzioni audio da ottimizzare nel momento in cui è stata attivata la modalità sviluppatore

Fai ricerca su Migliore equalizzatore per sony Xperia 1 III

Prendere il discorso di magari se vale la pena qualche cuffia

Mettere tutto insieme alle ricerchine audio fatte nel 2021

Iniziare a fare una sorta di database per ascolto audio di qualità in base agli ascolto provati con un google sheet dei file usati, I dettagli tecnici e cosa cercare in quell file

- Giorgio by Moroder (attorno ~07:00 ha un basso di una profondità e un attacco fantastici poi partono una serie di sintetizzatori)
