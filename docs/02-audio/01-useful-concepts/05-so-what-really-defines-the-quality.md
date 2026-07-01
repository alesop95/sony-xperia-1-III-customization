# So… what really defines the quality

Innanzitutto, va compreso che per audio compressi, il bitrate non è assolutamente sinonimo di qualità garantita. Per un file FLAC (ad esempio), il bitrate non è fisso: dipende dal livello di compressione e dalla complessità del segnale audio. Esempio:

Un brano con tanti silenzi o suoni semplici può occupare meno bitrate anche a 24bit/192kHz.

Un brano con dinamiche estreme, suoni complessi o molto “rumorosi”, può avere un bitrate più alto.

Inoltre, FLAC permette livelli di compressione diversi (da 0 a 8). Livelli più alti comprimono meglio (bitrate minore) ma richiedono più CPU in decodifica. La qualità audio è identica in ogni caso.

Quindi il bitrate diverso non significa per forza qualità diversa. Sono lo stesso identico master e la stessa qualità se provengono dalla stessa fonte, anche se occupano più o meno spazio.

For uncompressed audio, yes... a higher bitrate will pretty much always indicated a better potential sound than a lower bitrate. For example, regular CD audio, 44.1kHz at 16-bit in stereo is 1.4112 Mb/s. DAT was introduced as a slightly better format, 48kHz at 16-bit in stereo... 1.536Mb/s. When it's uncompressed, the bitrate is simply (sample_rate) * (sample_size) * (number_of_channels). So its easy to see that a higher bitrate could be a higher quality sound.

Once you start compressing audio, there are more variables. The particular compression CODEC you're using makes a difference.... a 256kb/s AAC file will probably sound much better than a 368kb/s MPEG Layer 2 file, simply because AAC uses a more advanced psychoacoustic model and more advanced compression algorithms. Some of it's dependent on the content... a 160kb/s variable bitrate AAC file could potentially sound better than a 256kb/s fixed-bitrate AAC file. You'd expect a 256Mb/s MPEG Layer 3 file to sound better than a 160Mb/s MP3 file, and when using the same CODEC and the same settings, it will.

But different encoders also produce better or worse compression... most of these algorithms, audio or video, specify the format, but not everything about how the format is created. So there's room for good and bad here... one example, the open source LAME encoder for MP3 has a reputation of producing noticeably better results than most commerically produced encoders. Similar claims are made of the x264 video encoder, versus many commercial AVC/H.264 encoders

