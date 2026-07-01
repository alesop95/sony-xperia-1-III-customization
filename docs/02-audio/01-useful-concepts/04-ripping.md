# Ripping

Rippare significa estrarre i dati audio da una fonte fisica (come un CD o un SACD) per convertirli in un file digitale. Nel caso di un CD, si estrae il flusso audio PCM a 16 bit/44.1 kHz, creando un file WAV o FLAC. Nel caso di un SACD (che usa tecnologia DSD), si può “rippare” il layer DSD e poi convertirlo in PCM per un file FLAC 24-bit/88.2 o 96 kHz. Dunque to rip means copying the original audio content in a digital format without any loss  (lossless).

![](assets/img-0004.png)

That's the idea of Redbook CD, the disks you buy to play on CD players. It samples 44.1 kHz and is 16 bits, often written as 44.1/16

The way digital is done is often to record at what is called DSD, which is one-bit audio. You pass such audio through a low pass filter like a high-quality audio transformer to play it. The trouble is that single-bit audio has a horrible 6db signal-to-noise ratio. There is a trick called noise shaping you can search on that, in effect, moves the noise from the audible frequencies up to inaudible frequencies that can be in the many MHz range. So, you filter the DSD at 20khz. Since a CD is 44.1 kHz sampling, you need a steep filter. Such steep filters cause phase shits and ringing. A more gentle filter would be better - even no filter at all.

Read an article freely available online by searching on MQA Time-domain Accuracy & Digital Audio Quality.

Have a look at Figure 7. Note that 96 dB is 16 bits.

Notice that if you strip off all the bits below 16 (i.e. 96 dB), there is no content above about 32 kHz, so that it can be encoded with a sampling rate of 64 kHz. It does not matter what resolution you recorded; you only need to use a final sampling rate of 64 kHz. Sure, it is above audibility, but you do not have to worry about the filter. Note that filters would convert it to 64 kHz, but they can be at such high frequencies that they are inaudible.

64 kHz sampling is not a standard sampling rate, but larger sampling rates, such as 88.1 kHz, can be used if desired. Also, oversampling is usually used inside the DAC and can be converted to a multiple of a standard sampling rate. If you limit yourself to 14 bits, 44.1 k samples are enough. And if you use dithering, you can get a resolution of 16 bits, so 44.1/16 can be done easily. Plus, the dithering can contain information using the tricky MQA encoding method, so sampling at 88.2/16 can be reconstructed. If such is audible, it is moot, although there are probably a few cases where it is.

The bottom line is that to prevent filter distortions, while you can't hear it, you need to transmit at a higher frequency than 40 kHz for the highest quality. But by using 14 bits instead of 16, you can usually get away with standard CD 44.1/16

Also, lossless compression techniques will reduce the file to about half its size

A cd frequecy response is 20Hz to 20kHz at 44.1kHz sampling frequency. At 20 Hz , there are 2205 samples for each complete sine wave of audio. As frequency increases, the number of samples for each complete sine wave gets lower. At 2kHz , there are 22.5 samples per complete sine wave. At 20 kHz , there are about 2.2 samples per complete sine wave, and it produces a square wave which needs heavy filtering to round off the edges of the square, making a sine.

So a cd is more accurate at low frequencies, but at the top end is hopelessly inaccurate, the treble end.

At 96kHz a 20kHz sine wave is sampled 4.8 times. At 128kHz, it is 6.4 samples to describe a single sine wave, so , 3.2 samples on the first half of a sine wave and 3.2 on the 2nd half. Still a very small number of samples to accurately describe an audio sinewave. This is not ideal for the audiophiles in the audience.

DSD is the latest audio encoding method. This uses 1 bit (unlike cd’s 16 bit) but at 2.8MHz sample rate (2.8 million times a second). So at 20kHz there will be about 140 samples per sine wave making for extremely accurate reproduction and because there are so many samples per sine wave , it doesn’t need the heavy filtering needed with cd’s, improving audio accuracy , making audiophiles very happy people.

The reason we have higher sample rate capabilities these days , is that cd’s just aren’t good enough. We have computers that can record better than cd quality. A few different formats have arisen in the search for improvements in reproduction. Now we are seeing DSD audio masters being used as the source audio for vinyl LP manufacture. The ultimate in accurate audio recordings in combination with stone age vinyl is the peak of vinyl production at this time.

Check out The Rolling Stones, Let it Bleed, 2003 DSD remaster (original 1969). The audio on this album is what I would describe as the among best I have heared on vinyl and that was my first DSD remaster experience.

[https://www.quora.com/If-a-human-ear-can-hear-no-frequency-greater-than-20-kHz-and-we-need-no-more-than-40-kHz-sampling-rates-why-does-equipment-exist-that-plays-and-records-at-96-or-128-kHz-sample-rates](https://www.quora.com/If-a-human-ear-can-hear-no-frequency-greater-than-20-kHz-and-we-need-no-more-than-40-kHz-sampling-rates-why-does-equipment-exist-that-plays-and-records-at-96-or-128-kHz-sample-rates)
