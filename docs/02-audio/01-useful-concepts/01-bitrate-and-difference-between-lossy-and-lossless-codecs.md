# Bitrate (and difference between lossy and lossless codecs)

A parità di **profondità di bit** (bit depth) e **frequenza di campionamento** (sample rate), i **kbps** (kilobit per secondo) ti danno una misura della **quantità di dati trasmessi o memorizzati per secondo** nel file audio. Più precisamente:

La **profondità di bit** indica quanti bit vengono usati per rappresentare ogni singolo campione audio (es. 16 bit, 24 bit).

La **frequenza di campionamento** indica quanti campioni vengono presi ogni secondo (es. 44.1 kHz, 48 kHz).

I **kbps** indicano la **velocità di trasmissione dati** O il **bitrate**: in generale quanti bit vengono usati per secondo per codificare l'audio.

Se profondità di bit e frequenza di campionamento sono fissi, allora il bitrate (kbps) è determinato da questi due valori **moltiplicati per il numero di canali**. La formula per il bitrate in kbps in un file PCM (Pulse Code Modulation) non compresso è:

Dove:

- : è il bitrate in kbps (kylobyte per second)
- : la frequenza di campionamento [Hz]
- : è il numero di canali (per un segnale stereo, quindi quel formato master specifico, sempre 2)

Quindi, i kbps in questo contesto ti dicono quanta quantità di dati per secondo è necessaria per rappresentare quell'audio con quella qualità.

In un algoritmo di compressione lossless, se anche si hanno due file FLAC con la stessa profondità di bit (let’s say 24 bit) e frequenza di campionamento (192 kHz), il bitrate può variare da un file all'altro. Se invece il file è compresso con un algoritmo lossy (es. MP3, AAC), i kbps indicano la quantità di dati usata per la compressione, quindi la qualità e la dimensione finale del file.

Sticking for the moment in the context of bitrate with lossless compression algorithms, for instance, FLAC uses variable bitrate (VBR) compression, meaning its bitrate adjusts dynamically based on the complexity of the audio. Unlike constant bitrate (CBR) formats like MP3, the kbps value in a FLAC file represents an average rather than a fixed rate. This allows FLAC to maintain the same lossless audio quality regardless of bitrate variations, as the compression efficiency adapts to the content without affecting fidelity.

But before explaining what a lossless compression algorithm means, let’s dive into what does it mean to lose some audio information instead and stanardized way in which this is done, basically fooling our ears in a clever way. 

## MP3

MP3's (more correctly *MPEG1 or MPEG2 Audio Layer III) files mostly start with a red book audio track, like an audio CD track. This means, as per Red Book standard, which defined how audio must be stored, that sampling rate is 44.1kHz, 16-bit resolution, 2-channels (stereo) and maximum duration of 74-80 minutes. The data format was uncompressed linear PCM. So, up to “now” no compression, just PCM data burned onto a CD. 

THEN a lossy. data compression algorithm is applied to the PCM digital file.
The intent is to reduce the files size by throwing away data (loss) but still leave enough to produce a sound that an average listener would consider faithful to the original.

Anche se gli MP3 (MPEG-1 o MPEG-2 Audio Layer III) sono un formato compresso, molti file MP3 iniziano con informazioni che simulano o sono compatibili con la struttura del Red Book, per facilitare la compatibilità con lettori che supportavano originariamente solo CD audio. Oppure, più precisamente, gli MP3 derivano spesso da tracce estratte da CD Red Book; quindi, mantengono certe caratteristiche (come il campionamento a 44.1 kHz e stereo a 16 bit).

MP3 is a lossy encoding which exploits many things like:

- Psychoacoustic model: removes sounds the human ear can’t perceive (like very quiet background details masked by louder ones).
- Transformation: converts the signal to frequency domain using methods like MDCT (Modified Discrete Cosine Transform).
- Quantization: reduces the precision of less important frequencies.
- Huffman coding: Uses entropy coding to further reduce size.

A lossy MP3 file is small in size, but, of course, with some quality loss. Since PCM files are large (~10MB or more per minute), back in the early digital days when storage limitations did matter more than nowadays it was a good compromise. 

