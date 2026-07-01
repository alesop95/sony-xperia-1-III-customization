# Why an external DAC?

First at all, external DACs are not controlled by the Audio HAL, they are handled by Android’s USB audio stack, which always goes through the Android mixer, unless bypassed by an app like UAPP.

UAPP has two output modes:

1. Android Audio API standard that goes through AudioFlinger, so no bypass.
1. Direct USB Driver (UAPP proprietary) that communicates directly with an external USB DAC via isochronous USB endpoint, completely bypassing AudioFlinger and the Android pipeline.

The internal DAC (Qualcomm WCD9385) is not exposed via USB and is not accessible by UAPP with its direct driver. To bypass AudioFlinger on the internal DAC you would need:

1. Access to the ALSA driver via NDK/low-level access.
1. Kernel support for raw direct_pcm or interface (usually not enabled on generic AOSP builds).

LineageOS doesn't include any official APIs for this, and UAPP doesn't implement direct drivers for the Qualcomm internal DAC. In summary:

| **Configuration** | **Internal DAC** | **External USB DAC** |
| --- | --- | --- |
| Stock Android | ❌ Resampled | ❌ Resampled |
| Modified Audio HAL | ✅ Clean, hi-res possible | ❌ No effect |
| UAPP or similar app | 🚫 Not needed | ✅ Full bypass, bit-perfect |
| Modified Audio HAL + UAPP | ✅ Best-case | ✅ Best-case (for DACs that support it) |

UAPP on Xperia 1 III with LineageOS 22 (pdx215) without Sony HAL: on stock firmware, Sony has a proprietary audio implementation that includes optimizations and partial bypasses of AudioFlinger for certain modes (e.g. Direct PCM to internal DAC). LineageOS typically uses generic AOSP Audio HAL, and everything goes through AudioFlinger unless an app uses direct drivers/paths (and the kernel supports it).

You can only use UAPP to bypass AudioFlinger with external USB DACs: you can't do it with your Xperia 1 III's internal DAC on LineageOS 22 without Sony HAL and without custom kernel/driver patches.

The Sony Xperia 1 III already has an internal DAC of excellent quality and with a 3.5mm jack output, enough for use with high-end headphones and 96kHz FLAC files. So, what’s the real advantage of installing LineageOS instead of using the stock Android firmware and the internal DAC of the Xperia 1 III?

- The internal phone DAC/amp (Xperia’s built-in 3.5 mm output) is decently good but still has limits: shared ground, higher noise floor, lower voltage headroom, and often analog jitter.
- External USB DACs (like Questyle M15) bypass the phone’s internal audio path, giving you better isolation, lower distortion, and higher output power through the balanced output.
   - UAPP is required for bit-perfect external USB DAC playback.

Essentially, one gets a transparent, neutral, and audiophile-grade pipeline instead of phone audio hardware limitations. We must also remember that using "bit-perfect mode" compatible players (e.g. Fiio, Poweramp, USB Audio Player Pro), you can bypass the Android mixer completely and send the native audio signal (24bit/96kHz, DSD, etc.) directly to the DAC. The advantage of an external DAC is therefore only real if the player supports it in bit-perfect mode.

Moreover, when plugging an external DAC to the phone, it must be noticed that the phone acts only as an audio source. One could just buy a standalone DAC/music player and plug headphones directly into it. In the setups we are about to describe, the Sony Xperia 1 III is only used as a music source (USB audio emitter in OTG host mode). One could instead use a dedicated portable audio player or DAC/amp with onboard storage. This is different to what we usually refer to as a “DAP” (Digital Audio Player). A portable DAC/amp (like Questyle M15, FiiO KA5) is not a player, it's a converter, and needs a digital source (e.g., smartphone, tablet, PC). In that case one plays audio files directly from that device, and connect your headphones to its 4.4 mm balanced or 3.5 mm jack – bypassing the phone entirely.
