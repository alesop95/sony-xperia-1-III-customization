# Analisi spettrale per l'autenticita' di un file audio - metodo

> Documento di metodo per lo strumento `tools/audio/spectral-audit.py`. Descrive il modello di
> segnale, gli indicatori misurati e i loro limiti, al livello di dettaglio utile a un lettore con
> formazione in signal processing. Complementa `track-benchmark.py`, che ragiona su metadati e
> dimensione, aggiungendo la misura diretta sul contenuto dei campioni, che e' la prova definitiva.

## Il problema e i due falsi

Un contenitore FLAC dichiara un formato (frequenza di campionamento Fs, profondita' di bit N,
canali) nei suoi header, ma gli header si possono scrivere a piacere. Le due falsificazioni comuni
sull'usato e sul file sharing sono l'hi-res fasullo per upsampling e la profondita' di bit gonfiata.

Nel primo caso il file dichiara, per esempio, 96 kHz, ma il materiale proviene da una sorgente a
44.1 o 48 kHz risamplata verso l'alto. L'upsampling non crea informazione: la banda tra la vecchia
e la nuova frequenza di Nyquist[^nyq] resta vuota, riempita solo dall'interpolazione, e nello
spettro medio l'energia collassa nel rumore ben prima della nuova Fs/2. Nel secondo caso il file e'
un contenitore a 24 bit i cui campioni usano di fatto solo i 16 bit piu' significativi, cioe' un 16
bit impacchettato in 24 senza guadagno reale di gamma dinamica.

Un terzo caso, affine al primo per firma spettrale, e' la transcodifica lossy mascherata: un MP3 o
AAC ridecodificato e reincapsulato in FLAC. La codifica percettiva ha gia' rimosso l'alta frequenza
con un taglio netto, un brickwall, che sopravvive alla riconversione e resta visibile.

## Modello di segnale

Il campionamento a frequenza Fs rappresenta senza perdita solo componenti sotto la frequenza di
Nyquist, `f_max = Fs / 2`. Un contenuto genuino a 96 kHz puo' contenere energia fino a 48 kHz; se
l'energia finisce a 20 kHz, la scelta di Fs non e' giustificata dal materiale.

La profondita' di bit N fissa il rumore di quantizzazione e quindi la gamma dinamica teorica. Per
un segnale sinusoidale a fondo scala vale la relazione nota

    SNR[dB] ≈ 6.02 * N + 1.76

quindi circa 96 dB a 16 bit e circa 144 dB a 24 bit[^snr]. Un file che dichiara 24 bit ma porta un
segnale con risoluzione effettiva a 16 bit non offre alcuno di quei circa 48 dB in piu': i bit
bassi sono costantemente a zero.

## Gli indicatori misurati

### Densita' spettrale di potenza media (Welch)

Lo strumento stima lo spettro medio del brano con il metodo di Welch: il segnale mono, ottenuto per
somma dei canali, viene diviso in segmenti sovrapposti al 50 per cento, ciascuno moltiplicato per
una finestra di Hann, trasformato con la rFFT e ridotto al modulo quadro; i moduli quadri si mediano
sui segmenti. La media riduce la varianza della stima in proporzione al numero di segmenti, cosa che
una singola FFT sull'intero brano non farebbe, restituendo uno spettro rumoroso. La finestra di Hann
contiene la dispersione spettrale[^leak] a scapito di una risoluzione leggermente inferiore, con
larghezza di banda equivalente di rumore di circa 1.5 bin. La risoluzione in frequenza e'
`Δf = Fs / Nfft`; con la finestra predefinita di 16384 campioni a 96 kHz vale circa 5.9 Hz, piu' che
sufficiente a localizzare un cutoff.

L'analisi non gira sull'intero file ma su un estratto centrale di durata limitata (120 s di
default), per contenere la memoria e per evitare intro e dissolvenze poco rappresentative.

### Cutoff come rolloff percentile

Il cutoff effettivo, cioe' la frequenza oltre cui non c'e' piu' contenuto significativo, e' stimato
come rolloff percentile: la frequenza sotto cui si concentra il 99.9 per cento dell'energia della
PSD. Si preferisce questa stima al semplice massimo bin sopra una soglia in dB perche' quest'ultima
e' fragile, un singolo bin di rumore in alta frequenza sopra soglia sposterebbe il cutoff fino a
Nyquist. Il rolloff cumulato e' robusto a questi picchi isolati e coglie dove finisce davvero il
grosso dell'energia. Il valore si legge poi in rapporto a Fs/2: un contenuto genuino ad alta Fs
arriva vicino alla propria Nyquist, un upsampling si ferma molto prima.

### Frazioni di energia in banda

