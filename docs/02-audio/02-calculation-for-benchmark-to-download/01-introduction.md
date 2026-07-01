# Introduction

su una fonte hi-res, dall’app non ufficiale di Android scaricata da APKPure, quello che viene indicato con “speed” è invece la combo bit depth/sample rate.

However, the final bitrate ALWAYS depends on the music content and the compression level chosen. The more complex or noisy music is, the higher the bitrate.

Ecco **valori realistici** (bitrate medio **in kbps**) per un FLAC **stereo** in base a risoluzione e frequenza di campionamento, considerando musica “normale” (rock, pop, jazz, classica).

Nota: il bitrate finale dipende SEMPRE dal contenuto musicale e dal livello di compressione scelto. Più musica è complessa o rumorosa, più il bitrate sale.

**Valori realistici**

**16 bit / 44.1 kHz (CD Quality)**

WAV (non compresso): **1411 kbps**

Calcolo bitrate WAV:

44.100×16×2=1.411.200 bps=1411 kbps44.100 x 16 x 2 = 1.411.200 \text{ bps} = 1411 \text{ kbps}44.100×16×2=1.411.200 bps=1411 kbps

FLAC compresso:

 **600 - 1000 kbps**
(≈ 30-60% di compressione possibile)

molto compresso: **500 kbps**

**24 bit / 48 kHz**

WAV (non compresso): **2304 kbps**

Calcolo bitrate WAV:

48.000×24×2=2.304.000 bps=2304 kbps48.000 x 24 x 2 = 2.304.000 \text{ bps} = 2304 \text{ kbps}48.000×24×2=2.304.000 bps=2304 kbps

FLAC compresso:

tipico: **1000 - 1700 kbps**

**24 bit / 96 kHz**

WAV (non compresso): **4608 kbps**

Calcolo bitrate WAV:

96.000×24×2=4.608.000 bps=4608 kbps96.000 x 24 x 2 = 4.608.000 \text{ bps} = 4608 \text{ kbps}96.000×24×2=4.608.000 bps=4608 kbps

FLAC compresso:

tipico: **2200 - 3500 kbps**

**24 bit / 192 kHz**

WAV (non compresso): **9216 kbps**

Calcolo bitrate WAV:

192.000×24×2=9.216.000 bps=9216 kbps192.000 x 24 x 2 = 9.216.000 \text{ bps} = 9216 \text{ kbps}192.000×24×2=9.216.000 bps=9216 kbps

FLAC compresso:

tipico: **4500 - 7000 kbps**

minimo accettabile (musica molto semplice): ~3500 kbps

**Quindi:**

**Regola pratica**

 **Un FLAC 24/192 sotto 3000 kbps è quasi sempre sospetto** (fake upsample o metadati falsi).
 **Un FLAC 24/96 sotto 1500 kbps è sospetto.**
 **Un CD rip in FLAC (16/44.1) tra 600-1000 kbps è normalissimo.**

Come fanno allora su una fonte hi-res ad esistere diverse versioni dello stesso album (ad esempio Random Access Memories dei Daft Punk) tutte versioni flac da 24bit e 96kHz ma allo stesso tempo avere bitrates differenti ma tutto l'album nel complessivo pesare uguale (in termini di Gb o Mb)? Quando su una fonte hi-res (o altrove) vedi **più versioni dello stesso album FLAC 24bit/96kHz** che:

hanno **bitrate medi diversi** (es. 3.000 kbps, 3.500 kbps, ecc.),

ma **hanno lo stesso peso complessivo in MB o GB**,

è quasi sempre perché il **bitrate riportato** è una stima calcolata dai player o dai tag del file, ma non sempre riflette una differenza reale nei dati. Ecco perché succede:

Questo è coerente con quanto è stato spiegato nella sezione FLAC. Abbiamo visto che il bitrate del FLAC è variabile per come intrinsecamente funziona e non ne impone uno fisso come MP3
