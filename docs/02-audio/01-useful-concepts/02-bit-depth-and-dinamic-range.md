# Bit depth (and dinamic range)

bit depth matters just as much. Audio resolution is 2-dimensional, and the sample rate is only your resolution in *one* dimension.
PCM audio is amplitude over time. Two dimensions. You need resolution for the “time” axis, and you need resolution for the “amplitude” axis.
Going high on one and low on the other doesn’t make much sense.

192khz at 24bit should be enough for all future.

**However**, note that when *processing* audio, the higher the sample rate the better. If you’re doing non-linear processing of audio, you will get harmonics, and you might get aliasing, and you avoid the problems of aliasing by using a higher sample rate.
A higher sample rate means you're more protected against aliasing.

And yes, aliasing sounds *horrible*.

Bit depth determines the minimum possible “step” change in the output waveform. With a bit depth of 1, you can only represent two output levels. With each additional bit, the number of available steps doubles and results in a smoother recreation of the original waveform in a linear pulse coded modulation recording (LPCM.) CDs use 16 bits per sample per channel for roughly 65K different output levels per sample. Alternative encoding methods can trade off a higher sample rate for a lower bit depth, or can encode audio in a compressed form that requires fewer bits per sample, throwing away data that a human is unlikely to notice during playback. All lossy schemes like MP3, Dolby, DTS, MP4, and AAC use this technique

Audio is always analog. The waveforms rise and fall in smooth, continuous, non-incremental ways and the frequency range goes from nothing to so far beyond human hearing that it bumps into the LF AM radio band.
Because even the parts you cannot hear have an influence on the parts you can hear, audible sounds are complex and nuanced things. The waves heterodyne as they interact, in the air, to produce additional complexity.

The dynamic range of sound, in nature, is a log scale that ranges from the very quiet sound of your own bodily functions up to the eruption of Krakatoa, the loudest sound in recorded history, which was heard 3000 miles away.

To turn that into digital audio, it must be
1. turned into an analog electronic signal,
2. passed through an A2D (analog to digital) converter, then at playback
3. it goes through a D2A converter, then
4. the converted analog signal is amplified to listenable levels.

CD audio tracks use a technical standard called "red book" and are raw Pulse Code Modulation (PCM) digital audio files sampled at a rate of 44.1 KHz and a depth of 16 bits. The bit depth determines the dynamic range and signal to noise ratio, while the sample rate determines the frequency response.

With 16 bits of resolution, there are 16,536 possible increments of audio amplitude (loudness) and a maximum SNR of 96db. The maximum frequency is half of the sampling rate of 44.1 kHz, so 22.05 kHz, in theory, but CD players have a brickwall audio filter at 19khz to prevent digital control signals from mixing with audio. If you have ever put a data CD into an audio player, you might have heard the sound of software which is not very musical.

[https://www.quora.com/Does-a-higher-sample-rate-audio-really-mean-better-quality](https://www.quora.com/Does-a-higher-sample-rate-audio-really-mean-better-quality)

Sound is a continuos signal or analogue waveform. Digital recording equipment truncate information so that the waveform can be stored as a discrete signal in digital format, which can later be re-created or converted back to analogue form before it is fed to an amplifier or transducer.

It is akin to using flash cards to represent a moving object, and the more times it is flashed per unit of time, the clearer the movement is reproduced.

In the truncation process, the basic sinewave information has to be sampled multiple times to enable the digital signal to replicate the analoque wave.

In this process, the higher the sampling rate, the higher the frequency response range can be captured. To reproduce 20,000Hz, the sampling rate has to be more than twice the frequency, hence 44.1kHz was adopted for the CD standard. This is essentially due to the Nyquist Theorem.

In digital audio using PCM (Pulse Code Modulation), the number of Binary Digits, (bits) or "bit depth" represent the number of binary digits used to represent a given analogue signal. The more bits used, the higher the fidelity or resolution and Dynamic Range of the original signal can be captured.

The CD standard uses 16bits of data but DVD or Bluray can support 24bits of data. 16 bits represents 65,536 (2 to the power of 16) possible integer values or a dynamic range of 96.33dBs. 24bits represents 16,777,216 (2 to the power of 24) possible integer values or a theoretical dynamic range of 144.49dBs! This is beyond the human hearing range!

In practical applications, 16bit CD or digital players reproduce only around13-14bits of resolution due to losses in the linerarity of the reproduced signal, from quantization errors and limitations of integrated circuits.

[https://www.quora.com/If-a-human-ear-can-hear-no-frequency-greater-than-20-kHz-and-we-need-no-more-than-40-kHz-sampling-rates-why-does-equipment-exist-that-plays-and-records-at-96-or-128-kHz-sample-rates](https://www.quora.com/If-a-human-ear-can-hear-no-frequency-greater-than-20-kHz-and-we-need-no-more-than-40-kHz-sampling-rates-why-does-equipment-exist-that-plays-and-records-at-96-or-128-kHz-sample-rates)

The high res recording has a higher bit depth - 24 rather than 16 bits - but most program material doesn’t take advantage of it. That’s because the dynamic range of a 16 bit recording is 96 dB. Assuming a peak level of 120 dB - a level that most home systems can’t even reproduce - that puts the noise floor at 24 dB, which is substantially below the noise floor of your listening room.

Pop songs in particular don’t need anything like 24 bits. Only the very widest range acoustical recordings - an uncompressed Mahler symphony, say - can potentially use 24 bits (or in practice, more like 21, since converters aren’t linear enough to use all 24).

Where 24 bits does come in handy is when making a recording. Since it’s impossible to predict precisely what the peak level will be, a bit of headroom has to be left, meaning that not all bits are used. So the 21 bits of usable dynamic range becomes more useful.

The only difference between 16bit audio and 24bit audio is that the noise floor is much lower with 24bit audio.

The reason that it is recommended to work at 24 bit when recording is because you will be layering up lots of audio files. This can result in background noise, so the further away it is to start with, the better.

I have no interest in debating an already well established fact, so I will disable the comments, sorry.

If you wish to test the difference. Take a 24bit file, dither it down to 16bit, then perform a null test on the audio. This is done by playing both files simultaneously with the polarity of one file reversed. The identical, but inverted audio cancels out, leaving you with just the differences between the files. Assuming you have done all this properly you will have a little noise down around -90-100dB (ish) which would of course be completely masked by 90dB of music.

I’m not saying you should not use 24bit audio, you absolutely should. But there is no audible difference in “quality”. It’s just the noise floor.

[https://www.quora.com/Is-Hi-Res-FLAC-24-bit-96-khz-better-than-CD-quality-Flac-16-bit-44-1-khz-Can-you-hear-the-difference](https://www.quora.com/Is-Hi-Res-FLAC-24-bit-96-khz-better-than-CD-quality-Flac-16-bit-44-1-khz-Can-you-hear-the-difference)

[https://www.quora.com/Can-you-hear-the-difference-in-quality-between-24bit-and-32bit-192khz-music-files](https://www.quora.com/Can-you-hear-the-difference-in-quality-between-24bit-and-32bit-192khz-music-files)