More in “details”, the MP3 codec (compress/decompress) methodology relies on the psychoacoustic phenomenon of temporal auditory masking where generally lower tones mask higher tones. MP3 compression removes sounds that are masked by louder sounds occurring just before or after them, reducing file size without noticeably affecting audio quality.

Because MP3 compression uses a continual, perceptual transform coding approach, it does not create digital audio with fixed bit depths and sample rates, like raw PCM data. Instead they use a *target bit rate* (because “here” priority is size shrinking) and continuously apply any of several strategies for data loss, depending on the frequencies present in the changing audio to meet the target data rate.
At 128k bits per second, a digital audio file will be about 1/11th the size of the original PCM file, with some noticeable loss [https://www.quora.com/Does-a-higher-sample-rate-audio-really-mean-better-quality](https://www.quora.com/Does-a-higher-sample-rate-audio-really-mean-better-quality).

The common sample rates used by lossless digital audio files are 44k, 96k, and 192k (and 48k for the audio on videos). However the numbers 128k, 256k, and 320k are still reserved for lossy files like MP3 and AAC. Because of the explanation above, the numbers used for MP3 and AAC are bit rates, which are something else entirely than sample rate [https://www.quora.com/If-a-human-ear-can-hear-no-frequency-greater-than-20-kHz-and-we-need-no-more-than-40-kHz-sampling-rates-why-does-equipment-exist-that-plays-and-records-at-96-or-128-kHz-sample-rates](https://www.quora.com/If-a-human-ear-can-hear-no-frequency-greater-than-20-kHz-and-we-need-no-more-than-40-kHz-sampling-rates-why-does-equipment-exist-that-plays-and-records-at-96-or-128-kHz-sample-rates). 

About how much MP3 affects *perceived* sound quality, the answer is all down to our perspective on sound quality. Spotify’s “very high” quality is normally taken to be equivalent to 320kbps MP3. For the music played on Spotify, the original audio source is in CD format, which has an inherent streaming bandwidth of 1,411kbps. Qobuz, for example, will stream at the full 1,411kbps - and can even stream higher than that if the original audio track was recorded in a higher-than-CD resolution format. And TIDAL does too. In fact, what really defines the quality is especially from the original source and the mastering process.

The MP3 format (and similar formats like AAC, OGG Vorbis, etc) is a system for compressing music files so that they take up less space and can be streamed using less bandwidth. This zipping-up process can actually be done in such a way that the music can be stitched back together again at the receiving end as an exact copy of the original audio file. But in order to maintain that quality you end up being limited by how much you can reduce the file size or streaming bandwidth. You can reduce them by about 40–50%, but rarely any more. That is what FLAC does - usually referred to as a “*lossless compression*” format. MP3 goes one step further with compression because it starts throwing away bits of the music that it thinks you either can’t hear, or *don’t need to hear*. Most MP3 files (such as what you likely hear on a radio) are even typically around 128kbps, and have thrown away a good 80% of the original music file since is a “*lossy compression*”. In this sense MP3 is very smart about which bits of the music it *throws away* and a casual listener probably wouldn’t even care that something is missing. We can think of MP3 in a figurative way as follows. If we try to read this message:

“Th d, f crs, s tht MP3 s vry, vry smrt bt whch bts f th msc t thrws wy. Th nd rslt s tht a csl lstnr prbbly wldn’t vn cr tht smthng s mssng. nd t 320kbps t tks a srs d plybck systm to rndr ths dffrncs dbl.”

we can probably read that reasonably well, and reconstruct in our mind enough of what the message is originally meant to communicate, and if that was all that mattered. But if all that squinting at the screen gives a little bit a headache, and the same applies for our brain when trying continuously to reconstruct the entirety of our audible message [https://www.quora.com/Is-Hi-Res-FLAC-24-bit-96-khz-better-than-CD-quality-Flac-16-bit-44-1-khz-Can-you-hear-the-difference](https://www.quora.com/Is-Hi-Res-FLAC-24-bit-96-khz-better-than-CD-quality-Flac-16-bit-44-1-khz-Can-you-hear-the-difference).

## FLAC

We’ve seen that MP3 files are small because they are compressed and this compression basically works by tossing data we are not supposed to hear: with a *bitrate* of 320kbps, an mp3 file will keep everything we can hear, tossing very few data which we wouldn’t have noticed anyway. But the reason why some people prefer FLAC or some other lossless file is because it literally has *all the data*. In this sense, FLAC compresses the audio to reduce file size, but can be decompressed back to the exact original data. For example, FLAC has a nice feature: if all the bottom bits of, say, 512 samp[les, are all zero, then those bottom bits are not encoded by FLAC and put in later. In lossyWAVE, the audio is analysed to find the least number of bits used. That is noise in that recording segment and can be inaudibly set to zero. When this is done, FLAC will compress it 30%-40% better [https://www.quora.com/Is-Hi-Res-FLAC-24-bit-96-khz-better-than-CD-quality-Flac-16-bit-44-1-khz-Can-you-hear-the-difference](https://www.quora.com/Is-Hi-Res-FLAC-24-bit-96-khz-better-than-CD-quality-Flac-16-bit-44-1-khz-Can-you-hear-the-difference).

However, FLAC allows to achieve same identical quality to WAV, but with smaller file size (~30-60% less) although may not be supported by all devices/players. See also the clarification about codec and containers format and how it applies to FLAC in the section below.

FLAC is a compressed lossless format: although the audio quality (bit depth and sample rate) is the same, FLAC uses lossless compression that takes advantage of the redundancy and complexity of the audio signal to compress the data. So for example:

- If the audio content is simple or repetitive (e.g. music with few instruments or long silences), the FLAC file will be more easily compressed → lower bitrate.
- If the content is very complex or rich in detail (e.g. a very dynamic live recording), the compression will be less effective → higher bitrate.

FLAC uses a variable bitrate (VBR) to optimize compression. It is not a fixed bitrate like for a constant bitrate (CBR) MP3. So the kbps value given in the FLAC file is an average or varies according to the complexity of the parts of the song. This is the reason why a FLAC file with same bit depth and sample rate has same quality even though the bit rate in kbps may be different, because the lossless lossless compression adapts to the content of the file, which can vary in complexity and therefore how much it can be compressed.

### Difference between a codec and a container

In previous sections we discussed sometimes about WAV, and it is spontaneous to ask oneself, for example, if both FLAC and WAV refer to the same non-loss of data, what’s the difference between the two? In a nutshell, the former is the container and the latter is the compression scheme.

A container is like a digital "wrapper" or "package" that holds audio data along with metadata (information about the audio, like artist, track title, sample rate, number of channels, etc.). The container defines how the data and metadata are organized and stored in the file and does not necessarily imply compression, it just specifies the file format structure. It is like who stores information in a way that an OS (Operating System) can read them. The container defines how the data is stored and organized so the OS, apps, or media players know how to interpret it. It’s not the operating system itself, but it enables compatibility and readability by the OS or programs. We can think it as a book with its *own* table of contents, chapters, page numbers, and maybe an index. So, a container format defines where the audio starts and ends, how to find the metadata, the file’s internal structure.

Pushing the reasoning further, a container can hold data compressed with different codecs. One thing that container also can define is also what kind of audio codec is used (if any). Thus, a compression scheme (codec) is instead the method or algorithm used to compress (reduce the size of) the audio data *inside* the container. As we discussed, compression can be lossless like in the case of FLAC when there’s no loss of audio quality, you can get back the exact original audio or lossy, when some audio data is discarded to save space, with some quality loss.

While WAV is primarily a container format and usually holds uncompressed PCM audio data which are basically raw audio samples and defines how audio and metadata are stored, but it doesn’t define the compression itself. To tell the truth, in the specific case of FLAC, it is both:

- A compression scheme (codec): it compresses audio losslessly.
- A container format: it defines how to store the compressed audio and metadata.

In practice, while WAV file is usually an uncompressed audio container, FLAC file is a compressed audio container using the FLAC codec. For audio, a WAV container might say “Start with this header, then store raw PCM samples, then maybe put some basic metadata at the end." while a FLAC container might say instead “Store compressed audio blocks here, and put detailed metadata (like album art, artist, lyrics) in specific chunks”.
