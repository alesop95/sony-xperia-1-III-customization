# Audio and Android limitations

Il problema nasce da come Android (e LineageOS in particolare) gestisce l'audio nativamente, attraverso il mixer di sistema chiamato AudioFlinger e la HAL (Hardware Abstraction Layer). Android, di default, utilizza un Audio Mixer interno (AudioFlinger) che converte tutti i flussi audio in PCM 16bit / 48kHz, li mixa internamente, poi li passa al sistema e non garantisce bit-perfect output, a meno che non venga bypassato.

Il DAC interno (Sony Xperia 1 III) è ottimo, supporta audio ad alta risoluzione (FLAC 96kHz, DSD nativamente no). Tuttavia, a meno che il lettore audio non bypassi il mixer, anche lui subirà downsampling a 48kHz, soprattutto su Android AOSP / LineageOS. Solo su firmware Sony originale, l'Audio HAL è ottimizzato per bypass hardware. Sony, nel firmware stock (ufficiale), include un’implementazione personalizzata e ottimizzata dell’Audio HAL, che consente:

- di bypassare AudioFlinger, il mixer interno di Android;
- di mantenere intatti flussi audio ad alta risoluzione (es. 96 kHz, 192 kHz, ecc.);
- di comunicare direttamente con il DAC interno per ottenere output bit-perfect (cioè l'audio non viene convertito, ricampionato o alterato).

LineageOS si basa su AOSP (Android Open Source Project), che non include le ottimizzazioni specifiche dei produttori, tra cui:

- driver proprietari (come quello audio di Sony),
- Audio HAL avanzati,
- bypass del mixer AudioFlinger

Quindi, anche se uno ha un ottimo DAC sull’Xperia 1 II, LineageOS probabilmente non sfrutta il suo pieno potenziale, e l'audio viene ricampionato a 48kHz (anche se il file è 96kHz o 192kHz), passa sempre da AudioFlinger, perdendo qualità. 

Dunque, per ottenere un audio bit-perfect su LineageOS si può:

1. Usare il DAC interno e un’app *tentare* il bypass del mixer AudioFlinger
   1. USB Audio Player PRO (UAPP): può usare il proprio driver audio nativo (con root o DAC USB);
   1. Fiio Music Player – è un app android standalone che funziona anche senza lettori Fiio. Su DAC interno, non può bypassare il mixer, a meno di avere HAL audio Sony originale (non presente in LineageOS).
   1. Poweramp – Il modulo Hi-Res Output è integrato in Poweramp da tempo. Supporta vari DAC interni (ma solo se Android li espone correttamente tramite HAL)

Il problema è comunque che su LineageOS (e Android AOSP in generale), il supporto al DAC interno Sony non è garantito, perché mancano i driver HAL proprietari di Sony. Il rischio è che il flusso venga comunque riscalato a 48kHz, anche se il DAC interno è capace di molto di più. 

Anche Poweramp e UAPP non possono "bypassare completamente" il mixer sul DAC interno, se la HAL (cioè i driver audio del dispositivo) non lo permette. Le app possono chiedere al sistema di usare Hi-Res output, ma se la HAL è generica o incompleta (come su LineageOS), il sistema ignorerà la richiesta e forzerà l’output a 48kHz via AudioFlinger. 

Se usi il DAC interno, le app (Poweramp, UAPP, ecc.) non possono garantire bypass del mixer, a meno che la HAL del sistema esponga correttamente il supporto Hi-Res. Con LineageOS, questo quasi mai accade, perché i driver Sony sono proprietari e non redistribuiti. Se Sony nella ROM ufficiale espone via HAL che il DAC supporta 24bit/96kHz, Poweramp lo vede e può usarlo, MA se LineageOS non ha quei driver HAL, il DAC non viene riconosciuto correttamente, quindi tutto passa dal mixer, e viene sottocampionato a 48kHz, anche se usi Poweramp o UAPP. Dunque, su LineageOS o AOSP, non tutti i DAC interni sono compatibili col modulo Hi-Res, proprio per la mancanza dei driver audio Sony proprietari. Dovrai verificare direttamente nelle impostazioni: se vedi i valori >48kHz disponibili, è supportato. Altrimenti, il sistema ricade su 48kHz standard.

LineageOS 22.2-20250701-NIGHTLY-pdx215 NON ha i driver HAL audio Sony (proprietari) e il DAC verrà visto come un generico “output standard” e il mixer di Android probabilmente imposterà 48kHz come limite. La strada del DAC interno con bypass funziona solo su ROM ufficiali Sony o su ROM che implementano HAL audio proprietaria. 

Facendo infatti la prova con PowerAmp, si ha che comunque settando le impostazioni del “Wired Headset/AUX” con delle semplici cuffie Sony connesse, nonostante si è selezionato 19kHz e 24bit sia il “Sample Rate” che “Sample Format” mostrano un 48 kHz e 16 bit di output perché “Actual sample format is defined by the device”.  Usando FiiO Music 3.2.8 e volendo sapere se il flusso audio FLAC 24bit/96kHz viene riprodotto a quella risoluzione reale, la situazione è simile ma un po’ più limitata rispetto a Poweramp. FiiO Music non fornisce un log diretto, ma puoi comunque fare alcuni controlli utili. Tuttavia, FiiO Music 3.2.8 su LineageOS (specialmente su dispositivi non FiiO) non mostra quelle opzioni perché FiiO Music attiva automaticamente il supporto Hi-Res solo sui dispositivi FiiO (es. M11, M15, ecc.) oppure su pochi telefoni Android che espongono correttamente l’HAL audio Hi-Res. LineageOS (22.2, Xperia 1 III) probabilmente non espone l’output Hi-Res tramite Audio HAL in modo compatibile con FiiO Music e un mixer standard AudioFlinger a 48kHz per tutti gli stream non esclusivi. La versione 3.2.8 di FiiO Music ha rimosso (o nascosto) molti controlli avanzati per output diretto su dispositivi non certificati. Siccome alcune versioni di FiiO Music mostrano il sample rate attivo durante la riproduzione, anche andando sulla schermata di riproduzione > tre puntini > check track info, si legge un Sample Rate di 96kHz con formato FLAC, bitrate 7231 kbps e file size: 180.0MB (per la traccia “Maxwell’s Silver Hammer (2019 mix)”). Questo significa che il file **caricato e decodificato è correttamente a 96kHz/24bit** (o simile) — cioè il player riconosce bene il formato sorgente. Questo non significa necessariamente che Android stia inviando quel segnale “puro” senza downsampling al DAC interno. Quella schermata indica il file caricato, non l’output effettivo hardware. L’app non ha una funzione di OUTPUT info e questa è la miglior info che puoi avere direttamente da FiiO Music. Molto probabilmente Android, tramite AudioFlinger, downsample a 48kHz (impostazione standard su molti dispositivi) prima di inviare al DAC interno, a meno che l’app non usi output esclusivo o bypass diretto.

Per monitorare l’output audio che passa nelle cuffie (sia interne che collegate a DAC esterno) mentre usi FiiO Music, puoi usare alcune app di terze parti che rilevano e mostrano in tempo reale il sample rate, bit depth e formato del flusso audio. da apk pure che posso scaricare per controllare che l'audio output (in questo caso sulle mie cuffie) sia effettivamente come in questo caso 24bit / 192kHz? APKPure: cerca "Audio Elements Pro". usi cuffie wired col DAC interno, voglio capire audio elements demo va bene per controllare se l'output viene downsamplato a 48kHz? Si. Avviando lo stesso file la riproduzione in FiiO Music di un file 24bit/96kHz (stessa canzone) su in e out dell’app andando “LIVE” e andando su “Audio Input” (Android In-built Engine) e “Audio Output” (Android In-built Engine) non fa selezionare sull’opzione menu sotto “Project Sample rate” qualcosa maggiore di 48000. Sto facendo i passaggi corretti? La limitazione del sample rate a 48kHz nell’app FiiO Music quando usi “Android In-built Engine” è normale e dipende da come Android gestisce l’audio nativamente.

**FiiO Music e la modalità “LIVE”**: Quando selezioni sia input che output su Android In-built, il flusso audio è gestito in modo “generalista” e quindi soggetto a queste limitazioni.

La gestione audio su Android (incluso LineageOS, che è una custom ROM ma non cambia la natura del framework audio di base) si basa su Audio HAL e kernel che, salvo patch specifiche, mantengono il limite di 48kHz per il flusso audio in tempo reale (live). LineageOS può avere migliorie o tweaking per la qualità audio, ma di norma non cambia la limitazione di sample rate nel percorso audio nativo in/out. Per il Sony Xperia 1 III (pdx215), la ROM non include driver DAC speciali o patch per bypassare il limite di 48kHz nel motore audio Android standard. Anche se il file è 24bit/96kHz, il DAC interno del Sony Xperia 1 III e il driver di Lineage OS possono limitare il sample rate massimo dell’audio in uscita tramite la pipeline audio standard di Android a 48kHz. In parole povere, il telefono o il sistema operativo non lasciano passare sample rate più alti su quella strada.

Il DAC interno del telefono, abbinato al driver audio e al framework Android (anche LineageOS), ha un limite massimo di sample rate in uscita a 48kHz per il flusso audio tradizionale. Persino un’app alternativa come Neutron, che può usare motori audio avanzati (AAudio, OpenSL ES) e può riprodurre file 24bit/96kHz, ma il segnale in uscita dal DAC interno sarà comunque downsampled a 48kHz se il driver o il sistema operativo non supportano sample rate più alti in uscita. Quindi, pur con Neutron che è una app potentissima, se non hai un DAC esterno che supporta USB Audio Class 2 o un motore audio custom che bypassa il DAC interno, sei limitato a 48kHz.

Dunque, se si vuole uscire in 96kHz o superiore devi per forza usare un DAC esterno USB compatibile. Il DAC interno è sempre il collo di bottiglia in questo scenario, indipendentemente dall’app. Per uscire >48kHz serve cambiare motore audio o uscita hardware (DAC esterno USB):

1. Usare DAC esterni USB, compatibile UAC2 (USB Audio Class 2) che sono meno vincolati dal sistema Audio HAL interno garantisce il bypass di Audioflinger. Questo perché se uno usa un DAC esterno USB, puoi selezionare un motore che sfrutti direttamente il protocollo USB per audio ad alta risoluzione (96kHz, 192kHz, etc). Insieme al DAC esterno allora si può provare:
      1. FiioMusic – lavora al meglio con DAC esterni USB. Ha supporto per Bit-perfect playback via USB DAC, DSD (nativo e DoP), MQA unfolding, Supporto file CUE, ISO SACD, ecc… È pensata per audiofili, ma non può bypassare il mixer Android sul DAC interno, se non gestito correttamente dal firmware
- Fiio Music App è progettata per funzionare principalmente con DAC esterni USB Audio Class 2 (UAC2).
      1. Poweramp – bypass del mixer se il DAC USB è compatibile.
      1. USB Audio Player PRO (UAPP) – bypass assoluto, driver proprietario
- In *questo* scenario, NON importa se la HAL è assente o limitata, perché l’audio non passa più dal sistema Android: l’app invia l’audio direttamente al DAC USB.
1. Fare una modifica avanzata sostituendo l'Audio HAL con quello estratto dal firmware Sony (richiede conoscenze tecniche, root, SELinux permissivo, ecc.); Tuttavia, non sempre funziona su LineageOS per incompatibilità con il kernel

In particolare, utilizzando DAC esterni, Android riconosce i DAC USB UAC2 come schede audio dedicate. Utilizzando lettori compatibili con "bit-perfect mode" (es. Fiio, Poweramp, USB Audio Player Pro), si può bypassare completamente il mixer di Android e inviare il segnale audio nativo (24bit/96kHz, DSD, ecc.) direttamente al DAC. Il vantaggio di un DAC esterno è quindi reale solo se il player lo supporta in bit-perfect mode. 

Poweramp ha un modulo Hi-Res Output, compatibile con diversi DAC interni e USB ma il bypass non è garantito su LineageOS. 

## The need of a specific app too

USB Audio Player PRO (UAPP) is the only Android app that includes a proprietary USB audio driver (its own USB audio driver (not relying on Android's stock audio stack)) and bypasses the Android mixer, enabling bit-perfect output. And bit-perfect bypass only works with external USB DACs, not internal DAC. UAPP supports bit-perfect output, DSD, MQA, exclusive mode – only on external USB DACs. When using the internal DAC (the phone’s 3.5 mm jack or speakers) UAPP cannot bypass the internal Android mixer and still passes through Android’s built-in resampler, DSP, and volume stages — not bit-perfect. UAPP is the only way to guarantee a truly clean, bit-perfect signal chain on Android, but only via USB DACs.

In the audio field, some music players such as Fiio Music Player [https://www.fiio.com/app](https://www.fiio.com/app) and Poweramp [https://powerampapp.com/it/](https://powerampapp.com/it/) are compatible and performing with external DACs. For high-fidelity audio playback, the Fiio Music App is recommended, compatible with external DACs (USB audio class compliant) capable of handling very high resolution files, including DSD512 and MQA 96kHz [https://www.fiio.com/newsinfo/877925.html](https://www.fiio.com/newsinfo/877925.html). FiiO Music *can* work with external DACs, but still uses the Android audio system (AudioTrack or OpenSL ES), which cannot bypass the Android mixer – no exclusive mode. Let’s dive into a deeper comparison:

| **Feature / App** | **UAPP** | **FiiO Music** | **Poweramp** |
| --- | --- | --- | --- |
| USB driver bypass | ✅ Yes – proprietary driver | ❌ No – uses Android’s standard API | ❌ No – Android AudioTrack |
| Bit-perfect output | ✅ Yes – full support | ❌ Not guaranteed | ❌ Not possible via USB |
| External DAC support | ✅ Full, all formats incl. DSD/MQA | ✅ Yes, even DSD/MQA (but not bit-perfect) | ⚠️ Limited |
| Exclusive mode | ✅ Yes | ❌ No | ❌ No |
| DSD native / DoP | ✅ Native and DoP supported | ✅ Native (via USB DAC), but mixed | ⚠️ Limited |
| MQA | ✅ Full decode + render | ✅ Only for MQA 96kHz, partial | ⚠️ Not officially supported |
| Mixer bypass (USB only) | ✅ Yes | ❌ No | ❌ No |

What FiiO Music really does is optimizing for for FiiO’s own DAPs and DACs, like the FiiO K9, BTR7, Q15, etc. It can send high-res audio to a USB DAC using Android APIs, but that’s not exclusive or guaranteed to be untouched (sample rate conversion may still apply).

The old Sony Music player was deeply integrated into their Android ROM and could support Hi-Res playback, but only with the internal DAC. There's no mixer bypass or bit-perfect path for external DACs with the stock Sony Music app. APKs on XDA Forums are outdated and do not support UAC2 features fully.

![](assets/img-0009.png)

If you're using a Questyle M15, FiiO KA5, or similar DAC and want bit-perfect audio, depending on apps using Android’s mixer (like FiiO Music or Poweramp) for critical listening must be avoided and UAPP [https://www.extreamsd.com/index.php/products/usb-audio-player-pro](https://www.extreamsd.com/index.php/products/usb-audio-player-pro) is the choice. 

LineageOS has USB Audio Class 2 (UAC2) support natively (just like stock android), and one can enable clean, bit-perfect streaming (DSD/PCM up to 384 kHz) without proprietary Android audio services interfering. All of this with a cleaner kernel, no bloatware.

   - Stock Android (from Android 5.0+), including Sony’s ROM has supported UAC2 since Android 5.0 (Lollipop), thus including USB Audio Class 2.0, but still routes audio through the Android mixer (AudioFlinger) introducing resampling, DSP, no bit-perfect as clearly discussed

It must be clarified that USB Audio Class 2.0 is a universal USB *standard* (not Android-specific) which enables asynchronous 24/32-bit audio, high sample rates (up to 384 kHz or more).It is supported natively by Linux, macOS, iOS, and *partially* in Android. USB Audio Class 2 (UAC2) is enabled and supported in LineageOS, but just like in stock Android, it still needs a compatible app (like USB Audio Player PRO) to deliver bit-perfect audio because it still does not bypass the Android audio stack by itself. Even with LineageOS, this does not give a bit-perfect playback on its own, but bit-perfect output over USB still requires a player like USB Audio Player PRO that uses its own USB driver – because Android doesn’t allow full control of the audio stack by default.

What’s more is that Sony’s stock Android might add extra processing (e.g., DSEE HX, ClearAudio+, Dolby), interfering with fidelity and also for this reason LineageOS is preferred because it’s cleaner, minimal and removes forced DSP for sure and allows direct control over audio devices via kernel (UAC2 passthrough is possible). Lineage OS can work better with apps like USB Audio Player PRO that need raw access to USB endpoints: while USB Audio Class 2 is not exclusive to LineageOS, using it allows for better transparency and less interference with external DACs, as long as kernel and app support it.

### UAPP on the Xperia

One can buy somewhere a UAPP app lifetime and extract tha .apk to run it on Sony Xperia 1 III. As a matter of fact, technically yes, legally no. When one buys USB Audio Player PRO from the Google Play Store, the app verifies the Google account license using Play Store DRM. This is how UAPP Licensing System works. If the license is valid, the app runs. If not (e.g., the app was sideloaded without purchase, or used on an account that never bought it), the app refuses to start or limits functionality. If the .apk is extracted and installed on another device without Play Store access, it will install but either refuse to launch or run in demo/limited mode, without the proprietary USB audio driver or high-res output.

UAPP also offers a direct purchase license via their website [https://www.extreamsd.com/index.php/products/usb-audio-player-pro](https://www.extreamsd.com/index.php/products/usb-audio-player-pro)   (using PayPal), which provides an APK + license file that works outside of Play Store. This license is portable across devices, but still personal (not meant for sharing). This version therefore does not require Play Store and is portable on all your personal Android devices (you can copy and install it anywhere, just include the license file).

Going to the dedicated forum [https://www.extreamsd.com/forum/forum-22.html](https://www.extreamsd.com/forum/forum-22.html) the section "Using UAPP on smartphone without Google Services" you found an email and:

![](assets/img-0010.png)

Then the reply:

![](assets/img-0011.png)

And the doubt:

![](assets/img-0012.png)

![](assets/img-0013.png)

Going to [https://consumer.huawei.com/en/mobileservices/appgallery/](https://consumer.huawei.com/en/mobileservices/appgallery/) and scanning the QR code with the android device:

![](assets/img-0014.png)

And a pop-up appears with “Do you want to download com.huawei.appmarket.2311221502.apk”. Opening the app says “The following categories of information will be collected and used in order to provide you with this service:

- HUAWEI ID information
- Such as nickname and profile picture
- Device information
- Such as device identifier
- Network information
- Such as IP address
- Usage information
- Such as the list of installed apps and reviews

And other irrilevant information for this purpose. Then is says: “This app requires the following permissions:

- Internet
- For you to access online services
- Phone
- For us to obtain device information

And the AppGallery User Agreement was accepted. The UAPP app installed is the 7.0.7.0 version. 

Sulla PRIVACY POLICY says “USB Audio Player PRO …

“I CONSENT” 

(vedi screen sony xperia)

INSTALL le feature HMS Core 

Installata HMS core app

Registering a new Huawei ID requires two-factor verification. Huawei can do it via SMS or email. The Huawei ID app or AppGallery sometimes requires a phone number for the first login, although you can only use email later. Se lo scopo è solo comprare UAPP e trasferire la licenza, conviene registrarsi via email su PC e poi usare quell’account sul telefono senza SIM. In questo modo non si tocca mai la verifica via SMS. 

Once Huawei ID account is created one can go on by logging-in only with mail and password. Going on:

![](assets/img-0015.png) ![](assets/img-0016.png)

In the meantime check the reddit post [https://www.reddit.com/r/usbaudioplayerpro/comments/1mfq30i/comment/n6o9omr/?context=3](https://www.reddit.com/r/usbaudioplayerpro/comments/1mfq30i/comment/n6o9omr/?context=3) out. 

#### Steps

Iniziando gli step di installazione dal Sony Xperia 1 III:

![](assets/img-0017.png) ![](assets/img-0018.png)

E poi:

![](assets/img-0019.png)  ![](assets/img-0020.png)  ![](assets/img-0021.png)

E:

![](assets/img-0022.png)

At a certan point the procedure says “Some features in USB Audio Player PRO rely on HMS Core to work properly.”. USB Audio Player PRO (UAPP) on Android can use certain Huawei Mobile Services (HMS) Core features for licensing and streaming integration, but only if you install the Huawei AppGallery version or you’re using a Huawei device.

On LineageOS without Google Play, if you sideloaded the Huawei version, you must install HMS Core to unlock full functionality. Local playback and basic USB DAC operation are unaffected either way.

UAPP’s core USB audio driver is completely independent of HMS Core or Google Play Services:

- It talks directly to your USB DAC over USB using its own native code.
- All bit‑perfect playback, DoP, native DSD, and high‑rate PCM will work normally without HMS Core.
- This is true even on a totally de‑Googled LineageOS.

The only exception: if you’re using a streaming service inside UAPP that’s implemented with Huawei’s SDK (mostly in the Huawei AppGallery build), you might lose that streaming integration, but local files and direct DAC output are fine. That’s handled by UAPP’s own driver, not HMS.

##### The in-app purchase

If one downloads USB Audio player from Huawei media gallery and buy the app from an in-app purchase and associate it with a device without google services, where does the license go? UAPP, when downloaded from Huawei AppGallery, does not use Google Play Licensing. The license is managed directly by the developers (eXtream Software Development) through:

- Internal license token saved to the app's internal storage.
- Pairing with your Huawei ID (if you purchase via Huawei IAP) or with an internal eXtream account if you use their activation system (in some cases the in-app purchase verified by their servers is enough).

This means that:

- It doesn't depend on Google Play → you can use it on devices without GMS.
- The license remains valid even if you reinstall the app on the same device or another where you have the same Huawei ID or manually transfer the license file (if provided by them).

Doing a total reset without a backup of the UAPP data folder and without the same Huawei ID, may make necessary the re-activation.

#### Further useful concepts

##### Why no modding can replicate UAPP behavior

There is no complete modding for LineageOS able to replicates UAPP behavior in Sony Xperia 1 III (pdx215) with LineageOS 22.2.

UAPP bypasses Android’s built-in AudioFlinger / mixer / resampler by using a *custom* USB driver built into the app. It communicates *directly with the DAC in exclusive mode* (bit-perfect PCM/DSD). On LineageOS (including 22.1/22.2 for Xperia pdx215) there is no system mod that fully replicates this without deep-level kernel changes or rewriting Android's audio HAL. Rooted mods (like AudioPolicyManager, AdvancedAudioMod, or certain Magisk modules) may improve audio routing or allow hi-res *internal* DAC usage, but:

- These do not replace the UAPP USB driver
- They do not enable DSD over DoP or exclusive USB access
- They are device-specific and can cause instability

The best current practice is to stick to UAPP for bit-perfect USB output: on LineageOS, this works great due to fewer background audio interferences.

But if could exist a way with system mod that fully replicates this without deep-level kernel changes or rewriting Android's audio HAL, still UAPP would be needed, since the audio HAL alone wouldn't be enough, correct. 

Even if a system-level mod replicates or replaces Android's Audio HAL, you’d still need something like UAPP (or similar app with its own USB audio stack), because the HAL alone is not enough for full bit-perfect USB output, especially with external DACs. The Audio HAL is responsible for connecting Android's internal audio pipeline (AudioFlinger, AAudio, etc.) to the *actual* hardware (e.g., DAC, codec). Modifying the HAL (or using a more transparent version) can help internal DACs, such as enabling:

- Higher sample rates
- Direct path to onboard DACs (bypassing software resamplers)

However, external USB DACs are handled separately. Android doesn't natively give exclusive, low-latency access to USB DACs and audio goes through the system mixer, it's often resampled or altered unless explicitly bypassed and no DoP (DSD over PCM), no direct DSD. 

What UAPP does that's unique is:

- Bypasses AudioFlinger / MediaServer completely
- Uses a proprietary USB audio driver inside the app
- Enables:
   - Bit-perfect PCM
   - DoP / Native DSD
   - MQA passthrough
   - Direct DAC handshake / driver config

Think of the Audio HAL as a high-quality sound card driver, and UAPP as an app that bypasses the operating system to talk directly to your external DAC, something like using ASIO in Windows, bypassing the mixer

Even if your ROM used a "perfect" HAL (which would mostly affect internal DAC), you still wouldn't get that direct USB control without an app that speaks USB Audio Class protocols on its own, like UAPP.

##### Without UAPP and internal DAC

Modifying or improving the Audio HAL can help internal DACs without UAPP, but this applies only to the internal DAC (the one inside the phone), not to external USB DACs. We understood that Android resamples all audio to 48 kHz using AudioFlinger (even FLAC at 96 kHz will get downsampled to 48 kHz losing resolution).

A custom ROM with a patched or transparent Audio HAL (e.g., in LineageOS or custom kernels) can allow:

- Hi-Res output from internal DAC (e.g., 96 or 192 kHz)
- Lower latency
- Bypass of mixer effects
- Cleaner sound closer to bit-perfect

This does not need UAPP because it just depends on the ROM/kernel/HAL. Modded HAL helps *internal* DACs.

Once you flash LineageOS, the stock Sony HAL (which enables high-quality internal DAC control) is typically replaced with a generic AOSP HAL. And that changes the game:

- Sony's proprietary audio stack is gone.
- Lineage uses AOSP's generic Audio HAL, which only exposes basic 16-bit/48 kHz audio paths.
- Hi-Res playback via internal DAC is lost unless a modded HAL is re-integrated manually (very complex).
- Even if you patch the system to allow hi-res routing, without Sony’s drivers the internal DAC won’t actually work in hi-res mode.

Patching or Re-adding the Sony HAL to LineageOS is very advanced and one needs to extract Sony’s proprietary audio blobs from the stock ROM and reverse-engineer or re-integrate them into the LineageOS device tree. This is very complex (especially on newer Android versions like 13+) and is not guaranteed to succeed unless someone already made a custom ROM with Sony audio HAL ported in (check XDA).

If you're running LineageOS, forget about using the internal DAC for audiophile-grade playback. Use an external USB DAC + UAPP or equivalent bypassing all Android audio limits is the best option. This is the most reliable and audiophile-grade setup: works great with LineageOS, even without Sony HAL.
