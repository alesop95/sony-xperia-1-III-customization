# Sample rate

## What’s the point in higher sample rates than 44.1kHz?

L'udito umano arriva fino a circa 20 kHz, quindi la legge di Nyquist-Shannon stabilisce che basta un campionamento a ~40 kHz per catturare l'intero spettro udibile. I CD usano 44.1 kHz, lasciando una piccola riserva per applicare filtri anti-aliasing migliori.

Those sampling frequencies has nothing to do with the human listening capabilities. It is just a matter of improving the non-ideal sampling process. Frequenze ultrasoniche (es. 30 kHz e 33 kHz) presenti nei file a 192 kHz possono generare *intermodulation distortion* se riprodotte su amplificatori o tweeter non progettati per quei range.

L’ingegnere Christopher Montgomery (Xiph.org) afferma:

“192 kHz digital music files offer no benefits … the ultrasonics are a liability during playback.”

Dan Lavry (Lavry Engineering) aggiunge che il sampling a 192 kHz compromette l’accuratezza del segnale e introduce distorsioni

In test doppi-ciechi condotti da Mark Waldrep (AIX Records), i partecipanti - professionisti e ascoltatori comuni - non hanno percepito differenze tra audio hi-res e CD-quality. Uno studio della Boston Audio Society (Meyer & Moran) ha dimostrato che il salto qualità maggiore si ottiene passando da MP3 a 16/44.1 o 24/48; salire a 96 o 192 kHz non migliora ulteriormente la qualità uditiva

