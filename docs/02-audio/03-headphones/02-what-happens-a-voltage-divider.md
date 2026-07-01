# What happens… a voltage divider!

L’impedenza di una cuffia è una misura della resistenza elettrica che il driver della cuffia oppone al segnale audio che gli viene fornito, espressa in ohm (Ω). Le cuffie ad alta impedenza (tipicamente 250 Ω, 300 Ω, anche fino a 600 Ω) richiedono più tensione per muovere i driver. Quelle a bassa impedenza (32 Ω, 16 Ω) sono più facili da pilotare, cioè richiedono meno potenza elettrica.

Quando colleghi una cuffia a una sorgente, stai creando un partitore di tensione resistivo/impedenziato:

Dove:

- : tensione in uscita dalla sorgente (DAC, ampli, dello stadio driver finale ecc…)
- : impedenza d’uscita della sorgente (amplificatore)
- : impedenza delle cuffie (carico)

Ad esempio, se la sorgente ha un'impedenza d'uscita non trascurabile (es. 10 Ω), si crea una perdita di tensione significativa con delle cuffie a bassa impedenza. Dalla formula sopra, il rapporto diventa 0.76, ovvero si ha il 76% della tensione disponibile. 

Delle cuffie ad alta impedenza (es. 300 Ω), prendendo la stessa formula, si ha il 97§% della tensione disponibile. Il comportamento è più lineare, minore distorsione causata dalla sorgente, maggiore compatibilità con amplificatori di qualità non eccelsa.

Dunque, una cuffia ad alta impedenza è più robusta a sorgenti con alta impedenza d’uscita perché l’attenuazione del segnale dovuta al partitore di tensione è minore quanto maggiore è l’impedenza della cuffia rispetto all’impedenza d’uscita dell’amplificatore. In altre parole, una cuffia ad alta impedenza è meno influenzata da un'alta impedenza di uscita della sorgente.

Inoltre, se  varia in funzione della frequenza (comune nei circuiti analogici), anche  varia con conseguente colorazione del suono, distorsione di frequenza. Il partitore attenuerebbe allo stesso modo a tutte le frequenze se i valori fossero costanti. Ma nei circuiti analogici reali,  non è puramente resistiva: è una funzione della frequenza a causa di componenti reattivi (induttanze parassite, condensatori di accoppiamento, reti di feedback non ideali, ecc.). Pertanto, la formula sopra può essere pensata come:

Con:

Ne consegue che la tensione in uscita non sarà in generale piatta su tutto lo spettro e la risposta in frequenza viene alterata e si introduce una colorazione del suono (enfasi o attenuazione su alcune bande). Dunque, la colorazione in questo contesto è una variazione indesiderata nella risposta in frequenza dovuta all’interazione tra l’impedenza di uscita dell’amplificatore  e l’impedenza del carico, cioè della cuffia .

Una cuffia ad alta impedenza (es. 300 Ω) rende la frazione quasi costante, anche se  è variabile in frequenza, dando comunque una risposta più lineare. Se invece  ha variazioni di impedenza con la frequenza (cosa normale nelle cuffie dinamiche, per effetto della risonanza del driver e del contenuto reattivo del carico), e  NON è trascurabile, allora la tensione risultante applicata al driver non non segue più fedelmente il segnale sorgente. Questo risulterebbe non in un’attenuazione lineare (cioè uguale su tutte le frequenze), ma una modulazione selettiva con conseguente colorazione (indesiderata) del suono. In un certo senso, quindi, più la cuffia è ad alta impedenza più è in grado di isolare il problema, perché se , anche se  varia, l’effetto è fortemente limitato perché la frazione sopra è approssimabile ad 1 e la tensione trasferita risulta comunque quasi identica su tutte le frequenze: anche se la sorgente non ha impedenza piatta o bassa, l’impatto sulla risposta è minimo.

Per questo motivo le cuffie ad alta impedenza sono meno sensibili alla qualità dell’amplificatore (in termini di impedenza di uscita). Non perché siano “migliori”, ma perché sono più tolleranti a una sorgente imperfetta.

Esempi noti di cuffie con impedenza commerciale (valore nominale):