Lo strumento riporta la frazione di energia totale nelle bande sopra 20 kHz e sopra 22.05 kHz.
La soglia di 22.05 kHz e' la frequenza di Nyquist del CD: energia genuina oltre quel valore e'
la firma di un contenuto realmente esteso oltre la banda del Compact Disc. La sua assenza in un
file dichiarato a 96 o 192 kHz e' un forte indizio di sorgente a 44.1 kHz.

### Profondita' di bit reale

I campioni interi vengono combinati con un OR bit a bit su tutta la selezione; il numero di bit
meno significativi[^lsb] costantemente a zero da' i bit inutilizzati, e la differenza rispetto
all'ampiezza del contenitore da' la risoluzione effettiva. Un contenitore a 24 bit con contenuto a
16 bit mostra otto o piu' bit bassi sempre nulli. Il test vale per i sottotipi PCM interi; per i
formati in virgola mobile non e' applicabile e viene omesso.

## Logica di verdetto e soglie

I criteri sono deterministici e documentati.

| Condizione misurata | Verdetto |
|---|---|
| Fs > 48 kHz e cutoff < 22.5 kHz | sospetto upsample: contenuto limitato alla banda del CD |
| cutoff vicino (±0.4 kHz) a 16/17.5/19/20/20.5/21/22.05 kHz e cutoff < 0.97·Nyquist | cutoff tipico di transcodifica lossy, da confermare a vista |
| energia oltre 22.05 kHz < 1e-4 con Fs > 48 kHz | nessun contenuto ultrasonico genuino |
| contenitore PCM_24 con risoluzione effettiva ≤ 16 bit | profondita' gonfiata |
| Fs > 48 kHz, cutoff ≥ 0.9·min(Nyquist, 24 kHz) ed energia oltre 22.05 kHz ≥ 1e-4 | coerente con hi-res autentico |

## Limiti, dichiarati esplicitamente

La misura sui campioni e' la prova piu' forte, ma non e' infallibile e va letta con giudizio.
Alcune registrazioni genuine hanno poca energia in alta frequenza per ragioni di strumentazione,
microfonaggio o scelte di produzione: un cutoff basso non implica sempre una frode. Il segno piu'
affidabile di transcodifica lossy resta la forma del taglio, un brickwall netto, piu' che la sua
sola posizione; questa distinzione tra taglio netto e rolloff graduale si apprezza meglio a vista,
per cui lo spettrogramma resta un complemento necessario. Un dither con noise shaping aggressivo
puo' alzare il rumore in alta frequenza e mascherare parzialmente un cutoff o simulare contenuto;
va tenuto presente. Infine, un file puo' aver subito piu' passaggi, per esempio lossy seguito da
upsampling, che sommano piu' firme.

Per questo lo strumento produce anche un PNG dello spettrogramma e rimanda all'ispezione visiva.

## Strumenti

Lo script `tools/audio/spectral-audit.py` esegue la misura quantitativa e genera lo spettrogramma.
Dipende da `numpy` e `soundfile` per la decodifica di FLAC, WAV e AIFF, e da `matplotlib` per il
solo PNG. Installazione delle dipendenze a livello utente:

```powershell
python -m pip install --user numpy soundfile matplotlib
```

Esempi d'uso:

```powershell
python tools/audio/spectral-audit.py traccia.flac
python tools/audio/spectral-audit.py traccia.flac --png spettro.png --seconds 90
python tools/audio/spectral-audit.py traccia.flac --no-plot
```

Per l'ispezione visiva rapida e interattiva resta ottimo Spek, open source e multipiattaforma, che
mostra lo spettrogramma con la scala di colori utile a cogliere i tagli netti. In alternativa da
riga di comando, SoX con `sox in.flac -n spectrogram` e FFmpeg con il filtro `showspectrumpic`
generano immagini equivalenti. Lo strumento di questo progetto aggiunge a quelli la misura numerica
e il verdetto automatico, e si integra con `track-benchmark.py`: quest'ultimo dice se la dimensione
del file e' plausibile per il formato dichiarato, questo dice se il contenuto reale lo giustifica.

[^nyq]: *Nyquist* - la massima frequenza rappresentabile senza aliasing e' meta' della frequenza di
campionamento; oltre quella soglia un campionamento non porta informazione.

[^snr]: *SNR*, Signal to Noise Ratio - rapporto segnale rumore; la formula lega la gamma dinamica di
quantizzazione al numero di bit per un segnale a fondo scala.

[^leak]: *dispersione spettrale*, spectral leakage - diffusione dell'energia di una componente su
bin adiacenti dovuta al troncamento del segnale; le finestre come la Hann la riducono.

[^lsb]: *LSB*, Least Significant Bit - bit meno significativo del campione; se i bit bassi sono
sempre nulli, la risoluzione effettiva e' inferiore all'ampiezza del contenitore.