[https://www.headphonesty.com/2025/05/192khz-worse-44-1khz-most-music/](https://www.headphonesty.com/2025/05/192khz-worse-44-1khz-most-music/)

Paul Maunder (ingegnere Pro Tools) osserva che frequenze ultrasoniche caricano inutilmente CPU e plugin, aumentando la probabilità di saturazione/distorsione

Gli audiofili e gli ingegneri concordano: per l’ascolto a casa, 44.1-48 kHz a 16 o 24 bit è più che adeguato. Le conversioni ad alta frequenza servono solo durante le fasi di registrazione o mastering. L’uso di 192 kHz comporta file molto più pesanti (circa 6× rispetto a 44.1 kHz/16 bit), consumo extra di CPU e storage inutilizzati [https://hifiauditions.wordpress.com/2025/05/19/with-44-1-khz-weve-had-enough](https://hifiauditions.wordpress.com/2025/05/19/with-44-1-khz-weve-had-enough).

**Per l’ascolto normale**: CD-quality - **44.1 kHz/16-bit** (o 24-bit) è più che sufficiente. Un’altra discussione su Reddit (r/qobuz) ha raccolto diverse voci autorevoli: “from an audio engineer - In my experience, higher sample rates in the RECORDING process make a much bigger difference than in the listening process…” “I use Audirvana … the vocals are more diffuse in 24/192 or a more aggressive sound mostly in treble areas…”

[https://www.reddit.com/r/qobuz/comments/1kowgpu/192khz_worse_than_44khz](https://www.reddit.com/r/qobuz/comments/1kowgpu/192khz_worse_than_44khz)

That higher sampling rates mean slightly less inherent latency, which is important in live sound applications, at least to a point. Sometimes you need equipment to go to an extent that the human ear is not capable for the sake of resolution and precision. More precisely, oversampling becomes a powerful resource when trying to analyze "very fast" events (i.e., gunshots or supersonic events).

Moreover, frequencies over 20kHz (much over, actually), can contribute musically to an audio recording. Cymbals are one of the instruments where this effect is most noticeable. Without frequencies above 20kHz represented correctly, cymbals sound *extremely* flat. Cymbals are supposed to sound much crunchier than they do on digital recordings. Though you will recognize a digital recording of a cymbal as a cymbal because you've been trained to do so, if you listen to a live cymbal crash and immediately listen to a digital, sampled recording of it, I guarantee you will notice the difference. This difference is called **timbre**, and it is very important. Piano and Drums since the cover a wide marging of the audible spectrum. Starting at 44.1Khz and up with 16bits, my tests "showed" me a considerably difference in sound quality, call it psycho-acoustics but there is a difference. What’s more, the difference between the sound a violin virtuoso produces and the sound a fiddler produces has nothing to do with the fundamental frequency - which can be the same. It's in the waveform, which is dependent on the harmonics. So if you sample at a 20KHz rate, and someone is playing a violin, you won't hear the 7th harmonic of very high pitch note when the recording is played back, and it'll sound more like a pure tone (sine wave) at the fundamental frequency than it will like a well-played violin playing that note. The mixture of various harmonics is why a violin, a trumpet and a clarinet, all playing the same note, sound different.

[https://www.quora.com/If-a-human-ear-can-hear-no-frequency-greater-than-20-kHz-and-we-need-no-more-than-40-kHz-sampling-rates-why-does-equipment-exist-that-plays-and-records-at-96-or-128-kHz-sample-rates](https://www.quora.com/If-a-human-ear-can-hear-no-frequency-greater-than-20-kHz-and-we-need-no-more-than-40-kHz-sampling-rates-why-does-equipment-exist-that-plays-and-records-at-96-or-128-kHz-sample-rates).

I have found 3 main reasons to use high sample rates:

If your recordings are destined to be used for sound design a high sample rate allows you to capture information that will be audible if the audio is pitched down. Let’s say I make a recording at 48k, then pitch it down one octave. The original file had information up to 24kHz, but now the highest frequency in my pitch shifted file is only 12kHz. The result is dull sounding because of the missing information from 12-20k. If I record at 96k I will capture up to 48kHz, and the pitch shifted result now has informtion up to 24kHz. The processed signal will have a full frequency range and sound much more believable. Sample up to 192k and then I can even pitch shift a full 2 octaves and still have the full audible frequency range. (Watch the scene in The Matrix Reloaded with the “pipe fight”. The sound of the wind through the pipe during the slo-mo sequences still sounds realistic because the original recordings were at 96k.)

For classical ensembles the ultrasonic information that happens in the air contributes to the audible spectrum. Unfortunately it is common practice to close mic large ensembles sometimes and those interactions don’t have time to happen. By capturing this extended frequency range those interactions can happen inside the DAW. I do a lot of classical recording and I believe there is a value to high sample rate recordings in that situation.

Even if the recording does not make use of the extended range the extra data does give plugins more to work with. Some engineers claim that compressor plugins sound smoother when fed with higher sample rates. I have not seen any scientific research on this yet, but it is a common opinion.

Having said all that I will admit that for pop or rock those high sample rates are usually unnecessary. If you mic a band with SM57s and a bunch of other cheap mics you can’t capture any of those high frequencies anyway, and unless you agree with #3 a higher sample rate will simply take up more space on your hard drive and make your computer work harder.

[https://www.quora.com/If-a-human-ear-can-hear-no-frequency-greater-than-20-kHz-and-we-need-no-more-than-40-kHz-sampling-rates-why-does-equipment-exist-that-plays-and-records-at-96-or-128-kHz-sample-rates](https://www.quora.com/If-a-human-ear-can-hear-no-frequency-greater-than-20-kHz-and-we-need-no-more-than-40-kHz-sampling-rates-why-does-equipment-exist-that-plays-and-records-at-96-or-128-kHz-sample-rates)

Ok so the sampling theorem says that the sample rate must be strictly greater then twice the bandwidth, so for the generally agreed 20kHz upper limit of human hearing (Which is actually optimistic for most people over 18 or so) we need at least a 40kHz sample rate.

Now back in the day (Early 80s) finding something to store the data that was cost effective was a problem, we needed something that ideally reused existing technology rather then inventing something new from scratch…..

Enter the VIDEO RECORDER, by encoding the digital audio as a video signal, it was possible to use existing video recording technology to store the data on readily available video tapes.

Problem: There are two video standards that matter, NTSC and PAL and they have different frame rates (25Hz and 30Hz (Actually 29.97Hz approximately), and different numbers of video lines. When you do the maths, it turns out that 44100 samples per second was the lowest rate that both satisfied the sampling theorem and at three samples per line could be made to work on both NTSC and PAL format recorders.

Note that 44.056 was used in the US to deal with the weird NTSC frame rate (Required to minimise interference between the colour subcarrier and the original sound carrier!, it is compatibility all the way down), but that is a 0.1% change and nobody really cared.

It is interesting to note that at the time the EIAJ was standardising on a 14 bit format for consumer audio because that was the best we could do with affordable chips at the time, it was Sony who pushed 16 bit.

See the Sony PCM F1 brochure here

[https://www.kenrockwell.com/audio/sony/pcm-f1.htm](https://www.kenrockwell.com/audio/sony/pcm-f1.htm)

For the 1981 marketing guff.

This thing was absolutely revolutionary.

While some audiophiles may prefer higher sampling rates for "better" sound quality, a standard 44.1kHz sampling rate is generally sufficient for most listeners, especially when considering the limitations of human hearing and the typical listening environment. Higher rates like 96kHz or 192kHz can offer subtle benefits in audio production and post-processing, but the subjective difference for playback is often negligible for the average listener. 

Here's a breakdown:

44.1kHz and Human Hearing:

The Nyquist-Shannon sampling theorem states that to accurately reproduce a signal, you need to sample at a rate at least twice the highest frequency in that signal. 

Since the highest frequency most humans can hear is around 20kHz, 44.1kHz (44,100 samples per second) is more than adequate to capture all audible frequencies. 

While some might argue for higher rates to capture ultrasonic frequencies or subtle nuances, the benefits are debatable and often imperceptible to most listeners. 

Benefits of Higher Sampling Rates:

**Production and Post-Processing:**

In audio production, higher rates (like 88.2kHz, 96kHz, or even 192kHz) can provide more headroom for processing and manipulation, minimizing potential errors during digital signal processing.

**Less Distortion:**

In theory, higher rates can reduce the need for aggressive anti-aliasing filters, potentially leading to a smoother treble response. 

Why 44.1kHz is Often Preferred for Playback:

**Standard:**

CD quality audio uses a 44.1kHz sampling rate, and this is a widely adopted and well-understood standard. 

**Small Subjective Difference:**

While some audiophiles may claim to hear differences, most listeners won't be able to discern a significant improvement in sound quality when comparing 44.1kHz to higher rates. 

**File Size:**

Higher sampling rates result in larger file sizes, which can be a consideration for storage and streaming. 

Conclusion:

For casual listening, 44.1kHz is a perfectly acceptable sampling rate. While higher rates can offer some benefits in audio production and may be preferred by some audiophiles, the perceived difference in sound quality for playback is often minimal and may not justify the increased file size or processing overhead. 

[https://www.quora.com/Does-a-higher-sample-rate-audio-really-mean-better-quality](https://www.quora.com/Does-a-higher-sample-rate-audio-really-mean-better-quality)

The higher the sample rate, the more clarity and precision. Overtones (harmonics) are destroyed by digital sampling, but more so with lower sample rates. A higher sample rate will have better reproduction of the *original analog overtones*.

CD quality is 16 bit 44,100Hz sample rate, meaning, it takes a sample of the sound wave 44,100 times per second, and the bit depth is how many steps are available for it to place the amplitude of the sampled wave. i.e., say the bit depth allows the amplitude to be placed at a resolution that makes 1, 1.5, & 2 available. Therefore, if the sample's amplitude is 1.6, it will be placed at 1.5, if it is 1.75, it will be placed at 2. And, 44,100/sec might seem like a lot, but what ultimately happens is the wave ends up in squared off step shapes. It is no longer a smooth, curvy wave. But the higher the sample rate, the more curvy the wave.

the decoded signal from 44.1 audio has a large 22.05 kHz component which must be filtered out. Filters are imperfect and work better when the signal to be removed is farther in frequency from the signal to be kept. The analog output of 96 kHz audio for example, is not attempting to reproduce 40 kHz waves.

[https://www.quora.com/What-is-sampling-rate-in-audio-and-why-do-we-choose-44-1-kHz-as-recording-sampling-rate](https://www.quora.com/What-is-sampling-rate-in-audio-and-why-do-we-choose-44-1-kHz-as-recording-sampling-rate)

Analogue audio - the old-style convention - was a continuous electrical representation of the signal level. It had infinite frequency resolution within the bandwidth of the audio chain carrying the signal, and infinite amplitude resolution, within the limitation of associated noise. That noise was a critical problem, because whenever the signal was recorded and copied, additional noise was added.

Digital audio takes that analogue signal and converts it to a string of numbers. It samples the signal very frequently, measures the level and then reports that measurement in numerical form. Provided you can record and replay these numbers (and ultimately convert them back to analogue) then no noise is added in the process. You can transmit, record, copy as many times as you like without compromising the original signal.

The frequency at which you do the sampling needs to high enough to measure the fastest peak signal within the audio bandwidth. This - the so-called Niquist frequency - turns out be anything greater than twice the maximum audio frequency you are interested in. In practice you need a little more than that to allow various filters used in the process to operate, so anything that is a bit faster than 2x20kHz will work.

The actual choice of 44.1kHz had to do with the use of video recorders that were the only type of device capable of recording wideband digital signals when CD was invented. These recorders needed the signal to be broken up to fit into the line and field structure of an analogue TV signal, and the maths to fit neatly for both European and US line and field rates dictated 44.1kHz.

Sadly the 44.1kHz rate doesn’t fit in well when video pictures are involved, so for film and TV production a different set of maths was required, resulting in 48kHz sampling rates. For various reasons, not all of which have much technical validity, multiples of the standard rates (88.2kHz, 96kHz, 192kHz etc) are sometimes used too.

Note that although discrete, separate samples are taken, the frequency domain resolution *within the audio bandwidth* is infinite if the replay filtering is done correctly. In exactly the same way the amplitude resolution is also infinite provided that *dithering* is carried out correctly. The converted digital signal is indistinguishable from the original analogue one. The frequently met assertions that digital sampling results in stepped waveforms, with incomplete frequency resolution, are simply wrong.

Quindi

If a human ear can hear no frequency greater than 20 kHz, and we need no more than 40 kHz sampling rates, why does equipment exist that plays and records at 96 or 128 kHz sample rates?

[https://www.quora.com/If-a-human-ear-can-hear-no-frequency-greater-than-20-kHz-and-we-need-no-more-than-40-kHz-sampling-rates-why-does-equipment-exist-that-plays-and-records-at-96-or-128-kHz-sample-rates](https://www.quora.com/If-a-human-ear-can-hear-no-frequency-greater-than-20-kHz-and-we-need-no-more-than-40-kHz-sampling-rates-why-does-equipment-exist-that-plays-and-records-at-96-or-128-kHz-sample-rates)

The short answer is - filtering.

Even very young people are not going to hear anything over 22khz. But some would say that the LPF roll-off needs to be quite shallow so as not to cause distortion and higher sampling rates provide more margin and prevent this roll-off eating into audible frequencies. Can’t argue with the theory, but in practice? No. Especially if your’re over 25 then that margin has naturally widened anyway. And the program needs to be well recorded and mastered rather than just upsampled and contain frequencies high enough to matter. [https://www.quora.com/Are-there-any-benefits-to-listening-to-music-sampled-higher-than-44-1-kHz](https://www.quora.com/Are-there-any-benefits-to-listening-to-music-sampled-higher-than-44-1-kHz)

	According to the Nyquist-Shannon sampling theorem, it is necessary to take more than two samples per cycle of the highest frequency you want to capture. That means more than 40k samples per second if you want a system response flat to 20 kHz. Also, it is mandatory to absolutely prevent any frequencies that would violate the sampling theorem (i.e. > 20kHz) from getting to the analog-to-digital converter, so there is a need for an “anti-aliasing” filter to reject them. It’s tricky to design filters that go from completely passing a signal to totally rejecting it over a very narrow range, so you need to add a little more to the sampling rate to allow for “real world” filter performance. That will get you near to 44 kilosamples per second.

As to why exactly 44,100 (or alternately 44,096) samples per second, that is because at the time the CD was introduced the only reasonable medium for transferring digital masters to CD production facilities was VCR casettes(!). At that time, computer tape drives were very expensive, disk drives were even worse, and computer networking was essentially non-existent.

Video cassettes had the capability to handle the data rate (~1.5 megabits per second), but in order to get things to work, it was necessary to make the digital audio “look like” analog video, complete with synchronizing pulses, etc. The “picture” just looked like noise, but the videocassette machines didn’t care just so long as the sync was good. Analog video (in the US) uses exactly 60 fields per second if the signal is black and white, or 59.94 FPS if it is color. So, if the audio production facility used a B&W sync generator, the audio needed to be sampled at 44,100 samples per second, and if it was a color facility, the sync was 59.94 FPS and the audio was sampled at 44,096 SPS.

There seems to be a huge amount of misunderstanding about digital sampling and reconstruction, with many folks believing that the digital audio will “be pulses” or would “look like a staircase”. That is totally false. IF the signal is properly conditioned prior to the A-D (the antialiasing filter), *and* there is a proper “reconstruction filter” after the playback D-A, the reconstruction is perfect. Not “close”. PERFECT.

As for why there are sample rates above 44,100 and/or precision greater than 16 bits per sample, there are two reasons: First, during the *production* process that greater precision can come in handy when performing “math” on the audio (as all digital audio workstations do) in order to minimize rounding errors. Second, there is always a group of folks who will spend money on unnecessary things (in this case, because they do not understand Nyquist-Shannon), and a group who is more that willing to spread BS and take their money rather than explain why what they want is a pointless waste of money.

	For recording and processing, however, higher sample rates can be beneficial - because we can’t build perfect equipment, everything is a compromise. One of the reasons would be sampling clock jitter but, depending on the particular equipment, there may be a sweet spot below the maximum available sample rate where the accuracy of capture is the best. Jitter versus sample window versus averaging. The Low Pass Filter that does the band limiting is another area. You want to build an analogue filter that brick-walls between 20kHz and 22.05 with infinite rejection and no pass band ripple!? Not going to happen. So, build a more relaxed filter, sample at a higher rate and then re-filter / re-sample in the digital domain where it is easier (but still not 100% perfect).

+

Every time you want to do an in-the-box EQ, or fancy time-based effect, it’s also going to be more accurate if you upsample. Easier and less lossy if you already have the audio upsampled, rather than having to up and down-sample it all the time through the mixing / production chain.

Sampling at higher rates makes it a LOT easier to design the anti-aliasing filters in front of the ADC. If I want to record up to 20kHz, and I’ve got a 40 kHz sample rate, I need a filter that has a “brick wall” response to keep signals at, say, 21kHz from aliasing down to 19 kHz and so forth. Such a steep filter response (pass everything at 19.999, stop everything at 20.001) is difficult to build, it will have lots of components, all those components have tolerances.

On the other hand, if I’m sampling at 128 kHz, I can have a filter that starts rolling off at 20 kHz and is, say, fully rolled off by 50 kHz. There’s no power above 64 kHz to alias in, especially that will alias below 20 kHz (anything above 108 kHz). A nice gentle slope, smooth phase response, etc. Then I take my 128 kHz sample stream and apply a *digital filter* to get my brickwall response - I can use lots of samples so I can control the phase behavior, I can have infinite precision in the calculations, and then I can resample down to 40 kHz sample rate. That digital filter can also compensate for non-ideal analog filter behavior.

A similar thing applies to digital to analog conversion - If I have a 40 kHz DAC, what actually comes out is my desired signal from 0-20kHz, and aliases every 20 kHz, which I need to filter out. Same problem - I need a brickwall filter to get rid of them. Instead, I run my DAC at 128kHz (perhaps doing some prefiltering in the digital domain when bringing the sample rate up from 40 kHz to 128 kHz), run it through an easy to build, gentle, low pass filter that cuts off at 20kHz, rolling off by 40-50, etc.

Back in the day, when getting 16 or 24 bits at 44 kHz was an ordeal, you used lots of op amps in your analog filters, each adding noise and aging and temperature stability problems. Now, you can likely use a passive filter - lower power, lower noise, etc.

Even if you can’t hear it directly, you don’t want to have 20kHz+ quantization noise components in the spectrum. They’re wasting power and causing intermodulation distortion with very audible artifacts.

The problem with 44kHz sampling rate is that these noise artifacts are only one octave separated from the audio signal. It’s difficult to filter them out with traditional filters with 6dB/octave selectivity. With 96kHz or 192kHz sampling the situation is somewhat better, but still not perfect.

Delta-sigma converters have only 1 (one) bit resolution, but extreme sampling frequencies in the MHz range. This helps pushing the noise spectrum far away from the audio signal where it’s easier to filter out

	Higher sampling rates are useful during the production process to avoid e.g. rounding errors when performing mathematical operations on the source material (and of course, all of the mixing and filtering processes in contemporary audio production are computer-based, and so are “mathematical”). Can you actually *hear* the difference when higher sampling rates are used? Sometimes. Maybe. Now, prove that the difference is not the result of artifacts in the higher-rate equipment (i.e. that it is actually not doing a less-accurate job of recording and reproduction). Just because you can hear a difference, does not automatically mean that the high-rate gear is “superior”.

The historical (cum technological) reasons for choosing 44.1 kHz as sampling rate are given here:
[http://www.cs.columbia.edu/~hgs/audio/44.1.html](http://www.cs.columbia.edu/~hgs/audio/44.1.html)

To summarise:
1. It is recognised that to be able to reproduce upto 20 kHz which is generally accepted as the highest frequency human beings can hear, one needs to sample it *at least* twice that highest frequency (as per the Nyquist theorem), which is 40 kHz or more.

2. Since computers in the early days of digital audio did not have sufficient storage, a means was devised to store digital audio on video tapes as pseudo video signals.

3. 44.1 kHz sampling rate was chosen because methematically it satisfies both 60 Hz NTSC and 50 Hz PAL television systems.

4. 44.1 kHz has been subsequently adopted for audio CD sampling rate.

Now, why sample at more than 44.1 kHz if 44.1 kHz suffices theoretically? Remember 44.1 kHz is like the bare minimum we can get away with to reconstruct the original audio signal.

Having more samples allows reconstruction of the original signal more closely, but this needs more processing power as higher number of data points need to be processed. But higher sampling rate puts less stringent requirements on output filters.

How much higher should one go? I don't know the answer to this but I can tell you many (if not most) digitally recorded studio masters are 24 bit 96 kHz recordings. There are two schools of thought - one that says 96 kHz is sufficient and one can't hear any sonic improvement beyond this rate. And then there are others who swear by higher sampling frequencies. An extreme example is Direct Stream Digital sampling rate used in Super Audio CDs which is 64 times 44.1 kHz = 2822.4 kHz.

These resources (quelle sotto) seem to get it quite right:

[If a human ear can hear no frequency greater than 20 kHz, and we need no more than 40 kHz sampling rates, why does equipment exist that plays and records at 96 or 128 kHz sample rates?](https://www.quora.com/If-a-human-ear-can-hear-no-frequency-greater-than-20-kHz-and-we-need-no-more-than-40-kHz-sampling-rates-why-does-equipment-exist-that-plays-and-records-at-96-or-128-kHz-sample-rates)

http://en.wikipedia.org/wiki/Oversampling

Oversampling gives better transition to anti-alias filters and reduces noise.

---

You can record bats, provided you have an ultrasonic microphone :)

Seriously, I heard different theories on that. I don't know to what extent they are believable, though:

1) Analog filtering. When the sound is captured and filter analogically, the lowpass filter has more "room" and needs to have an easier slope. Analog filters have physical limits (you can't just add computation power like you do with digital ones), so it's critical to have the best filter possible. Oversampling would make it easier to have good filters (or, it would make analog filters behave better).

2) Delay. Spatial perception on >2 speaker systems is made delaying sounds (or not) to give the brain the illusion they are distant or near. According to this theory, since the subtlest of these delay can be significantly smaller than the sampling rate, you need a sound engine with a clock much more precise than 44100 kHz.

3) No resampling. If you plan write on a medium that natively stores, say, 96 kHz sampling rate, you don't have resample you signal if you capture audio exactly @96. This doesn't explain why there are mediums that store oversample audio in the first place This theory assumes that upsampling, even to ultrasonic sampling frequencies, always introduces unwanted artifacts.

4) Money. Oversampling costs little, but it looks great on the box, given that most audiophiles know nothing about Nyquist frequencies and gladly pay hundreds of dollars for monster cables they don't really need: http://www.engadget.com/2008/03/03/audiophiles-cant-tell-the-difference-between-monster-cable-and/ )

(see also a discussion on the topic here: http://www.dvinfo.net/forum/all-things-audio/64653-44-1khz-vs-48khz-how-important.html an here: http://www.dvinfo.net/forum/all-things-audio/64653-44-1khz-vs-48khz-how-important.html )

Sounds in the real world have frequency content right up to 50kHz. So to sample them at 44.1 kHz the Nyquist Theorem requires everything above 20kHz to be filtered out.

But realtime filters are never perfect, and will affect the sound at lower frequencies than this cut-off - either by removing some of that lower-frequency content, or by messing with it's phase.

With a filter at 20 kHz, these filtering side-effects are audible on some material. Whereas if you sample at 96 kHz (say) the filter can be at 48 kHz and any side-effects are still way higher than our ears can hear. The higher you go, the gentler the filters can be (fewer audible side-effects) and the less filtering is required.

Exactly how beneficial these high frequencies are in the real world is debatable, though...!

Because a number of studies -

[Neve 1992](http://jn.physiology.org/content/83/6/3548)
[Theiss and Hawksford 1997](http://jn.physiology.org/content/83/6/3548)
[Yamamoto 1996](http://jn.physiology.org/content/83/6/3548)
[Yoshikawa et al. 1995](http://jn.physiology.org/content/83/6/3548),[1997](http://jn.physiology.org/content/83/6/3548)
[Japan Audio Society 1999](http://jn.physiology.org/content/83/6/3548)

- have shown that, even though the human ear can’t consciously perceive sound above 20KHz - (15-16KHz in most cases), brain activity is still affected by the presence of bandwidth extended as far as 32KHz or more. It could have to do with phase relationships between audible frequencies, which become more exact at higher resolutions, or the mere fact that the natural world imposes no 20KHz limit on frequencies transmitted through the air - (indeed there are ultrasonic frequencies present all around us) - and that we’re aware of them without “hearing” them, but in tests where the *same material* was presented *with* and *without* extended frequency response, listeners, *without being aware which one was being listened to*, preferred the extended frequency-response versions of the recordings well above statistical random.

There has also been a study -

[There's life above 20 kilohertz! A survey of musical instrument spectra to 102.4 kHz](http://www.cco.caltech.edu/~boyk/spectra/spectra.htm)

- showing that (acoustic) musical performances have content above the audible spectrum.

We may yet find the same to be true of light and images; experiments in video transmission are being conducted to try and see if the inclusion of ultraviolet light spectra leads to more realistic images.

Audio sometimes takes on a ridiculous yoghurt weaving, crystal wearing nonsense. People want to believe things sound better like gold connectors, speaker cables that cost as much as a good second hand car, and higher sample rates.

It’s all nonsense. Don’t believe the hype. If you can hear the difference between 48KHz and 192KHz you have better hearing than me, and I’ve made a career out of my ears.

There is no audible benifit to higher sample rates, the only thing it achieves is hotter DSP and CPU chips. Don’t believe the hype.

Some of the answers given already are great, but I think they are missing the most important factor of all: **Human phychology**.

Have you ever wondered why is it that you would need a cellphone with 4GB or RAM instead of one with 2GB, or even 1GB or RAM?

The real answer to that question is: *you don’t*. Still, people prefer the one with 4GB or RAM over the other models.

Now…*why* is that?

One might be tempted to say that more memory is always better, but there comes a time in which you don’t really need any more. This means that, unless you can have the data, you can’t even tell which has the more memory.

Let’s come back to the sampling frequencies now. We don’t really need more than 40kHz, but certainly a model with 96kHz is *much more powerful*, and more powerful is *always* better, *right*?

Do not forget that those products are still fighting for their place on a competitive market, so they have to show *something* that is better than the rest, even if it makes no difference.

There have been countless experiments that prove that what people perceive to be better will alter their experience with the product. If you were to offer to glasses with water to someone, have they taste both, and then you tell them that glass #1 has mineral water and glass #2 just plain tap water, I guarantee that 99% will say that glass #1 is better, *even* if you poured the same water into both glasses.

I do not mean to say that the other reasons given here are invalid, but **never underestimate the psychological factor**.

Dave Haynie

When the CD was released in 1982, it was already a fairly consumer friendly thing to deliver 44.1kHz, 16-bit sampled audio. According to the Nyquist-Shannon sampling theorem, that can perfectly reproduce a 22.05kHz sine wave -- a pure tone at 22.05kHz.

![](assets/img-0001.jpeg)

However, no one at the time really planned to have you hearing 22.05kHz audio. What they wanted was the ability to reproduce a proper sounding 20kHz *or so*. Ok, so let's talk digital to analog conversion here. There's a popular misconception that the output of a digital signal is a stair-stepped waveform, as shown here. **That's incorrect!** What you really have is a series of impulses: single point samples, 44,100 times per second. Nothing in-between the samples.

A pure signal at 22.05kHz would be a sine wave, not a square wave. And a perfect square wave is a thing that can only exist mathematically. It has a series of infinitely high frequencies contributing to its creation. That’s not what you get when you reconstruct digital impulses as a series of analog sine waves.. you get the original signal back. If there were any higher-order frequencies from that process, they’re going to be filtered anyway, via a filter called an anti-imaging or reconstruction filter.

If you could make a perfect brick-wall filter, a filter that blocked 100% of the signal above 22.05kHz, and passed everything at frequencies below 22.05kHz, you'd be good and have your essentially 22.05kHz signal. But real world filters don't work that way. They can only cut frequencies so far, typically, about 6dB (half amplitude) per octave per filter stage. You can gang up multiple filter stages, but that leads to other kinds of distortions in the audio. And, maybe not a huge shock here, but early CD players were either pretty expensive, or had sound issues we probably wouldn't accept today. So that's the basics.

But why do we make higher sampling rate hardware. There are plenty of reasons.

**Because we can.**

The technology for making a CD DAC was not exactly cutting edge in 1982. What was cutting edge? The first PCs based on the Intel 80286 microprocessor. These came out, with as much as 640K of RAM and a 6-8MHz clock for $5000+. My current smartphone has 4GB of RAM and six 2GHz+ processors... it makes mincemeat of such an old PC. So electronics has evolved in amazing ways since the dawn of consumer digital. One way it's moved is that, just like Intel was dedicated to selling a faster CPU to IBM or Compaq in those days every year, the companies making DAC chips (and the corresponding analog to digital converter, or ADC, that you need to make a digital recording) were making constant improvements. For example, the DAC in my new smartphone (LG V10) has the ESS Sabre 9018C2M DAC ([http://www.esstech.com/files/8714/4095/2156/SABRE9018C2M_PB_v0.9_141212.pdf)](http://www.esstech.com/files/8714/4095/2156/SABRE9018C2M_PB_v0.9_141212.pdf) and the ESS 9602C headphone amp... that's not 24-bit, but a 32-bit DAC.

Why? Because they can.

No one needs a 32-bit audio sample... 24-bit delivers a 144dB signal to noise ratio (SNR) or dynamic range (DNR). That's wider than the difference between absolute silence and the human threshold of pain. It's also more resolution than any practical analog audio system -- or even any of these chips -- will deliver once in the analog domain (the DNR on this chip is about 127dB , which while fantastic, means there are in effect 22 actual bits and 10 marketing bits in the resolution of this best-in-class DAC).

**Digital filters and oversampling.**

Ok, so up above, I established that there's a need to filter, and filters ain't perfect. What if I told you that there's a magic trick available in the digital world? That's called oversampling. I can build a filter in the digital domain that runs at many times higher frequencies than the actual sample, but will do most of the work of sample reconstruction, with a mathematically perfect digital filter rather than an analog filter I have to build with actual real-world components. It will leave some residual noise of its own, but at much higher frequencies. And so, that means a very simple analog filter after the digital filter, which can be gradual because I pushed the analog noise and perhaps some digital noise as well up high, where you really can’t hear it. Maybe not even your dog, depending on the frequencies.

That's what pretty much every modern DAC does today.. you'll read things like 64x or 128x oversampling... that means it's doing it's work way the hell up there in megahertz land. This is good. And I could bring that now-filtered audio out at 22.05kHz and apply a relatively simple analog filter. But since I have all this stuff going at higher speeds anyway, I can also deal with 96kHz or 192kHz samples, output 48kHz or 96kHz audio, and use a very basic filter, because you’re not able to hear that high anyway. So anyway, that's one reason, and it's generally a good one.

And as mentioned, that oversampling DAC is digital. In most cases, digital = cheap … we have made our digital stuff faster, cheaper, and quieter every year. Oversampling DACs are not without their critics, but for most everyone else, they're delivering a much better sound than you'd be able to get with an analog filter you'd be willing to pay for.

**Audiophiles, Audiophools, and Specs.**

So, a not-necessarily-so-good reason for these is that humans love simple quality metrics. In the days of the PC wars, the one they settled on was MEGAHERTZ. You needed a faster clock to deliver a faster CPU. In fact, not always true... Intel jacked up the clock on the Pentium 4, but it didn't really make for that much of a faster chip. AMD at the time actually had a better architecture -- something Intel did even better, in the days after the Pentium 4 (and maybe AMD’s finally matching with Ryzen… but that’s another article). Computer performance and architectures are very complicated things (well, for most people), and they're just looking for some answer. Same goes with digital cameras and megapixels. Same with cars and horsepower. It's been around forever.

So it is with sample rates, sample depths, and all things digital... the sounds, what we can hear, etc. are complex issues of technology and physiology. Most people don't care that much -- thus, the rise of the MP3 player. Some do. I do studio work -- audio production -- as an advanced hobby, and I want to hear sound in a certain way, employing "critical listening", a full concentration on the sound [hopefully] without prejudice, so I can hear if maybe the bass needs another +1dB or so, etc. Because of that experience, I believe that true audiophiles are often self-taught critical listeners, hearing things that the rest of us -- maybe even studio rats -- don't hear. I wrote a couple articles touching this subject here:

[https://www.quora.com/Are-vinyl-records-considered-to-have-better-audio-quality-than-CDs-or-high-bitrate-MP3-audio-encoding-format-Gupta-Audio-Studio/answers/8905623](https://www.quora.com/Are-vinyl-records-considered-to-have-better-audio-quality-than-CDs-or-high-bitrate-MP3-audio-encoding-format-Gupta-Audio-Studio/answers/8905623)

[https://www.quora.com/Is-it-true-that-record-players-have-the-best-sound-quality-as-compared-to-cassettes-and-digital-music-Comparatively-analyze-the-various-different-digital-sound-formats/answer/Dave-Haynie](https://www.quora.com/Is-it-true-that-record-players-have-the-best-sound-quality-as-compared-to-cassettes-and-digital-music-Comparatively-analyze-the-various-different-digital-sound-formats/answer/Dave-Haynie)

On the other hand, you will look long and hard to find an industry with more "snake oil" salesmen in it than the audiophile market. There are all kinds of people promising all kind of incremental performance wins, lovely magical coloration of a sound through a speaker wire, etc. I think it's pretty much all bogus, but I have different needs. When I buy a wire, I want a reliable plug that's not going to wear out -- nickel chrome plating, not a few angstroms of gold over corrosive copper. One thing you can bet -- true audiophiles are spending way more on their wires than the was spent on the wires used to record that music.

**Recording and Beats**

So, one additional thing to consider is how music is played. I don't have a great deal of gear that can record much in excess of 22kHz or so, other than my recording interfaces. Few general purpose mics go much higher, etc. But instruments do, and even those mics not speced beyond a certain range will record there, just not linearly.

So in the old days, and sometimes even today for those of us recording amateur bands as non-professional recording engineers, we do a "live in the studio" recording. That's when the whole band plays. It's pretty common in traditional Jazz recording to just set up a stereo XY mic or whatever and monitor your levels while the players do their thing. If I have my 'druthers, I have at least one mic on every instrument or vocal, at least three on the drum kit (two overhead small condensers and one dynamic kick mic). This means I have lots of control when mixing. And if I had a studio, I might actually be able to record every instrument separately... which I also do when I'm recording myself... awfully hard to play harmonica, guitar, and sing several vocal parts -- with doubling -- all at once.

Ok, so here's an interesting phenomena... beat frequencies. When several frequencies play, our brains put together the result of both as a new frequency. Digital sampling will also record this "beat frequency" as long as your recording device gets both original sounds... it's going to reject the higher frequency signal, but it may preserve the "envelope" described by the higher frequencies.

![](assets/img-0002.png)

However, if you're recording many separate tracks, these interactions may not fully occur until playback... perhaps the first time the two stereo or 6-8 surround channels ever interact in the real world. When there actually is higher frequency energy, you can't hear that directly, but it's possible to hear beats, it's possible to hear subharmonics and other interactions based on your room. Now, whether you actually want that, that's maybe a different question, but it is one small argument for maintaining the higher frequency information. This is always a potential issue when mixing a project (and one reason not to mix on headphones when you can help it)… perhaps less value, but still a potential issue, when playing back as a listener.

**An Actual Good Argument**

However -- and there's certainly some controversy here, too -- I found Neil Young made a good argument for high end audio playback in his Pono Kickstarter and now company. When I record, I usually record at 24-bits/sample, 96kHz. Because I can. Everything I use supports that rate. When I mix, I mix at 24-bit, 96kHz. So my final recording is done, and then I have to downconvert/downsample to 44.1kHz/16-bit for playback. That means a non-integer interpolation for sample rate. And it means dithering -- actually adding a small bit of very carefully designed noise -- to go from 24-bit to 16-bit samples. All of those tools are very high quality, very mature, but it technically does affect the music. I'm not sure I can hear the effect these days ... with earlier technology, I believe I could. Doesn't matter -- perhaps others can.

So the Pono goal was this: you should be able to get a copy of that final artists' mix, in the exact same resolution, nothing changed, and hear that music exactly as the artist intended. Since there really isn't one way of doing a recording or a mix -- some folks, like Dave Grohl, still use analog tape -- there isn't one way of deciding, as CD or DVD did, that THIS is that one way. So making a player that can play any format -- like a PC can -- is an enabling technology to make this idea work. I can't swear it IS working, but PonoMusic at least attempts to only offer the best version of any music they sell. And they upgrade you if a better one comes along (I have no interest in Pono other than being a Kickstarter and wanting THAT specific idea to be successful).

**But Is This a Bad Idea?**

And it's easy to think... hey, why not get the best sampling rates. How can it hurt? Well, part of the problem is that you kind of need the whole signal chain to be at those frequencies. So if you're playing a 192kHz sample into an amplifier that's linear out to 96kHz into a speaker network that can reproduce 96kHz, you're just dandy. At the worst, you spent all kind of extra money for no real improvement. At best, your ears are better than mine and you actually hear a difference over 96kHz or 48kHz. Or at least you dog does. Let's not worry about that.

But there's another thing that's worth understanding, but it isn't always just a free ride. I designed radios for ten years at a startup company, and one of the major components of a radio is a thing called a RF mixer. It's not an audio mixer, but rather, a non-linear component that causes chaos

![](assets/img-0003.png)

So I put two signals into a linear circuit, like an amplifier, and out come those two signals.. you could filter them apart again, and find nothing extra there. But put two signals into a non-linear component, and you'll get, as shown in the diagram, the sum and the difference, as well as the two original signals. And thanks to a phenomena called transconductance in real world non-linear systems, you get "spurs", or spurious products, as bad as all possible combinations of sums and differences between the harmonics of those signals.

So if I want to change, say, a 2GHz radio signal to 6GHz, I put the 2GHz signal in, put in a 4GHz oscillator, and I get all sorts of stuff out. Most of it's useless, but unless I have a spur showing up right where I want my new RF band, I can put that output into a bandpass filter, get clean output, and I've magically moved my radio to a different band.

So here's the thing... your average amplifier doesn't have a filter, and is not linear much beyond 20kHz. So when you feed that 96kHz signal into the amplifier -- and think, it's music, there are dozens or more different frequencies in there -- you may find all kinds of weirdness coming out. Now, sure, the sums you don't hear, the harmonics, etc. are all reduced in amplitude as you go out, but what you can get is muddy audio... just a little worse than what you might have had otherwise.

I should also point out that, if you actually have a digital amplifier, this won't happen -- that digital amplifier will have an ADC with an anti-aliasing filter in front of it (kind of the other half of the reconstruction/anti-imaging filter, ensuring you don't try to sample frequencies above the Nyquist/Shannon cutoff), so none of the higher frequency information gets in, anyway. Which of course also negates the point of the higher spec DAC, unless, as before, you have a 96kHz amplifier.

One organization very against ridiculously high sampling rates is the [Xiph.org ](http://xiph.org/)Foundation, one of the main organizations devoted to open source digital media formats. They're responsible for Vorbis audio, Theora video, the truely miserable Ogg multimedia streaming container format, and a bunch of other stuff. They kind of missed the point of Neil Young's Pono project, and the fact that in a portable player, you actually can deliver a high spec audio output without nonlinearity issues. But it's still worth a read for the general concepts.

### Da quello che si era screenato… Listening?

Listening? Not unless you’re a dolphin or bat. Maybe if you’re dealing with something from the late 70’s/early 80’s when digital technology was in its infancy, and converters were kinda crappy and reconstruction filters had longer slopes. Now? Not so much.

Here’s the thing; you’ll probably see lots of people talking about “snapshots per second” and “filling in blanks” and all that. That all stems from a misconception about how digital audio works. It’s not like a movie where your brain has to fill in pieces missing between frames; it’s really all about weird and terrifying math. What the Nyquist-Shannon theory, upon which all digital sampling is based, states is that when you pick a sampling rate and take regular samples, you have enough data to perfectly reconstruct the curves of all frequencies up to 1/2 that sampling rate. So that means that if your sampling rate is 44.1khz, you can perfectly reconstruct all frequencies up to 22.05khz, which is about 2khz above the upper limit of human hearing (and most people top out below that). (there are a few edge cases in which this doesn’t work, involving zero crossings at the sample boundaries, but that’s exceedingly rare). That 2khz is a handy slop space too for the filters that cut out aliasing noise and such.

So why does higher-rate audio exist? Well, a few reasons.

First, it’s often recorded at higher sample rates for the benefit of processing. If you’re doing a processing operation on digital audio that introduces certain kinds of noise, if you can introduce that noise incredibly far outside the range of human hearing then it’s something you don’t have to worry about cluttering up your finished product.

Second, the conversion process from a higher sample rate to a lower one is not always perfect; converting from 88.2khz to 44.1 isn’t merely a case of “dividing by 2.” So in some cases a high-sample-rate signal is left at a high sample rate just so there’s no rate conversion before it goes to analog conversion.

Of course, there are arguments to be made (often rather passionately) on both sides of these rationale; some engineers will assert that the conversion process, while imperfect, is still imperceptible to humans, and that most modern digital audio processors internally oversample, rendering the need for a higher sample rate essentially moot. Other people will tell you they certainly can hear the difference.

Honestly, though, for 99.99999% of listeners, any differences are entirely academic, because they’re not listening in an environment that is capable of differentiating any nuance. What’s the point of having a perfectly clean pristine signal if you’re listening on consumer speakers that introduce their own noise, or listening in a living room that has a 140hz z-axial room node ruining bass response? Heck, what’s the point of being able to reproduce audio up to 48khz if one to many rock shows in college left you with an upper limit of hearing at 16khz?

In sort, there *might* be benefits to high-SR audio, but there’s a lot of diminishing returns involved for the vast majority of listeners, and even for many artists and engineers.

[https://www.quora.com/Are-there-any-benefits-to-listening-to-music-sampled-higher-than-44-1-kHz](https://www.quora.com/Are-there-any-benefits-to-listening-to-music-sampled-higher-than-44-1-kHz)

**Yes and no**.

**The actual case** is that, even though you cannot *hear* above 17-18KHz (as an adult), you *are* affected by it. Numerous studies using FMRI have shown that there *is* a difference in brain activity when lsitening to a recording of extended bandwidth beyond 20KHz vs. one without.

There is also a benefit to phase relationships which (*even with a signal of 2KHz* - well within the range of hearing) are only going to be as accurate as 360(°)/(bandwidth/frequency), therefore a 2KHz tone would only attain a phase accuracy of 360/(20KHz/2KHz=10) or 36°. **Most people can hear phase differences of 30° or less**, so (based on a number of *double-blind listening* tests conducted), a statistically-above-random selection of listeners report a “better sense of placement” when played the same recording at high sample rate compared to 44.1KHz Fs.

**However**, you will only get the phase accuracy benefit if the source material was *recorded* at high sample rate - (most *isn’t*) - and the bandwidth benefit if your amplifier and speakers can reproduce frequencies beyond 20KHz - (most do *not*) - therefore the other answers are (somewhat) correct in most cases.

For most people, no.

BUT, this is because their hearing is developmentally stunted by listening to music only through studio recordings which have extensive temporal distortion. Every knob in the audio production chain introduces compounding tempero-spatial distortion , virtually no loudspeakers are minimum phase devices and most listeners are perpetually immersed in post-industrial noise pollution which inhibits the neurogenesis necessary for the finer nuances of hearing. The bad conditioning of hearing is even worse if you only listen to digital audio, worse yet if you listen to Internet music which is all file compressed.

Children given musical instruments and lessons grow 10 billion more neurons, in part to hear ten times better than the general population. Many of them can hear the difference of 96K and 192K sampling like I do.

[http://www.jneurosci.org/content/23/27/9240.full.pdf](http://www.jneurosci.org/content/23/27/9240.full.pdf+html)

Note that the increased sampling rate only matters if there has been no processing of the audio - no mixing, no panning, no equalization, no compression or gating, no added reverb and no file compression. If you stop listening to recordings and go to acoustic concerts (NO PA system), or live your life in a forest with no motorized transportation then you can hear the wonders of high sampling rates and experience a wealth of more meaning in music.