- Sennheiser HD600 / HD650 — tipicamente 300 Ω
- Beyerdynamic DT 880 (250 Ω)
- Sennheiser HD800 — 300 Ω

Questi modelli sono ampiamente utilizzati in contesti dove vengono effettuate misure THD+N e, talvolta, IMD in laboratori indipendenti. Tuttavia, i dati precisi di Bl(x), Kms(x) non sono pubblicati.

## A good quality amplifier

In ogni caso, l’impedenza d’uscita non è soltanto ciò che definisce la “qualità” di un amplificatore perché può essere considerato un indice critico per l’adattamento di carico. Un amplificatore può essere perfettamente lineare, basso rumore, alta dinamica — ma se ha un’impedenza d’uscita elevata, colorerà il suono quando lavora con carichi variabili (come le cuffie). Il concetto chiave è il fattore di smorzamento (damping factor):

Maggiore è il fattore di smorzamento, più l’amplificatore controlla il carico (cuffia o altoparlante), “dominandolo” quindi elettricamente e controllandone le variazioni. Anche qui bisogna tenere in considerazione che le impedenze non sono ideali/resistive nella realtà e quindi si ha:

Dunque, se  cambia come ad esempio nel caso di picchi di impedenza a causa di risonanze acustiche del driver, e  non è trascurabile, quel rapporto cambia su ogni frequenza. In questo caso, il segnale viene trasferito in modo non uniforme, anche se l’ampli è perfettamente lineare *in tensione* e questo è il punto centrale del concetto di “colorazione”: modifica involontaria della risposta in frequenza dovuta al carico.

### Example

Supponiamo un esempio con dei valori pratici plausibili. Ad esempio, se un DAC ha un’uscita  di 70Ω e una cuffia ha una impedenza  non troppo alta di 32Ω ma con un picco a 70Ω sui 3kHz dovuto alla risonanza di quel driver, questo cambia il damping factor a quella frequenza (attorno a) e Il trasferimento di segnale cambia con la frequenza, e quindi l’SPL (sound pressure level) generato dalla cuffia cambia anche a parità di tensione di ingresso. Questo significa che il DAC non è neutro in uscita e la cuffia non suona come dovrebbe. 

Ingegneristicamente, nei DAC/ampli di alta qualità, si mira a < 1Ω  per avere un DF > 100 anche con cuffie da 100Ω e assumere virtualmente questo “trasferimento” costante. I DAC quelli un po' più “consumer” o da smartphone spesso hanno 10-30 Ω e su cuffie da 32Ω - 50Ω la risposta è influenzata. 

## More on DACs and amplifiers

### Typical components inside and why they are crucial

In un DAC/amplificatore non ideale, troviamo principalmente tre componenti che giocano un ruolo chiave per quanto detto finora:

1. Stadio d’uscita op-amp + resistore in serie
   1. Molti DAC hanno stadi d’uscita con un'op-amp e una resistenza di uscita esplicita (es. 10–100 Ω). Serve come protezione contro corto circuito o carichi instabili e stabilità dell’ampli op-amp (soprattutto se è un current-feedback) e persino come attenuazione di ringing su cavi lunghi o carichi reattivi.
   1. Questo resistore rappresenta la parte spesso puramente resistiva di  (ovvero ) e non trascurabile

Questa è la componente dominante di   e la più prevedibile, ma non l’unica. L’intera impedenza totale del circuito varia comunque con la frequenza, anche se una parte è costante, e le altre componenti di impedenza () derivano da quanto segue. 

1. Capacitori di accoppiamento
   1. Spesso ci sono condensatori in serie per bloccare la DC offrendo un’impedenza capacitiva alle basse frequenze:
- Vedere l’impatto nell’esempio corrispondente.
1. Induttanza parassita del cablaggio/stadio di uscita (PCB, pinout, tracce)
   1. A frequenze alte (>20 kHz), le induttanze parassite introducono un aumento di  con attenuazione degli alti su cuffie molto sensibili

Altri componenti reattive dell’impedenza possono derivare da eventuali reti di filtro interne.

#### Example