[https://www.quora.com/Does-a-higher-sample-rate-audio-really-mean-better-quality](https://www.quora.com/Does-a-higher-sample-rate-audio-really-mean-better-quality)

Quindi, per audio invece compressi

**Non è questione solo del sample rate**: la qualità dipende soprattutto dalla **fonte originale** e dal **processo di mastering**. Dunque, prendendo ad esempio lo stesso file FLAC, un FLAC 24/88.2 derivato da un **remaster MoFi SACD** (che è un master di alta qualità in DSD) è probabilmente **migliore** di un FLAC 24/96 derivato da un upsampling di un CD standard (16/44.1). Anche se il 96 kHz è più “alto” come valore, la **qualità sonora reale dipende dal master originale** e dal metodo di conversione.

È il caso di Making Movies. Quel file FLAC 24/88.2 proviene da SACD, ma è in PCM per comodità e compatibilità ed è più pregiato del semplice FLAC 24/96 upsampled da CD. Difatti, au la fonte (e in generale nel file sharing) c’è un grosso rischio: file **upsamplati**. Alcuni utenti prendono un file a 16/44.1 e lo convertono a 24/192 solo per farlo sembrare “hi-res”. In questi casi:

Il file avrà **un bitrate più alto** solo perché ha più dati inutili.

Ma **non conterrà più informazioni audio** rispetto all’originale.

Per capire se il file è genuinamente high-res, si può:

- Guardare lo spettro con programmi tipo Spek o Audacity. Se sopra i ~22kHz non c’è nulla, è quasi sicuramente un file a 44.1kHz upsamplato. Si possono usare programmi semplici come:
   - Spek (facilissimo da usare - basta aprirlo e trascinare dentro il file FLAC e poi osservare lo spettrogramma)
   - Audacity (gratis, multipiattaforma)
   - Sonic Visualiser (più avanzato)
- Controllare il sito ufficiale dell’artista o le piattaforme come Qobuz o HDtracks per vedere se esiste davvero una versione high-res di quell’album

Se lo spettrogramma ha un taglio netto a 22 kHz, significa quasi sempre che il file proviene da un CD (44.1 kHz) e NON è vero high-res, anche se è stato “gonfiato” a 192 kHz. Se il grafico arriva oltre i 22 kHz, con informazioni presenti fino a 40-50-60 kHz (o oltre), è più probabile che sia davvero un file high-res - ma non è garanzia assoluta (potrebbe essere noise aggiunto).

FLAC è solo il contenitore/compressione lossless, non il formato nativo SACD (che è DSD).

recording at higher sample rates and downsampling, than directly recording at 22 Khz 16 bits.
Noise floor is not anymore a concern this days, just a little.

When recording to 192/24, downsampling at 22/16, you can hear a most ‘’complete’’ and detailed waveform, than if it were recorded initially at 22.5/16.

Try to record at 22.5/8 and see how it sounds. That resolution is too low to capture more ‘’frames’’ of sound.

Like in video or photography: a video it’s better looking at 60 fps than 20 fps. because it has more resolution.

Try to record video at 10 fps. It looks bad, you can see the actual frames one by one.

Listen to 8 bit music. You can hear the ‘’dots’’ of the digital domain. [https://www.quora.com/If-a-human-ear-can-hear-no-frequency-greater-than-20-kHz-and-we-need-no-more-than-40-kHz-sampling-rates-why-does-equipment-exist-that-plays-and-records-at-96-or-128-kHz-sample-rates](https://www.quora.com/If-a-human-ear-can-hear-no-frequency-greater-than-20-kHz-and-we-need-no-more-than-40-kHz-sampling-rates-why-does-equipment-exist-that-plays-and-records-at-96-or-128-kHz-sample-rates)

Vedere anche What’s the point in higher sample rates than 44.1kHz?

Hi-Res FLAC files (24-bit/96 kHz or higher) are technically superior to CD-quality FLAC files (16-bit/44.1 kHz) in terms of dynamic range and frequency response. Here are some key points to consider:

**Technical Differences**

**Bit Depth**:
- **24-bit** allows for a greater dynamic range (up to 144 dB) compared to **16-bit** (up to 96 dB). This means Hi-Res audio can capture quieter sounds and louder peaks more accurately.

**Sample Rate**:
- **96 kHz** (or higher) allows for capturing higher frequencies (up to 48 kHz) compared to **44.1 kHz**, which captures frequencies up to 22.05 kHz. This is important for certain types of music and sound design.

**Audibility of Differences**

**Hearing Differences**: Whether you can hear the difference between Hi-Res audio and CD-quality audio depends on several factors:

**Listening Environment**: A quiet, controlled environment may make it easier to notice differences.

**Equipment**: High-quality headphones or speakers and a suitable DAC (Digital-to-Analog Converter) can reveal the nuances of Hi-Res audio.

**Personal Sensitivity**: Individual hearing ability plays a significant role; some people may not perceive a noticeable difference, while others may.

**Conclusion**

While Hi-Res FLAC files offer technical advantages, the perceived difference in sound quality can vary widely among listeners. For casual listeners or in everyday settings, CD-quality audio may suffice, while audiophiles and professionals might prefer the enhanced fidelity of Hi-Res formats, especially for critical listening. [https://www.quora.com/Is-Hi-Res-FLAC-24-bit-96-khz-better-than-CD-quality-Flac-16-bit-44-1-khz-Can-you-hear-the-difference](https://www.quora.com/Is-Hi-Res-FLAC-24-bit-96-khz-better-than-CD-quality-Flac-16-bit-44-1-khz-Can-you-hear-the-difference)

Inoltre, va cercato su Qobuz, HDtracks, Bandcamp o altri store digitali se esiste DAVVERO una versione di quella combinazione <bit depth>, <sample rate>.

A volte si può anche controllare il DR (Dynamic Range)

## MoFi remaster

MoFi sta per Mobile Fidelity Sound Lab, un’etichetta storica molto famosa per le sue edizioni audiophile di album. Il remaster MoFi è una nuova versione rimasterizzata di un album, prodotta con cura estrema per migliorare la qualità sonora rispetto alle versioni precedenti (più dinamica, meno compressione, miglior dettaglio).

Ad esempio, per Making Movies e altri album, MoFi ha prodotto una Hybrid SACD con remaster DSD di alta qualità, considerata da molti audiofili la versione di riferimento.

Su una fonte o altri network si trovano spesso i rippaggi di questi remaster MoFi SACD, che sono in formato DSD nativo convertito in PCM (FLAC 24/88.2 o 24/96). Sono molto ricercati perché offrono una qualità superiore rispetto ai vecchi CD standard o ai semplici rippaggi 16/44.1.

## So what is “bad” is really “bad”??

Dal link [https://www.reddit.com/r/italy/s/igw0lQFn7b](https://www.reddit.com/r/italy/s/igw0lQFn7b)

![](assets/img-0005.jpeg)

Il mio setup consiste in un paio di HD490 Pro, Topping L30 e JCally JM6 Pro. Comunque un setup di tutto rispetto - uso Spotify.

Perché uso Spotify? Perché gli altri servizi pur avendo tecnicamente supporto lossless sono terribili.

Forse il migliore è Apple Music ma se non sei su Windows/macOS (es: Linux o semplicemente in un device non tuo quindi su web) ti attacchi per discorso DRM e ascolti a 256kbps. Non ha inoltre un supporto umano per [last.fm](http://last.fm/) che uso relativamente parecchio per espandere la mia libreria musicale e i miei gusti.

Passiamo a Tidal, che ho avuto per un paio di mesi. Amo la UI, ma è buggato a schifo, ogni tanto non riproduce qualcosa, si glitcha e la gestione della libreria risulta subpar per via delle 38 versioni dello stesso album che non vengono accorpate.

Spotify ha OGG Vorbis a 320kbps (non AAC) che nel 95% dei casi sono indistinguibili da CD Quality (.flac 16/24bit 44.1kHz). Il 99.9% delle persone facendo un test A/B non riuscirebbe a distinguere i due file.

Quello che OP sta descrivendo è semplicemente un placebo effect gigantesco per via delle piccole differenze di volume tra i due servizi in streaming (e per il fatto che big number = better)

Arriviamo inoltre al fatto che via Bluetooth non esiste in alcun modo una riproduzione lossless.
La maggior parte dei dispositivi bluetooth (Airpods Pro e anche le Max da 500 e passa euro), non supportano neanche LDAC che, pur non essendo lossless, risulta ottimo e bensì usano AAC limitato a 256kbps al posto dei classici 320kbps dei file MP3 (o OGG Vorbis come Spotify).

Ultimamente, Spotify just works for me - le playlist sono ben curate e la web UI funziona bene. Credo comunque sia uno UI mess strabiliante e sotto moltissimi aspetti di tale AM e Tidal vincono a mani basse. Basti pensare ai Canvas di Spotify che sono dei video in 144p orribili quando Apple Music ha le album cover animate con degli effetti spettacolari. Su Spotify se scorri troppo in basso c'è un jumpscare di TikTok e si trasforma in uno scroll to listen di cosa a caso. Veramente terribile, se aggiungi il fatto dei podcast ti viene da spararti. Detto ciò, credo rimanga comunque il migliore per via del fattore "just works" e per Spotify Connect che uso un sacco per controllare la riproduzione su PC comodamente dallo smartphone.

EDIT: Preferisco 1000 volte ascoltare un brano con un master di cristo come Hotel California in MP3 128kbps rispetto a qualsiasi altro master spazzatura in .WAV 32bit 192kHz. Se un brano è masterizzato male, non ci sarà lossless che lo farà splendere.

Che poi, i master ora sono di fatto realizzati per essere compressi (e riprodotti in condizioni pietose), la stereofonia viene aggiustata per non subire perdite in codifica, le frequenze vengono saturate/eccitate e poi limitate nello spettro (oltre a tutti gli accorgimenti per l'ampio range di ascolti diversi), si testa il clip digitale considerando già l'algoritmo di compressione.

Magari puoi comunque guadagnare della brillantezza o del dettaglio con i lossless, ma sarebbe un suono che praticamente non è neanche stato "calibrato" per l'ascolto, in quanto la priorità viene ovviamente data sicuramente ai file compressi, magari anche riprodotti nella cassa di qualche telefono o in qualche cuffietta marcia.

E i master vecchi che erano fatti per il vinile (ma anche i nastri non scherzano) erano pure peggio, combattevano proprio per far suonare bene il vinile in tutte le condizioni (altro che la qualità del vinile, vi piace solo la saturazione analogica), se fosse possibile riascoltarli "puri" in alta qualità senza il passaggio tra pressa vinili e lettore vinile, non renderebbero bene.

Impianto meno sofistico ma simile (dac su raspberry, ampli cambridge e casse indiana line) ed alla fine sono tornato anche io a Spotify anche perché il cambridge ha un ingresso bluetooth.

Ma prima mi sono fatto un abbonamento a tidal e mi sono tirato giù i flac di tutta una serie di album precisi e di cui conosco la qualità dei master (esempio i vari Pink Floyd remastered) e mi li sono messi sul nas (alla fine sono 7 tera di file, un paio di mesi di abbonamento ed uno script recuperato da GitHub e passa la paura), ma alla fine Spotify va ovunque, mi fa compagnia in macchina con CarPlay per i podcast e via così.

Così ho il meglio dei due mondi, musica ad alta qualità quando ho voglia di sbattermi ed assortimento nel resto del tempo. Fa cagare? Ma chissene, se voglio la musica buona ce l’ho per quei dischi a cui tengo davvero.

Premesso che 192kHz è solo marketing, visto che il 99,9% della musica è prodotta a 44,1kHz.

Il punto è se si riesce a distinguere un lossless da un mp3 320 kbit. In passato in doppio cieco sono riuscito a distinguere tidal da spotify, poi probabilmente hanno migliorato la codifica e ora posso dirti che non li distinguo più.

Posso dirlo nonostante abbia una catena audio pre onkyo + finale hypex + diffusori jbl ti10k in stanza dedicata e trattata acusticamente, quindi abbastanza rivelatore.

Ciao, io sono nell’hobby dell’audiofilia da qualche anno ormai, ti dirò: ormai sono convinto che non ci sia alcuna differenza percepibile dal mio sistema nervoso tra un 320 kbs e un 24/192. Utilizzo una combo topping A90/D90 e le Sennheiser HD800S che con l’equalizer di oratory1990 sono VERAMENTE spaziali [https://www.reddit.com/r/oratory1990/comments/1byez4l/how_damn_oratorys_eq_on_my_hd800s_have_made_them/?tl=it](https://www.reddit.com/r/oratory1990/comments/1byez4l/how_damn_oratorys_eq_on_my_hd800s_have_made_them/?tl=it). La differenza che noti è legata al fatto che la registrazione audio di partenza non è la stessa nei vari servizi di streaming, anche io noto subito una differenza tra i vari servizi, senza alcuna difficoltà; tuttavia, utilizzando la stessa fonte di origine questa differenza sparisce. Ti invito a fare questo test: scarica audacity, è un software per editing audio, ora scarica da archivio un album in 24/192 a tuo piacimento, scegli una canzone, metti una copia di questa canzone su audacity e convertila nei vari formati di qualità inferiore. Io facendo così e poi rinominando i vari files e sentendo in cieco facendo random shuffling non sono assolutamente in grado di percepire anche la più minima differenza, nemmeno una differenza insignificante, sono letteralmente identici. Esistono anche dei software che ti permettono di far partire i due files in maniera sincrona e di switchare subito da uno all’altro così è ancora più evidente che non ci sia alcuna differenza. E ti assicuro che col sistema audio che ho sento veramente tutti gli strumenti con una definizione pazzesca, sono i soldi meglio spesi della mia vita. Purtroppo, però tra FLAC e non flac non sento nessuna differenza e non credo di poterla biologicamente sentire.

Che post sterile. "La Lancia Delta è molto meglio di questa Panda Hobby del '98! Non capisco la gente come faccia! Io noto la differenza!". Il target di Spotify è diverso da quello di Tidal. Il costo è diverso, anche. La libreria a disposizione, anche. Che rant sarebbe, scusa? Tutti quelli che usano Spotify sono dei plebei? Anche io fui obliterato dalla qualità Tidal, ma con Spotify per 3€ al mese ho tutta la musica di sto cazzo di mondo. Se voglio qualità audiofila mi compro il CD. Fine. Ci sono mille sfumature per avere buona qualità di ascolto, e ti assicuro che con attrezzatura di livello alto puoi tirare fuori cose interessanti da Spotify. In sintesi, hai scoperto l'acqua calda.

Non sono un audiofilo, ma un musicista. Ascolto musica attraverso due monitor Yamaha HS80M (con cavi XLR) e la differenza tra un mp3 a 320kbps e un FLAC- su un buon master-si sente (maggiore limpidezza e distribuzione spaziale di alcune parti). Fa tutta questa differenza? Assolutamente no. La maggior parte delle persone la sentirebbero? No. Se ne può fare a meno? Sicuro. Però è piacevole.

Perfetto, proviamo un approccio un minimo scientifico perché io rimango scettico sul fatto che si riesca effettivamente a sentire la differenza.

Qui ([https://abx.digitalfeed.net/spotify-hq.html](https://abx.digitalfeed.net/spotify-hq.html)) mi sembra di aver trovato un bel test in cieco per vedere se si riesce a distinguere un formato lossless dalla versione di Spotify a 256kbps (manco a 320kbps).

Più tardi la provo anche io e posto i risultati, che prevedo saranno deludenti per le mie orecchie (ascolto su un paio di Yamaha HS8 da scheda audio Focusrite 18i20).

Chi dice/pensa di poter distinguere un FLAC da un MP3 a 320kbps è moralmente obbligato a fare il test e postare i risultati (niente multi-try finché non ti viene fuori la risposta che volevi eh…)

Ricordiamoci sempre della sacra sinusoide [https://archive.org/details/sinusoidetdc](https://archive.org/details/sinusoidetdc)