Supponiamo un esempio vediamo l’effetto dell’accoppiamento AC tramite condensatore in uscita che è molto comune in DAC portatili o smartphone. Il circuito equivalente con un condensatore di uscita  (in serie) e una cuffia resistiva  o  è un filtro passa-alto del primo ordine, con frequenza di taglio:

Facendo qualche piccolo esempio numerico, con una = 32Ω e considerando un valore tipico per un condensatore  = 47F, la frequenza di cut-off descritta sopra è attorno ai 106Hz con un *percepibile* risultato di bassi attenuati sotto i 100Hz. Se si collegasse invece una cuffia da 300Ω, la stessa frequenza risulterebbe essere di circa 11Hz cadendo persino nel range non-udibile. La situazione semplificata può essere descritta dal seguente grafico:

![](assets/img-0006.png)

Che mostra chiaramente come la cuffia da 32 Ω subisca un taglio più alto nei bassi (~106 Hz), mentre quella da 300 Ω mantiene una risposta piatta fino a ~11 Hz, a parità di condensatore d’uscita (47 µF).

### Balanced signals

In headphones amps is usually used the balanced output. Balanced output means the amplifier uses two separate signal lines per channel instead of one, and a shared ground is eliminated or separated.

Technically speaking, differently from the unbalanced output (single-ended - SE) whose signal path per channel is 1 hot (signal) wire and 1 ground wire shared between left and right, the balanced output has:

- 1 hot (+) wire
- 1 cold (–) wire, which carries the inverted signal
- Ground is either separate or handled differently

This way, the headphone driver receives both the normal and inverted signals. Because the cold line carries an inverted copy of the signal, any noise or interference picked up along the cable is canceled out (common-mode rejection - CMRR). This means cleaner audio, especially with long cables or electrically noisy environments.

So, in a “standard” (single-Ended) wiring in headphones one wire carries the audio signal (+) and one wire is ground (–), shared by both left and right drivers:

    +-------------+             +------------+
    | Amplifier   |             | Headphone  |
    | Left Out +--|-------------| Left Driver|
    | Ground ----|-------------| Shared GND  |
    | Right Out -|-------------| Right Driver|
    +-------------+             +------------+

The signal goes from amp hot then to the driver and returns via ground. Both drivers share the same ground wire.

In the balanced configuration, each driver has two separate wires: a positive (+) and a negative (–) signal with no shared ground between left and right:

    +------------------+                   +-------------------+
    | Balanced Amp Out  |                   | Balanced Headphone |
    | Left + -----------|-------------------| Left Driver +     |
    | Left – -----------|-------------------| Left Driver –     |
    | Right + ----------|-------------------| Right Driver +    |
    | Right – ----------|-------------------| Right Driver –    |
    +------------------+                   +-------------------+

The negative wire carries an inverted copy of the positive signal, so the driver receives a *differential signal*. The driver coil sees a larger voltage swing because the amp is pushing one wire positive and the other negative simultaneously. This creates twice the voltage difference, leading to higher power output and better control.

Moreover, balanced amps can deliver almost double the voltage swing compared to single-ended for the same supply voltage. This usually means more power available for demanding headphones (like high impedance or low sensitivity) and better driver control, tighter bass, more dynamic range. Since the left and right channels are completely separated, stereo separation can also improve because of crosstalk reducing. 

Physically a balanced headphone cable uses special connectors like:

- 4-pin XLR
- 4.4mm Pentaconn (increasingly popular for portable DAC/amps)
- ![](assets/img-0007.png)
- 2.5mm TRRS (less common but present in smaller portable amps)
- ![](assets/img-0008.png)

while unbalanced typically uses 3.5mm TRS and 6.3mm TRS (single-ended plug). Some headphones come with balanced cables with 4 wires inside (two per driver, positive and negative). Others only support single-ended.

Balanced output often improves power and noise floor, but sound quality depends on the amplifier design, headphone compatibility, and synergy. Many high-end DAC/amps provide balanced outputs to maximize power and reduce noise, essential when driving high-impedance headphones that need more voltage and cleaner signals.

Furthermore, the Sony Xperia 1 II via USB-C supports USB Audio Class 2, which can pass high-res signals to DACs that leverage balanced output for superior fidelity.
