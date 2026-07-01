# (TBC) DAC + amplifier in a single USB-C powered device

Sony Xperia 1 II (pdx215) is the main source (and with LineageOS 22, therefore USB Audio Class standard), you can make a targeted selection of portable DACs/headphone amplifiers compatible via USB-C (OTG) and capable of driving high-impedance headphones. First, you need to check that USB OTG is active in Lineage (almost always yes).

Then, for high impedance headphones (e.g. 250–600Ω) one needs sufficient voltage >2Vrms, power >100mW into 300Ω. Here's a clear, detailed table, listing the best DAC + headphone amp combos for use with a Sony Xperia 1 II running LineageOS 22, with pros, cons, power capabilities, and special notes like external power requirements.

| **Model** | **Balanced Output** | **Power @ 300Ω** | **Price (€)** | **Pros** | **Cons** | **External Power Note** |
| --- | --- | --- | --- | --- | --- | --- |
| **iFi GO Bar** | ❌
(SE only) | ~120mW | 270–300 | Top-tier sound quality, powerful, iEMatch, XBass+/XSpace features | No balanced output, expensive, high power draw | ⚠️ Might require Y-cable for stable power |
| **Questyle M15** | ✅ (4.4mm) | ~195mW | 200–250 | Clean, detailed sound, powerful current-mode amp, premium build | Slightly bulky, gets warm | ⚠️ Medium draw; borderline for phone power |
| **FiiO KA5** | ✅ (4.4mm) | ~120mW | 130–150 | OLED screen, buttons, great performance/price ratio, portable | No volume knob, 4.4mm cable fragile | ✅ Generally OK without external power |
| **MoonRiver 2** | ✅ (4.4mm) | ~110–120mW | 110–130 | Smooth, organic sound, small form factor | No controls or display, minimalistic design | ✅ Good for direct phone use |
| **Shanling UA2+** | ✅ (2.5mm) | ~80mW | 80–100 | Great budget option, compact, warm sound | Not enough power for 300Ω+ headphones | ✅ Low draw; fully phone-friendly |

These are all eligible for a USB-C, portable, audiophile-friendly configuration. However, The iFi GO Bar does NOT have a balanced output—it only outputs single-ended (SE) signal via a 3.5mm jack. This means you can’t connect it to balanced headphones or use balanced cables from it but it compensates by delivering very high voltage on the SE output, enough to drive high-impedance headphones well.

Considering the Sabre ES9023 DAC chip, a very popular, widely used DAC integrated circuit—let’s see where it stands in comparison and what it means in the context of these DAC/amp choices. First at all, a Sabre ES9023 Overview:

- Manufacturer: ESS Technology
- Type: 24-bit, up to 192kHz PCM DAC
- Architecture: Traditional delta-sigma DAC, known for smooth, musical sound with low distortion and good dynamic range
- Typical use: Entry to mid-level DACs, portable DAC/amps, some mid-fi desktop devices

ES9023 is commonly found in the Portable DAC/amps around €100–€200 FiiO K3, some Creative Sound Blaster models, earlier Shanling models and is often paired with budget-friendly headphone amps.

| **Feature / DAC Model** | **iFi GO Bar** | **Questyle M15** | **FiiO KA5 (likely ES9038Q2M)** | **MoonRiver 2 (likely ESS variant)** | **Shanling UA2+ (likely ES9023)** |
| --- | --- | --- | --- | --- | --- |
| **DAC Chip** | Burr-Brown True Native | Custom/ES | ESS ES9038Q2M | ESS variant (exact TBD) | ESS ES9023 |
| **Max sample rate** | 384kHz PCM / DSD256 | 384kHz PCM / DSD512 | 768kHz PCM / DSD512 | 384kHz PCM (probably) | 192kHz PCM |
| **Bit depth** | 32-bit | 32-bit | 32-bit | 32-bit | 24-bit |
| **DSD support** | Yes | Yes | Yes | Likely yes | No |
| **Dynamic range (dB)** | ~120+ | High | ~120 | High | ~112 |
| **Power consumption** | Higher | Medium | Medium | Medium | Low |
| **Audio quality tier** | Audiophile / High-end | Audiophile / High-end | Upper Mid-Fi / Audiophile | Upper Mid-Fi | Entry / Mid-Fi |

The Sabre ES9023 is a solid DAC chip for **entry to mid-level DACs**, offering clean, detailed sound but without the extended dynamic range, high sample rate, or native DSD support of higher-end ESS chips like the ES9038Q2M or Burr-Brown chips in iFi. It is perfectly capable for portable use, especially if your listening preferences and headphone match well. However, in a direct comparison with higher-end DACs like iFi GO Bar or Questyle M15, the ES9023 may sound slightly less detailed, less resolving, and with less “air” on top-end frequencies. The ES9023 often pairs with amps that have lower power output, so one needs to consider the headphone impedance carefully.

If one wants to achieve top-tier fidelity and drive power for high-impedance headphones, go for devices with higher-end DAC chips and strong amps (like iFi GO Bar, Questyle M15). If one wants to achieve good quality in a budget or mid-range setup, the Shanling UA2+ (with ES9023) is a very solid and compact choice, perfect for headphones up to about 250Ω

## The power problem with demanding DACs

First at all, it is mandatory to spend some words about the fact that impedance alone doesn’t determine the need for balanced output; driver technology and sensitivity do too. For example, headphones like Sundara and Clear Mg *act like* “high-end” headphones and pair well with balanced amps, even if their impedance is moderate. Then, IF one wants strictly “high-impedance” headphones (300Ω+), the best are Sennheiser HD600/660S or Beyerdynamic DT880 250Ω (borderline), which *do demand* more voltage and power and absolutely benefit from balanced output, and this is a scenario where more power is mandatory and may become a bottleneck.

Some DACs can consume more power than the phone delivers via USB: if one wants to use "heavy" DACs like the iFi, also a USB dongle with external power (Y-cable, DAC + charging) must be considered. 

For FiiO KA5 or MoonRiver 2, usually no external power is needed because power draw is moderate. For low or medium-power DACs like FiiO KA5 or MoonRiver 2 the standard connection (no external power) is:

[ Sony Xperia 1 III ] ────USB-C────▶ [ DAC/Amp ] ────▶ [ Headphones ]

The phone powers the DAC through USB-C and the DAC converts digital audio to analog and amplifies it and one plugs the headphones in the DAC. The DAC power draw is low (e.g., FiiO KA5: ~200–300mA) and is a “casual” listening with no DSD/Hi-Res overload. The battery drain on phone is tolerable.

Sony Xperia 1 II provides USB-C (USB-C 3.2 Gen 1) audio output with USB Audio Class 2 support, but phone USB power output through the port is limited (usually 5V @ ~500mA = 2.5W max) and the DAC may ask 600–800mA or even more. But power-hungry DAC/amps (like iFi GO Bar, Questyle M15) can draw more current than the phone can supply, causing distortion or disconnections or even the DAC may not turn on or drain the phone battery very fast. In such cases, what to do is:

1. Use an external USB-C Y-cable (OTG + charging cable) to power the DAC externally while connected to your phone. Recommended products are:
   1. **USB-C OTG + Charging Y-Cable**: UGREEN USB-C OTG Y-Cable (Audio + Charging) - Price: ~€12–€18
   1. **Power Source** options:
      1. Anker PowerCore PD 10000mAh (Power bank) – Delivers clean 5V/2A power (Price ~35€)
      1. Anker Nano II 30W or 45W USB-C Charger (Wall adapter) – Compact and reliable (Price: ~€25–30)
   1. **USB-C to USB-C Cable (DAC to Y-cable)**: if the DAC doesn’t come with a short USB-C cable, use:
      1. Cable Matters USB-C Gen2 cable (short, 20–30cm) – Shielded, data + power (Price: ~€10–15)
1. Use a powered USB hub or DAC with *its own power supply*.

In case a) to avoid overloading the phone, one can feed external power to the DAC while still sending audio from the phone. The Y-cable setup (OTG + charging) is the following:

                      +-----------------------------+
                      |      Alimentatore USB-C     |
                      | (es. >5V 2A - Power Supply) |
                      | (Wall adapter / Power bank  |
                      +-------------+---------------+
                                    |
                                    v
                     +-------------+-------------+
                     |         power IN          |  <-- Power only (no data)
                     |     [Femmina USB-C/Micro] |
                     +-------------+-------------+
                                   |
                                   |
                             (Y-Cable OTG)
                                   |
          +------------------------+------------------------+
          |                                                 |
          v                                                 v
+--------------------------+                 +----------------------------+
|      Sony Xperia 1 III   |                 |  External DAC USB Hi-Fi    |
|        (USB-C host)      |                 |          (USB powered)     |
|  USB audio Data + OTG	 |		      |      (amp combo)           |
|  OTG attivo → modalità   |                 | Richiede più corrente di   |
|  host (USB host mode)    |                 | quella fornita da Xperia   |
+--------------------------+                 +----------------------------+

       [USB-C **male**]                          		 [USB-A **female**]
       (ramo dati/host)                          (ramo dati + power out)

      │                                                     ▲
      └──── ── ── ── ── ── [ USB-C Audio Data ]── ──────────┘
                   							 │
                                                  analog OUT balanced 4.4mm

                        						│
              					    **Balanced** 4.4mm **Cable**
                  			    			       │
     			   		 [ High-impedance Analog Headphones balanced 4.4mm ]

This way one can use a special USB-C Y-cable with the CC pin configured for host usage. One branch sends data from the phone to the DAC while the other branch sends power from a wall charger or power bank to the DAC so that the DAC has enough stable power and doesn’t drain your phone. If the DAC has an internal battery, the power branch may be optional, but it generally improves stability. Alternatively, a power bank can be considered.

A completely different setup is b) is a powered USB hub, which works almost the same way but uses a desktop-style hub:

[ Sony Xperia 1 III ]──USB-C─▶ [ Powered USB Hub ] ─▶ [ DAC ] ─▶ [ Headphones ]
                                         ▲
                                 [ Power adapter ]

This is a configuration that works best for desktop listening anyway thus being less portable. 

The Sony Xperia 1 II supports OTG, but does not provide enough current for high-power DACs (e.g. above ~100 mA). The Y-Cable OTG isolates power (from the power branch) from data (DAC host ↔ branch), allowing stable communication + adequate power supply. Power role del Xperia stays as a host (does not behave as a client). Therefore, putting all things together, the iFi GO Bar with USB-C + Y-cable and external power is a strongly suggested configuration. Therefore, a reasonable final connection flow is the one above.

## Combinations

### K-ARRAY Duetto-KD6B + Xperia 1 III + DAC/amp combo analysis (no)

The K-ARRAY Duetto-KD6B is a planar magnetic headphone with an impedance around 30–40Ω (very manageable), known for clear, detailed sound but tends to be a bit bright due to planar timbre. The key points here are:

- Impedance: Low to moderate (~30–40Ω) → easy to drive
- Sensitivity: Medium-high → doesn’t require massive power
- Planar magnetic drivers: Need clean, low distortion amplification to avoid harshness

For a neutral target one needs to avoid overly warm or colored amps/DACs in favor of a clean, transparent sound.

| **Model** | **Balanced Output** | **Power @ 32Ω** | **Sound Signature** | **Why it's a match for Duetto-KD6B** | **Price (€)** |
| --- | --- | --- | --- | --- | --- |
| **FiiO KA5** | Yes (4.4mm) | ~265mW | Clean, neutral, slightly analytical | Powerful enough, clean ESS DAC, balanced out | 130–150 |
| **MoonRiver 2** | Yes (4.4mm) | ~250mW | Natural, smooth, neutral | Very transparent, non-fatiguing, musical | 110–130 |
| **Shanling UA2+** | Yes (2.5mm) | ~190mW | Slightly warm, smooth | Budget-friendly, good clarity, less power | 80–100 |
| **iFi GO Bar** | No (SE only) | ~475mW @ 32Ω | Neutral to slightly warm | Super powerful, very clean Burr-Brown DAC | 270–300 |

With this configuration the top pick for such a setup is FiiO KA5 or MoonRiver 2 because:

- Both have balanced outputs, cleaner signal and better noise rejection (important for planar drivers)
- Provide more than enough power at 32Ω without risk of distortion or fatigue
- Neutral and transparent sound, avoiding harshness typical of some planar drivers when paired with warm or colored amps
- Compact, portable, and fully compatible with your Sony Xperia 1 II over USB-C

Since these headphones have a low impedance, amplifier power is not a bottleneck, but clean signal and neutral DAC chips really matter here.

![](assets/img-0023.png)

The iFi GO Bar is overkill power-wise, but if budget allows, it’s a solid choice with a very refined sound stage and dynamics. The moon river 2 [https://moondroplab.com/en/products/moonriver2](https://moondroplab.com/en/products/moonriver2) is still a very good choice. 

But it is extremely important to pay attention to the fact that K-ARRAY Duetto-KD6B normally comes with single-ended cables (likely 3.5mm or 1/4" TRS). To benefit from balanced output on your DAC/amp, one needs either:

- A balanced cable designed specifically for Duetto-KD6B, with the proper connector on headphone side and a balanced plug (4.4mm Pentaconn or 2.5mm TRRS) on amp side.
- If the headphones support detachable cables with 2-pin or 3.5mm connectors, get a custom balanced cable with the right connectors.

If detachable and standard, one can order a custom balanced cable from companies like Moon Audio, Effect Audio, or Astell & Kern cables. If your headphone cable is not detachable, balanced cable use might be impossible without modding (which is complex and risky).

### The most powerful combination(s)

Assuming one wants a *new* headphone that’s neutral and high-res capable, the objectives recap is;

- Balanced output (better power, separation, lower noise) – it’s an analogue audio cable
   - The headphones have a 4.4mm balanced connector (typical for balanced Hi-Fi headphones).
   - The DAC has a balanced analog audio output (4.4 mm jack or balanced dedicated output).
   - The Balanced 4.4mm cable connects the DAC to the headphones.
- Portable DAC/amp with internal amplifier (possibly no stack, just one small unit)
   - Remember that usually a DAC only converts digital → analog, is the headphone amplifier that increases voltage/current to drive the headphones properly. A DAC/amp combo (like MoonRiver 2, FiiO KA5, Questyle M15) includes both inside a single portable device.
- USB-powered, manageable from Xperia 1 III
   - Not all USB-C Y-Cables are made correctly. They must have the DC pin configured per host, or work via a handshake chip (some DACs require this).
   - DAC must be **USB Audio Class Compliant** (most Hi-Fi DACs are).
- Neutral, detailed sound
- Headphone that fully takes advantage of balanced + a clean DAC output

As far as the connection chain is concerned, the ideal portable setup (fully-optimized) becomes, if DAC power draw is low/moderate so, as seen, with a direct USB-C or, if DAC power draw is high, a Y-cable or a powered bank must be added (see section about the power problem with demanding DACs). 

So, let’s compare again MoonRiver 2, FiiO KA5, Questyle M15, and iFi GO Bar, assuming to buy a new headphone that’s neutral and high-res capable:

| **Model** | **Balanced Output** | **Power @ 32Ω** | **Sound Signature** | **Amp Quality** | **Best Match Headphones** | **Power Draw** | **Notes** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MoonRiver 2 | ✅ (4.4mm) | ~250mW | Smooth, neutral | Transparent | HD600, Sundara, DT880 250Ω | Medium | Compact, musical, neutral warmth |
| FiiO KA5 | ✅ (4.4mm) | ~265mW | Clean, slightly bright | Neutral-detailed | Sundara, DT900 Pro X | Medium-low | OLED screen, tuning filters |
| Questyle M15 | ✅ (4.4mm) | ~195mW | Extremely accurate | Class-A-like | HD600, LCD-X, Clear Mg | Medium-high | Great for layering/detail |
| iFi GO Bar | ❌ SE only | ~475mW (SE) | Slightly warm, analog | High-power SE | Any up to 600Ω (SE) | High | No balanced, very powerful SE |

One may ask why "Power @ 32Ω" is still shown” although considering very high-impedance headphones. The reason is: because it’s the standard reference metric as the majority of portable headphones fall in the 32Ω–50Ω range. DAC manufacturers quote this number for consistent comparison to give a general sense of available output current, even though it’s not enough to judge power for high-impedance headphones. We know that in high-impedance headphones, what you really care about is voltage swing (Vrms), not current and as mentioned before, balanced outputs are better because they double voltage output over SE. A DAC that outputs 2Vrms SE / 4Vrms BAL will do better with 300Ω headphones and why we care more about balanced output than just raw "Power @ 32Ω".

However, we absolutely know now that it does worth considering headpones with high impedance. Here are balanced-compatible, portable-friendly headphones that fully exploit balanced DACs. 

| **Headphone** | **Impedance** | **Sound Signature** | **Balanced Cable?** | **Matches with** | **Notes** |
| --- | --- | --- | --- | --- | --- |
| Sennheiser HD600/650/660S | 300Ω | Natural, neutral | ✅ Available | All listed above | Benchmark neutral open-back |
| HiFiMAN Sundara | 37Ω | Flat-neutral, planar | ✅ Included | MoonRiver, KA5 | Excellent with balanced DACs |
| Beyerdynamic DT880 250Ω | 250Ω | Analytical, airy | ⚠️ Custom needed | MoonRiver, M15 | Needs control, benefits from balanced |
| Focal Clear Mg | 55Ω | Neutral-warm, detailed | ✅ Included | M15, MoonRiver | High-end portable synergy |
| Sennheiser HD 560S | 120Ω | Very neutral, wide | ✅ Aftermarket | KA5, MoonRiver | Budget reference open-back |

A clarification must be done here: HiFiMAN Sundara (37Ω) and Focal Clear Mg (55Ω) are actually low-to-mid impedance headphones, not high-impedance by traditional definition (usually 150Ω+). We are including them in a “high-impedance balanced” list because:

- They benefit tremendously from balanced output and quality amplification despite their lower impedance.
   - Their planar magnetic (Sundara) and dynamic driver (Clear Mg) designs require clean, stable power and gain, which balanced DAC/amps provide.
   - Balanced outputs reduce noise and crosstalk, enhancing detail and staging even on lower-impedance headphones.
- They’re also often recommended for portable use due to their reasonable impedance and sensitivity – easier to drive than true 300Ω headphones.

With iFi Go Bar is always recommended external power (with Y-cable or bank) while for Questyle M15 only for long sessions. For sennheiser HD600/660S (optional, if you listen very loud).

The final recommended portable balanced DAC/amp + headphone setup based on well-known detailed scheme and high-impedance headphone goal – optimized for neutral, high-res listening and external USB-C power:

If it's okay to set the external power in a portable way, the final Recommendation (best neutral, portable experience) with Sony Xperia 1 III (USB-C host) can be:

🥇 Setup A (Best Value / Portable Audiophile)

DAC/Amp: MoonRiver 2 or FiiO KA5 (balanced, musical, USB-powered)

Draw moderate power (~200–300mA @ 5V)

Power Management: No Y-cable needed

Works via compact USB-C Y-cable + small power bank (10,000mAh or less)

No bulky PSU or wall connection needed

Headphones: HiFiMAN Sundara (neutral planar, lightweight) [https://www.amazon.it/HiFiMan-Sundara-Cuffie/dp/B07BY82GLL](https://www.amazon.it/HiFiMan-Sundara-Cuffie/dp/B07BY82GLL) 

Cable: Balanced 4.4mm (comes with Sundara)

Connection: USB-C direct to Xperia 1 III

DAC/amp is compact (thumb-sized) and self-contained – one can move freely, pocket the chain, and travel.

🥈 Setup B (More analytical / reference-grade)

DAC/Amp: FiiO KA5 (OLED, filters, balanced)

Headphones: Sennheiser HD 660S or HD 600

Cable: Balanced aftermarket 4.4mm

Connection: USB-C to Xperia

Power: Optional external power supply (only for HD600 at high volumes)

Wall adapter >5V 2A (e.g., Anker 30W Nano)

Power bank with stable 5V output (portable)

For MoonRiver 2 and FiiO KA5 (DAC/amp combo (balanced output), power draw is moderate and Xperia 1 III + Y-cable + power bank works well. For Questyle M15 and iFi GO Bar, Y-cable + external power is mandatory due to higher draw.

Nonetheless, if we want a:

- Portable (pocketable) setup
- External power via Y-cable + power bank
- Analytical sound: flat, fast, neutral, detail-first
- Two setups: one premium, one value-oriented

Let’s finally build a portable, balanced, externally powered chain for stability chain from phone to headphone that drives high-impedance headphones with neutral and analytical tuning:

- ✅ Sony Xperia 1 III (USB-C, OTG host mode)
- ✅ External power via power bank or wall adapter (>5V 2A)
- ✅ Y-cable to split power and USB audio
- ✅ Portable DAC/Amp with balanced output and internal amp
- ✅ Balanced 4.4mm cable
- ✅ High-impedance headphones, flat/analytical tuning

We know that phones like the Xperia 1 III cannot deliver enough current to power DAC/amps like the M15 or GO Bar reliably and Y-cable feeds dedicated current into the DAC without overloading the phone.

The definite premium setup chain for a pocket-friendly setup, but with desktop-grade fidelity anywhere that:

- Drives high-impedance headphones
- Delivers a neutral / analytical sound signature
- Is powered stably via power bank
- Works flawlessly with your Sony Xperia 1 III

is:

  ┌─────────────────────────────┐
  │     🔋 **USB-C** **Power** **Bank**     │  ← **supplies** **5V**/**2A** (Power IN)
  └────────────┬────────────────┘
               │
               ▼
   [ POWER ONLY INPUT – USB-C Female ]
               ▲
               │
    ┌──────────┴───────────┐
    │   **USB** **OTG** **Y-CABLE**    │
    │  (OTG Splitter Hub)  │
    └────┬────────────┬────┘
         │            │
         │            │
         ▼            ▼
[ USB-C Male ]   [ USB-A Female ]
  (Data OUT)         (Data + 5V OUT)
     │                  │
     │                  └──────▶ **🔊 **Portable** **DAC**/**Amp** FiiO KA17(USB input)**
     │                               	- Receives digital audio + 5V power
     │                               	- Internal Amp + DAC chip
     ▼                                         │
📱 ****Sony Xperia 1 III (USB-C Host)****         │
   	- OTG mode                              │
   	- Sends audio                           │
(USB Audio Class compliant)                    │
                                               │
                                			 ▼
                    		 🎧 **4**.4mm **Balanced** **Output** (analog)
                       			        │
                       			        ▼
             			 ****High-Impedance** **Headphones**** (with balanced cable)

Choosing the LINDY USB-C OTG splitter is an excellent move: it's reliable, correctly wired for OTG, and compact enough for a clean portable audiophile rig. The LYNDY choice over Meenova can bu justified by some aspects:

- OTG mode support: for Lindy is confirmed proper host signaling while with Meenova some fails on host init
- 5V injection clean: here, Meenova may not negotiate power cleanly while Lindy is more designed for stable power merge
- USB C > USB A:

Moreover, LINDY seems to have a more solid molded plug, sturdy strain without flexible and fragile cable. What’s important is also that some DACs are not recognized by Meenova while Lindy was tested with FiiO, iFi and Questyle too.

![](assets/img-0024.png)

LINDY is a safer choice, more stable for power when it comes to powering and data splitting avoiding random disconnects or underpower issues. In this context, this Y-Cable has three ends:

      1. USB-C Male (→ Sony Xperia 1 III)
         - This is the data + OTG leg (tells the phone: “You’re the USB host.”)
         - When plugged in, it activates USB host mode on the Xperia.
         - It streams the digital audio from the phone to the DAC via the other leg ("I’m the boss — I’ll send the audio data downstream.")
      1. USB-A Female or USB-C Female (→ Portable DAC/Amp) – this leg receives two things:
         - The USB digital audio signal from the phone (via the Y-cable’s internal circuit).
         - The 5V power injected from the power-only leg.
- This is the data + power output leg and carries audio signal (streamed by the phone and passing through the splitter) + 5V power to the DAC. Is the main connection to the DAC/amp and acts like the "active delivery line" for both data (USB audio) and power. The audio signal from the phone is streamed through the splitter and flows to this port, arriving at the DAC.
      1. USB-C or Micro USB Female (→ Power Bank)
         - This is the power-only (input) leg which is connected to a power bank or charger
         - Injects 5V into the chain without carrying any data
         - It’s isolated from the Xperia and doesn't interfere with USB host signaling

The splitter allows the phone to act as a USB host, while avoiding underpowering the DAC – which is often the issue when connecting high-performance DAC/amps to a phone directly. This way the phone sends digital audio, the power bank feeds 5V, the DAC receives both and the headphones get clean analog audio. Therefore we need:

| Component | Type | Function |
| --- | --- | --- |
| USB-C Power Bank | Power Source (IN) | Feeds 5V to the DAC (via Y-cable) |
| LINDY OTG Y-Cable | Signal/Power Splitter | Routes USB audio to DAC, injects power |
| Sony Xperia 1 III | USB Host (OUT) | Sends digital audio (USB Audio Class 2) |
| Portable DAC + Amp | Digital + Power IN | Converts USB audio to analog, amplifies |
| Balanced Headphones | Analog OUT | Receives clean, amped analog signal |

Sony Xperia 1 III sends the USB audio stream, power bank injects 5V via the power leg of the Y-cable and the DAC/Amp receives digital audio from the phone (via OTG mode) and power from the power bank (because the phone power is not enough). The DAC/Amp converts digital to analog, amplifies, and sends signal to the headphones via 4.4mm balanced analog output.

We must remember that planars headphoned (Sundara, LCD-X) have low Ω but high current demand so balanced amp matters a lot

#### In-depth analysis for headphones (aborted)

##### Sennheiser HD 600/650/660S2

aaaaa

##### Beyerdynamic DT 880/990 Pro 250 Ω

aaaaa

##### Audio‑Technica R70x

Aaaaa

##### Beyerdynamic DT 880/990 600 Ω

Aaa

##### Audeze LCD‑2

Aaa

##### Hifiman Arya

Aaa

##### Hifiman Sundara

Aaa

##### Ananda

Aaa

##### HE6s

Aaa

##### AKG K240 DF (600 Ω)

Aaaa

##### Audeze LCD‑XC (2021)

Aaaa

##### Audeze MM‑100 (semi‑open)

Aaa

##### Dan Clark Audio Aeon 2 Closed

aaa

#### In-depth analysis for FiiO Q15 (and comparison) ❌

It does worth analyzing also the FiiO Q15 [https://share.google/qIutmlpQ3JbTMUH6y](https://share.google/qIutmlpQ3JbTMUH6y) keeping the rest of the premium setup unchanged to understand performance, portability, and whether switching devices makes sense.

About DAC chips & processing:

| **Feature** | Questyle M15 (or M15i) | FiiO Q15 |
| --- | --- | --- |
| DAC Chip | Dual ESS ES9281AC PRO (flagship class) | Dual AKM AK4499EX + AK4191 (Headphonesty, [NT Global Distribution GmbH](https://fiio-shop.de/EN/Portable-Audio/DAC-AMP/?utm_source=chatgpt.com)) |
| PCM Support | Up to 32-bit / 768 kHz | Up to 32-bit / 768 kHz (Audiophile Heaven, [qfiaudio.com](https://www.qfiaudio.com/review/fiio-q15?utm_source=chatgpt.com)) |
| DSD Support | Native DSD up to DSD256 (11.2 MHz) | Native DSD512 support (Audiophile Heaven, [qfiaudio.com](https://www.qfiaudio.com/review/fiio-q15?utm_source=chatgpt.com)) |
| MQA Support | Full unfolding supported | Yes, full MQA via XMOS engine (Headphonesty, [qfiaudio.com](https://www.qfiaudio.com/review/fiio-q15?utm_source=chatgpt.com)) |

About output power and noise floor:

| **Metric** | **Questyle M15** | **FiiO Q15** |
| --- | --- | --- |
| Balanced Output | ~2.62 Vrms @ 300 Ω (~22.6 mW); THD+N ~0.00057% | ~2.3 W @ 32 Ω, ~340 mW @ 300 Ω; THD <1% (Audiophile Heaven) |
| Noise Floor | Balanced < –130 dB | Excellent, very low (<5µV) (Audiophile Heaven) |
| Gain Levels | Fixed, clean, low noise | 5 gain modes + turbo/desktop |

The FiiO Q15 has multiple gain settings because it can adapt to:

- Ultra-sensitive IEMs (in-ear monitors): needed low gain to avoid hiss and give fine volume control.
- Moderately hard-to-drive headphones: might use mid gain.
- Very demanding full-size / planar headphones: high gain or turbo for extra voltage swing and current.
- Desktop mode: bypasses battery power limits when powered from USB-C PD (power delivery), unleashing full amplifier output continuously.

FiiO Q15 has a 4.4 mm balanced headphone output fully supporting balanced headphone connection out of the box.

The Q15 delivers massive headroom as it is able to drive even lower-sensitivity or planar headphones effortlessly. M15 is optimized for clarity and ultra-low distortion even with sensitive IEMs or high‑impedance cans.

Questyle M15 has an ultra-neutral, transparent, fast, with excellent micro-detail and image making it ideal for analytical listening and mastering use. The FiiO Q15 is rich and dynamic with smoother tonal balance. It combines analog warmth (AKM’s Verita sound) with incredible headroom and optional EQ features [https://www.headfonia.com/fiio-q15-review/4/](https://www.headfonia.com/fiio-q15-review/4/), [https://www.headphonesty.com/2024/04/fiio-q15-review/](https://www.headphonesty.com/2024/04/fiio-q15-review/), [https://www.qfiaudio.com/review/fiio-q15](https://www.qfiaudio.com/review/fiio-q15).

#### In-depth analysis for Questyle M15 ❌

The Questyle M15 is often regarded as top-tier performance in portable DAC/amp combos even though it's not the most expensive. It is also UAC2.0 compliant making it a plug-and-play choice with Android with no drivers needed working with lossless/bit-perfect apps. The Questyle M15 is not the most expensive, but it has the most technically capable amp stage, a neutral, analytical profile, an excellent scalability with external power, the support for both low- and high-impedance headphones. This makes it a reference-grade tool for audio enthusiasts and professionals, and one of the smartest buys for a premium portable setup. About what’is in the box:

   - 1 x Questyle M15 Ultra Portable USB DAC/Amplifier
   - 1 x USB Type-C to USB Type-C Low Profile Cable
   - 1 x USB Type-A to USB Type-C Low Profile Cable
   - 1 x Print Material (Instruction Manual & Guarantee Card) [https://www.hifivision.com/threads/questlye-m15-the-allrounder.90483/](https://www.hifivision.com/threads/questlye-m15-the-allrounder.90483/)

The Questyle M15 [https://www.ear-fidelity.com/questyle-m15-review/](https://www.ear-fidelity.com/questyle-m15-review/) supports PCM decoding up to 32bit/768kHz and native DSD decoding up to DSD256 (1bit 11.2MHz). It utilizes the flagship ESS ES9281AC DAC chip [https://www.reddit.com/r/headphones/comments/z03if3/questyle_m15_usb_dac_review/](https://www.reddit.com/r/headphones/comments/z03if3/questyle_m15_usb_dac_review/):

![](assets/img-0025.png)

Questyle surely did a lot of R&D for this device to maximize the performance of dual ES9281AC PRO DAC chips. The M15 is a perfect example that we can't evaluate the sound of a DAC by looking at its DAC chips and making a general statement. There are many variables when it comes to real-world performance. The engineering like implementation, combining good hardware with well-done firmware, proper amplification, and filtering differentiates the final sound. The Questyle M15 is an excellent DAC. It looks gorgeous. It sounds organic, detailed, and effortless. It has a great tonal balance and it offers precise imaging. Not many USB DACs can do that. Getting the dynamics, tonality, and technicalities right is hard. 

As a quick overview [https://www.audiophonics.fr/en/portable-dac-and-mobile/questyle-m15i-p-19563.html](https://www.audiophonics.fr/en/portable-dac-and-mobile/questyle-m15i-p-19563.html):

![](assets/img-0026.png)

When playing audio, the data status indicator will illuminate one of the following colors [https://www.hifivision.com/threads/questlye-m15-the-allrounder.90483/](https://www.hifivision.com/threads/questlye-m15-the-allrounder.90483/):

- Green: indicates the audio sample rate is 48kHz or less.
- Red: indicates hi-res lossless playback.(Hi-res lossless refers to PCM 88.2kHz~384 kHz, or DSD64~DSD256.)
- Magenta: indicates the M15 is performing the final unfold of an MQA Core stream.

Additionally, balanced cables (4.4mm TRRS) and high-impedance headphones are available via specialist retailers (e.g. Sunnara, Beyerdynamic, Sennheiser). In summary:

| **Feature** | **Measurement / Review Insight** |
| --- | --- |
| Ultra-low distortion | ~0.0003% THD+N |
| High voltage output | ~2.62 Vrms balanced into 300Ω |
| Wide bandwidth | up to ~1 MHz via Current Mode Amp |
| Frequency response | ±0.1 dB from 20 Hz–20 kHz |
| Noise floor | Balanced < –130 dB |
| Sound signature | Neutral, highly resolving, dynamic |

Questyle M15 exhibits no hiss even with sensitive IEMs, yet can drive 600Ω headphones which is a rare duality. It has an extremely flat, detailed, non-colored presentation ideal for mastering, studio, or accuracy. It is also UAC2.0 compliant making it a plug-and-play choice with Android with no drivers needed working with lossless/bit-perfect apps. 

All this makes the Questyle M15 a top-performing, portable DAC/Amp, ideal for analytical listening on high-impedance headphones while staying pocketable.

If using with different operating systems the specs required are:

- Android phone and pad: Android 5.0 and above
- PC: Win10 1803 and above
- Apple cellphone: iOS (You need to buy an OTG cable for Lightning to Type-C.)
- Apple computer: mac OS

With its minimalistic design with metal housing and transparent cover supports multiple devices including Smartphones, Tablets, Windows, and Mac systems. The Questyle M15 works as a USB DAC/amp both with mobile devices and computers (Windows, macOS, Linux): one can plug it into a computer USB port and use it instead of or alongside (for example) Scarlett audio interface, especially for headphone listening. It’s not a microphone input device, but excellent as a desktop headphone output DAC/amp (with negligible latency and ultra-low distortion [https://www.ear-fidelity.com/questyle-m15-review](https://www.ear-fidelity.com/questyle-m15-review), [https://www.audiodiscourse.com/2024/06/questyle-m15i-portable-dacamp-review](https://www.audiodiscourse.com/2024/06/questyle-m15i-portable-dacamp-review), [https://www.headfonia.com/questyle-m15-review](https://www.headfonia.com/questyle-m15-review). 

On Windows or Linux hosts, the Questyle M15 does not support Direct-DSD output unless handled via specific software and its playback path is limited (e.g. via WASAPI exclusive on Windows, ALSA quirks on Linux) [https://www.audioreviews.org/questyle-m15-review-ap/](https://www.audioreviews.org/questyle-m15-review-ap/), [https://www.personalaudionotes.com/questyle-m15](https://www.personalaudionotes.com/questyle-m15). For best results, stick with Android + UAPP for bit-perfect output.

##### Review Excerpts from Audiophiles & Experts

Across multiple reviews, it’s praised for its neutral tonality, pitch-black backgrounds, and ability to drive high-sensitivity IEMs and 300–600Ω headphones alike with ease:

“Top-class desktop-grade audio performance in a DAC that fits in the palm of your hand” 

“Clear, neutral sound with lively dynamic… excellent pace, rhythm and timing. Imaging with open spatiality. Realistic timbre with great transparency” [nobordersaudiophile.wordpress.com](https://nobordersaudiophile.wordpress.com/2022/06/10/questyle-m15-review/?utm_source=chatgpt.com)

“Probably the most immersive-sounding dongle I’ve heard… plenty of power… do not be fooled by those paper specs” [headfonics.com](https://headfonics.com/questyle-m15-review/?utm_source=chatgpt.com)

“The M15 boasts superb objective measurements… ultra-low distortion and impressively low noise floor” — Headphonesty [Questyle](https://questyleshop.com/blogs/m15/headphonesty-review-questyle-m15-liquid-gold?srsltid=AfmBOoos_IaOm2ZkIWgeTxv0lG3LAtCr80Wf3QVqiXV3as-5_JE3GZ_Z&utm_source=chatgpt.com)

World-class digital to analog conversion ESS ES9281AC DAC offers top-of-the-line decoding. The M15 features the highly acclaimed ESS ES9281AC flagship DAC, which can handle up to PCM384kHz/32bit and DSD256. It’s almost inconceivable that something as small as the M15 can process and reproduce such demanding audio formats [https://manuals.plus/questyle/m15-headphone-amplifier-mobile-lossless-dac-manual](https://manuals.plus/questyle/m15-headphone-amplifier-mobile-lossless-dac-manual).

##### The New Questyle M15i?

While the Questyle M15 and iBasso DX170 are both excellent portable audio solutions, Questyle has recently unveiled the M15i, a second-generation update to the M15. The M15i promises several enhancements. The M15i is the second-gen version – same chassis and CMA architecture but upgraded [https://bloomaudio.com/products/questyle-m15i-portable-dac?srsltid=AfmBOoqHTI2TdYJfVJnoVeECpD5llzKPKXfzjUKiRM_7CGLUDzYgitth](https://bloomaudio.com/products/questyle-m15i-portable-dac?srsltid=AfmBOoqHTI2TdYJfVJnoVeECpD5llzKPKXfzjUKiRM_7CGLUDzYgitth), [https://majorhifi.com/questyle-m15i-review/](https://majorhifi.com/questyle-m15i-review/):

Improved compatibility with iOS, Android, HarmonyOS, Windows, and macOS devices

Retains support for high-res formats and supports PCM up to 768 kHz and DSD512 (vs 384/DSD256 on the original) [https://hifigo.com/blogs/news/questyle-introduces-m12i-and-m15i?srsltid=AfmBOorFRyZX055EJ8-P7uoYJGS8pNu9gf_FFpE-h_ciYv3YsOteUotH](https://hifigo.com/blogs/news/questyle-introduces-m12i-and-m15i?srsltid=AfmBOorFRyZX055EJ8-P7uoYJGS8pNu9gf_FFpE-h_ciYv3YsOteUotH) 

Optimized power efficiency to prevent draining connected devices

Sound signature is a bit more open and extended in treble, slightly more dynamic and dimensional, while remaining highly resolving [https://majorhifi.com/questyle-m15i-review](https://majorhifi.com/questyle-m15i-review) 

Ultra-low noise floor of -130dB and distortion of 0.0003%

Like the M15, the M15i features the flagship ESS ES9281AC DAC chip and Questyle’s proprietary Current Mode Amplification technology with four amp engines. It also maintains the 3.5mm and 4.4mm headphone outputs with adjustable gain [https://fbk-photography.com/audiophile-showdown-questyle-m15-vs-ibasso-dx170](https://fbk-photography.com/audiophile-showdown-questyle-m15-vs-ibasso-dx170).

##### More technical highlights and specifications

The specs of this DAC place the M15 in desktop-grade territory, with reference-level clarity, minimal noise, and exceptional dynamic control [https://questyleshop.com/blogs/m15/headphonesty-review-questyle-m15-liquid-gold?srsltid=AfmBOoos_IaOm2ZkIWgeTxv0lG3LAtCr80Wf3QVqiXV3as-5_JE3GZ_Z](https://questyleshop.com/blogs/m15/headphonesty-review-questyle-m15-liquid-gold?srsltid=AfmBOoos_IaOm2ZkIWgeTxv0lG3LAtCr80Wf3QVqiXV3as-5_JE3GZ_Z).

Form: Portable DAC/amp (dongle)

Removable Cable: Y (USB-C)

DAC chip: ES9281AC (ESS flagship chip)

Decoding format: PCM: 32kHz – 384kHz (16/24/32Bit), DSD64 (1Bit 2.8MHz) , DSD128 (1Bit 5.6MHz), DSD256 (1Bit 11.2MHz)

PCM: the M15 can decode PCM audio files with a bit depth of 16, 24, or 32 bits, and sample rates ranging from 44.1kHz to 384kHz. 

   - DSD: it supports native DSD decoding up to DSD256, which corresponds to 11.2MHz (1 bit). This includes DSD64 (1 bit 2.8MHz), DSD128 (1 bit 5.6MHz), and DSD256 (1 bit 11.2MHz).
   - MQA: the M15 can also unfold MQA (Master Quality Authenticated) audio files, bringing users closer to the master recording quality [https://questyle.com/en/product/m15i-mobile-headphone-amplifier-with-dac/](https://questyle.com/en/product/m15i-mobile-headphone-amplifier-with-dac/)

Source Jack: 3.5mm single-ended and 4.4mm balanced

Output impedance: 3.5mm: 0.96 ohm, 4.4mm: 1.22 ohm

THD+N%: 0.0003% [https://www.hifivision.com/threads/questlye-m15-the-allrounder.90483](https://www.hifivision.com/threads/questlye-m15-the-allrounder.90483), [https://questyleshop.com/blogs/m15/headphonesty-review-questyle-m15-liquid-gold?srsltid=AfmBOoos_IaOm2ZkIWgeTxv0lG3LAtCr80Wf3QVqiXV3as-5_JE3GZ_Z](https://questyleshop.com/blogs/m15/headphonesty-review-questyle-m15-liquid-gold?srsltid=AfmBOoos_IaOm2ZkIWgeTxv0lG3LAtCr80Wf3QVqiXV3as-5_JE3GZ_Z)

Frequency Response (Hz): ±0.1 dB across 20 Hz – 20 kHz 

Output: 

3.5mm: RL = 300Ω, Po =1 1.97mW, Vout(Max) = 1.895Vrms,THD+N=0.00045%

4.4mm (balanced): RL = 300Ω, Po = 22.60mW, Vout(Max) = 2.624Vrms, THD+N=0.00057% [https://www.reddit.com/r/headphones/comments/z03if3/questyle_m15_usb_dac_review/](https://www.reddit.com/r/headphones/comments/z03if3/questyle_m15_usb_dac_review/)

Background noise floor (balanced): < –130 dB [https://questyleshop.com/blogs/m15/headphonesty-review-questyle-m15-liquid-gold?srsltid=AfmBOoos_IaOm2ZkIWgeTxv0lG3LAtCr80Wf3QVqiXV3as-5_JE3GZ_Z](https://questyleshop.com/blogs/m15/headphonesty-review-questyle-m15-liquid-gold?srsltid=AfmBOoos_IaOm2ZkIWgeTxv0lG3LAtCr80Wf3QVqiXV3as-5_JE3GZ_Z) for both the 3.5mm output:

![](assets/img-0027.png)

And the 4.4mm output:

![](assets/img-0028.png)

Bandwidth up to ~1 MHz, owing to Current Mode Amplification, enabling ultra-fast transients 

For a full summarized review one can check also [https://www.androidbrick.com/questyle-m15-usb-dac-review/](https://www.androidbrick.com/questyle-m15-usb-dac-review/).

##### (TBC) UAPP compatibility

USB Audio Player PRO (UAPP) is fully compatible with the Questyle M15 (and M15i) when used on Android devices. Questyle M15 is USB Audio Class 2.0 compliant and is *natively recognized*  by Android as an external DAC.

The M15’s balanced (4.4 mm) output is reputed to provide better sound quality than its single-ended 3.5 mm jack. UAPP simply passes audio to the DAC — output sound quality remains determined by the M15 hardware and headphone used.

- The Questyle M15/M15i works as a plug‑and‑play USB‑DAC for Android devices running Android 5.0/5.1 or later
- Reviews confirm that the M15’s USB interface is fully supported on Android, and it will be automatically recognized as a USB audio device when connected via USB‑C

Community reports show that UAPP successfully eliminates crackling or volume issues on Pixel and other Android devices when using external USB DACs like the Questyle M15.

There are numerous confirmations from users on Reddit and other forums that the M15 works with UAPP, and even that it is one of the best combinations for quality and stability.

The M15 relies purely on UAC2.0 (USB Audio Class 2) and no special driver, no app hack. LineageOS usually supports it too but it depends on how the specific build handles USB host mode, wheter the kernel powers the DAC properly and USB permission dialogs are handled correctly. USB Audio Player PRO (UAPP), bypasses Android’s stock audio stack entirely (AudioFlinger and resampler/mixer) because talks directly to the USB DAC using its own driver. If your kernel itself doesn’t recognize the DAC at all, UAPP can’t help: the device needs to appear in /dev/ first. In LineageOS, there’s a small chance of instability (DAC not recognized, sample rate stuck, occasional disconnects). Some people on custom ROMs reported it not enumerating only because of low-power OTG defaults but THIS is avoided with external power injection. The other rare cause is quirky USB enumeration timing usually fixed by plugging DAC after boot or using UAPP. This can happen more often custom ROMs (LineageOS included) because the USB driver is slightly different from Sony’s stock firmware and/or with some DACs like the Questyle M15 that expect a very precise handshake. In other words, if your kernel never finishes that initial USB “handshake” (enumeration), then the DAC doesn’t even show up as a connected USB audio device and Android has nothing to send audio to, so UAPP (or any app) can’t talk to it. UAPP can only take over *after* the kernel says: “Yes, I see a DAC. Here’s its USB address and capabilities.” If that never happens because of:

- Quirky USB timing
- Buggy OTG driver in the kernel
- Broken handshake sequence

then UAPP is powerless until you fix the enumeration issue (by re-plugging, changing connection order, or using a different cable/DAC).

With the build number lineage_pdx215-userdebug 15 BP1A.250505.0053439504aa9 e LineageOS version 22.2-20250701-NIGHTLY-pdx215 one can likely use the Questyle M15, but here’s the realistic assessment:

- LineageOS 22.2 inherits Android 15’s native UAC2 stack.
- Unless the maintainer for pdx215 removed or broke it, UAC2 should work.
- Xperia hardware already supports OTG host mode perfectly — the only risk is if this specific nightly has USB stack bugs

Even if the DAC gets its power from a power bank via the Y-cable,
the USB data connection still needs to enter  USB host mode (OTG mode), mantain a stable handshake with the DAC and keep the DAC awake when streaming. External power removes the current‑draw problem but doesn’t magically fix USB stack issues. Even though you’ll be feeding the M15 with external power via the LINDY OTG Y-cable + power bank, the data link still relies on kernel OTG handling.

Questyle M15, boots its DAC + Current‑Mode Amp section together, which can add delay before USB is ready. This timing quirk is what sometimes confuses Android into not seeing it until you re‑plug or power‑cycle.

##### Questyle M15 + Xperia 1 III (LineageOS) connection ritual

If one wants to make a questyle M15 + Xperia 1 III (LineageOS) connection ritual to make USB enumeration work reliably every time.

About the gear preparation:

- Sony Xperia 1 III (booted and idle – no apps playing audio).
- LINDY USB‑C OTG Y‑Cable.
- Power bank (or wall adapter, ≥5 V / 2 A).
- Questyle M15 DAC/amp.
- Balanced headphones already plugged into M15.

The connection order (important for enumeration timing):

1. Plug the M15 into the Y‑cable’s “data leg” (USB‑A female or USB‑C female, depending on your LINDY version).
1. Connect the power bank to the Y‑cable’s “power‑only leg” — this powers the DAC immediately.
1. Wait 2–3 seconds — let the M15 fully boot (its LEDs should light).
1. Now connect the Y‑cable’s USB‑C male to your Xperia.
1. Unlock phone → look for “USB device connected” notification.
1. If your ROM asks what to do with the USB device, select Use for Audio.

As a first time test:

- Open USB Audio Player PRO (UAPP) → Menu → Audio Device Info.
   - You should see Questyle M15 with PCM up to 384 kHz and DSD listed.
- Play a hi res file (96 kHz or higher).
   - LED on M15:
   - Green = ≤48 kHz
   - Red = 88.2–384 kHz
   - Magenta = MQA

If it fails to enumerate:

- Unplug only the phone connection → wait 5 sec → plug it back in.
- If still no detection → power‑cycle the M15:
   - Disconnect M15 from Y‑cable.
   - Reconnect M15 to power leg.
   - Wait 2–3 sec, then plug to phone again.

External power must boot the M15 before the phone starts the USB handshake. Waiting a couple of seconds ensures the DAC’s USB interface is “awake” when the Xperia sends the OTG host request: this avoids the quirky USB enumeration timing issue entirely.

It’s very likely to work with your LineageOS 22.2‑20250701 nightly for pdx215, but it’s not 100% guaranteed. 

Why it’s not 100% guaranteed

Nightly builds can have USB enumeration bugs or quirks in the kernel USB host driver.

If enumeration fails before the OS even knows a DAC is connected,

→ UAPP or any app won’t help — you have to fix the connection sequence (hence the “ritual”).

No one has publicly confirmed running the M15 on this exact nightly of LineageOS for pdx215, so we can only say “very probable,” not certain.

Bottom line

90% chance it will work if you follow the power‑first connection ritual I gave you.

If it doesn’t, it’s almost always a USB handshake timing issue, which is fixable by:

Changing the plug‑in order

Trying a different OTG adapter/Y‑cable

Testing with UAPP to manually re‑init the DAC

##### (TBC) Conclusions and alternatives

When buying M15 I don't want to waste money. Restoring the proprietary stock firmware would make it work for sure because Sony’s stock ROM has Sony’s proprietary USB audio driver (tuned for their DAC hardware) and mantains perfect OTG compatibility with a wide range of DACs and M15 would be recognized instantly no handshake games needed but one loses the LineageOS clean approach and tweaks you have now.

Anyway, 04/08/2025 Alessio wrote:

![](assets/img-0029.png)

![](assets/img-0030.png)

![](assets/img-0031.png)

About comparable DAC/amps with neutral, analytical, balanced output like M15 but with safer compatibility reputation one can explore the followig alternatives:

| **Model** | **Sound** | **Output** | **Pros** | **Cons** |
| --- | --- | --- | --- | --- |
| FiiO KA5 | Neutral-slightly bright | 4.4 mm balanced + 3.5 mm SE | Very stable with Android, OLED display, good power | Slightly less resolving than M15 |
| iBasso DC06 Pro | Neutral | 4.4 mm balanced + 3.5 mm SE | Great price/performance, stable USB | Not as much drive for 300–600 Ω |
| Shanling UA5 | Neutral-slightly warm | 4.4 mm balanced + 3.5 mm SE | Can run from internal battery (avoids power issues), OLED display | Larger than M15 |
| Luxury & Precision W2-131 | Neutral-bright | 4.4 mm balanced | Excellent detail retrieval, stable USB | Expensive, rarer |

We can at first exclude L&P W2-131 and iBasso DC06 Pro because Luxury & Precision W2‑13 has an excellent detail, but is very expensive for what it gives compared to M15. Slightly brighter tuning can be fatiguing with analytical chain. It has a more niche support, but is less tested with LineageOS. The iBasso DC06 Pro is a great budget performer, but provides a weaker power for 300–600 Ω headphones and less refined stage/detail compared to M15, KA5, and UA5. Is simply a good entry option, but if one aims for for top‑tier analytical is not so ideal for the main chain.

KA5 and UA5 have excellent neutral detail tuning still being very USB‑friendly with LineageOS. They offer balanced output with enough voltage for high‑impedance loads and have a stable, proven track record with UAPP and Android devices. Hence, for pure neutral + detail retrieval, KA5 and Shanling UA5 are the safest alternatives if one fears M15 quirks. They’re considered safer than the Questyle M15 on LineageOS for two reasons:

- USB behavior
- Implementation style

even though in absolute sound quality the M15 can still edge them out for micro‑detail. Even though KA5 and UA5 are safer in terms of USB handshake stability, the M15 still beats them for pure micro‑detail, transient speed, and low‑level resolution, all with a flat, neutral tonality. If your ROM handles it fine, the M15 remains the better analytical listening choice. In the meantime:

![](assets/img-0032.png)

FiiO KA5 and Shanling UA5 have very standard, conservative USB enumeration: they present themselves to the phone as a basic USB Audio Class 2 device with no unusual startup timing. That means even ROMs with slightly flaky OTG stacks (like some LineageOS builds) tend to recognize them instantly as a plug-and-play choice almost everywhere.

About the power draw handling for them, KA5 draws moderate power (~200–250 mA) — within most phones’ OTG supply limit, and even without a Y-cable, it’s fine for portable use. UA5 is unique: it can run entirely from its own internal battery in “DAC battery mode”, avoiding USB power draw almost entirely. This makes it very friendly for phones with weak OTG supply or quirky external‑power handling. M15 draws more power (~350–400 mA) when fully active, which is fine with a power bank via Y‑cable, but adds one more point where enumeration can fail if power isn’t stable.

#### In-depth analysis for Shanling UA5 ❌

The full specs sheet in M15‑style format:

- Form: Portable DAC/amp (dongle)
- Removable Cable: Yes (USB‑C)
- DAC chip: Dual ESS ES9038Q2M
- Decoding format:
   - PCM: 16/24/32‑bit, 32 kHz → 768 kHz
   - DSD: Native DSD64, DSD128, DSD256, DSD512
   - MQA: 8x hardware unfold
- Source Jack: 3.5 mm single‑ended + 4.4 mm balanced
- Output impedance: 3.5 mm: ~1 Ω, 4.4 mm: ~1.2 Ω
- THD+N: 0.00035%
- Frequency Response: ±0.2 dB (20 Hz – 20 kHz)
- Output power:
- 3.5 mm: ~137 mW @ 32 Ω
- 4.4 mm balanced: ~211 mW @ 32 Ω (~3.0 Vrms)
- Background noise floor: < –120 dB (balanced)
- Extras: OLED display, DAC battery mode (internal battery bypasses USB power), gain settings, hardware EQ modes
- Sound signature: Neutral, slightly smoother treble than KA5, very refined staging.

As a quick takeaway, this is a neural but smoother top end, unique battery mode makes it ultra‑safe for your Xperia regardless of OTG quirks.

#### In-depth analysis for FiiO KAx ✔️

The full specs sheet in M15‑style format:

- Form: Portable DAC/amp (dongle)
- Removable Cable: Yes (USB‑C)
- DAC chip: Dual Cirrus Logic CS43198
   - Decoding format:
   - PCM: 16/24/32‑bit, 32 kHz → 768 kHz
   - DSD: Native DSD64, DSD128, DSD256
   - MQA: Full 8x hardware unfold
- Source Jack: 3.5 mm single‑ended + 4.4 mm balanced
- Output impedance: 3.5 mm: ~1.2 Ω, 4.4 mm: ~1.4 Ω
- THD+N: 0.00037%
- Frequency Response: ±0.5 dB (20 Hz – 20 kHz)
- Output power:
   - 3.5 mm: ~125 mW @ 32 Ω
   - 4.4 mm balanced: ~265 mW @ 32 Ω (~3.2 Vrms)
- Background noise floor: < –118 dB (balanced)
- Extras: OLED display, gain settings (low/high), hardware volume control
- Sound signature: Neutral with slight treble lift, very clean, crisp transient response.

As a quick takeaway, this is the most plug-and-play choice, crisp neutral, slightly more “analytical sparkle” in treble.

Moreover:

![](assets/img-0033.png)  ![](assets/img-0034.png)

The KA5 works with UAPP, as confirmed by multiple users on Head-Fi & Reddit. The official driver in UAPP is designed to handle any UAC2‑compliant DAC, not only those in the list.

While FiiO KA5 and Shanling UA5 are not listed on eXtreamSD’s official device database, many reviewers and community members have confirmed they work flawlessly with USB Audio Player PRO (UAPP), based on their USB Audio Class 2 compatibility.

Assuming that one goes with FiiO KA5, this guy may even handle high impedance headphones safely (for the balanced output ~3.2 Vrms translates to ~34 mW into 300 Ω). The voltage swing is also more than enough for most high‑impedance, high‑sensitivity audiophile headphones (e.g., Sennheiser HD 600/650/660S2, Beyerdynamic DT 880/990 Pro 250 Ω, Audio‑Technica R70x). It works comfortably well for most models and the noise floor is extremely low with no hiss even with sensitive IEMs. 

Where it might start to sweat is with very inefficient 600 Ω models like Beyerdynamic DT 880/990 600 Ω in the sense that it still plays but the headroom for the extreme dynamics is reduced. Another case is with planar magnetics with low sensitivity (e.g., Hifiman Sundara, HE6se, Arya Stealth) but these require current monsters, way beyond any dongle amp.

If the goal is a premium portable rig with KA5, your safest “guaranteed performance” bet is Balanced 4.4 mm Sennheiser HD 660S2, HD 600, or HD 650 for maximum neutrality and synergy or Audio‑Technica R70x for ultra‑light, airy neutral tuning or Beyerdynamic DT 880 Pro 250 Ω if you want more treble sparkle and wide stage.

##### The final comparison with newest models

Now let’s loop back to your Sony Xperia 1 III portable chain and integrate the KA13 and KA17 into the picture. About power and driving ability:

| **Model** | **Max Balanced Output Power** | **Voltage Swing (Balanced)** | **Gain Modes** | **Size/Portability** | **Power Draw** | **Suitable for High-Impedance (>300 Ω)** |
| --- | --- | --- | --- | --- | --- | --- |
| KA5 | ~265 mW @ 32 Ω | ~4.4 V RMS | Low / High | Very pocket-friendly | Moderate | ✅ Drives 300 Ω well, borderline at 600 Ω |
| KA13 | ~550 mW @ 32 Ω | ~5.2 V RMS | Multiple | Slightly larger than KA5 | Higher | ✅ Confident with 300 Ω, better grip at 600 Ω |
| KA17 | ~650 mW @ 32 Ω | ~6.2 V RMS | Multiple + "Desktop mode" | Bigger dongle (heavier) | High | ✅ 600 Ω no problem, very high damping factor |

With KA5 one is already safe for: 

- Sennheiser HD600 / HD650 / HD660S (300 Ω)
- Beyerdynamic DT880/DT990 250 Ω or 600 Ω (at 600 Ω you’re near the limit)
- HiFimanSundara / Ananda (planar, moderate power needs)

With KA13 / KA17 

- Beyerdynamic DT880/DT990 600 Ω with full headroom
- High‑impedance studio classics like AKG K240 DF (600 Ω) or vintage 400–600 Ω loads
- More demanding planars (Audeze LCD‑2, Hifiman Arya) at decent listening levels

The KA5 remains a sweet spot for pocket use, lower power draw, no heat issues. Perfect if your target is neutral + analytical listening with 300 Ω headphones max. the KA13 is bigger, heavier, but gives extra voltage swing for peace of mind with 600 Ω or insensitive planars. The KA17 is an almost portable desktop DAC/Amp. Great if you don’t mind bulk + external power. Has "desktop mode" where it behaves like a small desktop amp — ideal for your Y‑cable + power bank setup. Of course,  Y‑Cable + Power Bank becomes more important with KA13/KA17 due to higher power draw in a portable configuration. 

The KA5 if you want maximum portability, already enough for HD600-class. KA13 is the compromise for an extra margin for 600 Ω or more headroom for planars without losing too much portability. The KA17 offers the same, with a desktop‑class power in your bag if more bulk + heat do not mind.

| **Feature** | KA5 | KA13 | KA17 |
| --- | --- | --- | --- |
| Max Output Power | ~265 mW @ 32 Ω (balanced) | ~550 mW @ 32 Ω (balanced) | ~650 mW @ 32 Ω (balanced) |
| Voltage Swing | ~4.4 V RMS | ~5.2 V RMS | ~6.2 V RMS |
| Gain Modes | Low / High | Low / High | Low / High |
| Desktop Mode | No | No | Yes |
| Dimensions (mm) | 58.5 × 25.5 × 11.5 | 61.5 × 26.5 × 11.5 | 64 × 27.7 × 12.7 |
| Weight (g) | 19.0 | 33.5 | 33.5 |
| Price (USD) | ~$149.99 | ~$149.99 | ~$149.99 |

KA17 is the largest and heaviest of the three, designed for desktop use but still portable. Due to its higher output power, it may produce more heat, especially during extended use [https://ichos-reviews.com/fiio-ka17-review](https://ichos-reviews.com/fiio-ka17-review). 

So what’s the real difference with KA13 / KA17 in terms of hardware and high-tier headphones drivability? Let’s break it down sharply and precisely:

| **Feature** | FiiO KA13 | FiiO KA17 |
| --- | --- | --- |
| DAC Chip | ESS ES9219C (mid-tier) | ESS ES9038Q2M (high-tier flagship) |
| Max Output Power | ~550 mW @ 32Ω balanced | ~650 mW @ 32Ω balanced |
| Voltage Swing | ~5.2 V RMS | ~6.2 V RMS |
| Amplifier Design | Efficient Class AB | More robust Class AB with better heat dissipation |
| Desktop Mode | No | Yes (better sustained power for desktop use) |
| Balanced Output | Yes, 4.4mm TRRRS | Yes, 4.4mm TRRRS |
| Power Consumption / Heat | Moderate (good for portable use) | Higher (heats more, heavier body) |
| Physical Size / Weight | Smaller, lighter | Larger, heavier |

The practical impact on high-tier headphones is about:

- Power & Headroom:
   - KA17 delivers higher voltage and power, making it ideal for very demanding headphones (e.g., 600Ω Beyerdynamics, some planar magnetics).
   - KA13 handles 300–600Ω headphones well but might reach its limits with super-high impedance or very low sensitivity cans at max volumes.
- Sustainability:
   - KA17 has a dedicated desktop mode, meaning it can provide sustained clean power over long listening sessions without thermal throttling.
   - KA13 is more portable-friendly but can get warm and may throttle under heavy loads if used continuously at high volume.
- Sound Quality:
   - KA17 uses a flagship DAC chip (ES9038Q2M), which tends to deliver a cleaner, more refined sound with lower distortion and noise floor.
   - KA13’s ES9219C is very capable but sits a notch below in technical specs and sound purity.

Between these two, one may choose KA13 if a powerful, very portable DAC/amp combo that comfortably drives most high-impedance headphones with good detail and neutral sound are desiderata. KA17 is only if the focus is ultimate drivability and pristine audio with the *toughest headphone:* if one wants top-tier hardware with higher sustained output, ideal for the most demanding high-impedance or planar headphones, and is okay with a bit more bulk and heat for the power gains. The KA17 is the real heavyweight champion. For a solid balance of portability and power, KA13 is excellent.

Just to have a size range the Sony Xperia 1 III, here’s the clean comparison table for dimensions and weight:

| **Device** | **Dimensions (mm)** | **Weight (g)** | **Relative to Sony Xperia 1 III** |
| --- | --- | --- | --- |
| Sony Xperia 1 III | 165 × 71 × 8.2 | ~186 | - main device |
| FiiO KA13 | 56 × 22 × 12 | ~20 | ~34% phone length, very slim |
| FiiO KA17 | 68 × 28 × 13 | ~45 | ~41% phone length, chunkier |

So in the pocket, the KA13 is barely noticeable, while the KA17 starts feeling like a small brick compared to the phone, but still much smaller than carrying a separate desktop amp.

### FiiO KA‑series model + headphones combo

Cconsidering the purchasing of a fiiO KAx model we can do an in-depth analysis for the aforementioned headphones putting all the things together with a very complete description that must lead to best choice possible. Let’s do this methodically so we can quantitatively determine which FiiO KA‑series model fits you best and which headphones will maximize your portable Sony Xperia 1 III chain without wasting power, money, or potential.

To summarize previous findings we can describe the FiiO KA‑series output power reality check as follows:

| **FiiO Model** | **Max Output (Balanced)** | **Max Output Voltage (Balanced)** | **Notes** |
| --- | --- | --- | --- |
| KA5 | ~265 mW @ 32 Ω | ~4.1 V RMS | Very capable for 300 Ω, borderline for 600 Ω at high SPL |
| KA13 | ~550 mW @ 32 Ω | ~5.2 V RMS | Stronger drive than KA5, can handle 600 Ω decently |
| KA17 | ~650 mW @ 32 Ω | ~6.2 V RMS | Strongest portable drive in KA series, ideal for hard-to-drive planars / 600 Ω dynamics |

High impedance headphones need high voltage while low‑sensitivity planars need high current. The KA5 → KA13 → KA17 evolution can be taught as increasing voltage & current delivery.

But now come the headphones requirements and synergy with KA models.

| **Model** | **Impedance / Sensitivity** | **Power Need (Balanced)** | **KA5** | **KA13** | **KA17** | **Comments** |
| --- | --- | --- | --- | --- | --- | --- |
| Sennheiser HD 600 | 300 Ω / 97 dB SPL | High voltage, moderate current | ⚠ Borderline at max volume | ✅ Good | ✅ Best | KA13 already enough, KA17 gives more headroom |
| Sennheiser HD 650 | 300 Ω / 103 dB SPL | Slightly easier than HD600 | ✅ OK | ✅ Excellent | ✅ Excellent | KA5 okay if you listen moderate-loud |
| Sennheiser HD 660S2 | 300 Ω / 104 dB SPL | Similar to HD650 | ✅ OK | ✅ Excellent | ✅ Excellent | Neutral lovers will adore with KA13/KA17 |
| Beyerdynamic DT 880 Pro 250 Ω | 250 Ω / 96 dB SPL | High voltage need | ⚠ Borderline loud | ✅ Good | ✅ Best | KA13 recommended |
| Beyerdynamic DT 990 Pro 250 Ω | 250 Ω / 96 dB SPL | High voltage need | ⚠ Borderline loud | ✅ Good | ✅ Best | Same as above |
| Audio-Technica R70x | 470 Ω / 99 dB SPL | High voltage, low current | ❌ Weak | ⚠ Acceptable | ✅ Best | KA17 recommended for dynamics & control |
| Beyerdynamic DT 880 / 990 (600 Ω) | 600 Ω / 96 dB SPL | Very high voltage | ❌ No | ⚠ Usable | ✅ Best | KA17 strongly recommended |
| Audeze LCD-2 | ~70 Ω / ~101 dB SPL | High current planar | ✅ OK | ✅ Excellent | ✅ Excellent | KA13 is fine; KA17 if you want more slam |
| Hifiman Arya | 35 Ω / 90 dB SPL | High current planar | ⚠ Slight strain | ✅ OK | ✅ Best | KA17 better for effortless headroom |
| Hifiman Sundara | 37 Ω / 94 dB SPL | Current-hungry planar | ⚠ Slight strain | ✅ OK | ✅ Best | KA13 good, KA17 excellent |
| Hifiman Ananda | 25 Ω / 103 dB SPL | Moderate planar load | ✅ OK | ✅ Excellent | ✅ Excellent | Even KA5 okay, but KA13 better |
| Hifiman HE6se | 50 Ω / 83.5 dB SPL | Extremely difficult | ❌ No | ❌ No | ⚠ Barely (not ideal) | Needs desktop amp |
| **AKG K240 DF** | 600 Ω / 88 dB SPL | Brutal voltage demand | ❌ No | ❌ No | ⚠ Barely (not ideal) | Better with true desktop amp |

Since a neutral, analytical, high‑resolution is desired and primary goal is future‑proof portability and no headphone limitations (except absolute outliers like HE6se / K240 DF):

- Go KA17: more voltage = more headroom = more control = more realistic dynamics.
- Go KA13 — enough for almost all premium headphones, cheaper, more pocket‑friendly. If you only plan to own up to 300 Ω Sennheisers or moderately demanding planars, and you want a lighter, cooler device

And the best headphone matches per model is:

- KA13 Best Match: HD600 / 650 / 660S2, DT880/990 250 Ω, LCD‑2, Sundara, Ananda
- KA17 Best Match: All of the above plus 600 Ω Beyers, Arya, R70x – with better dynamics & control

If you want the single safest purchase that will handle nearly any high‑end headphone without going desktop amp, choose KA17.

## The definitive portable kit for an audiophile

### What You’d Need to Buy (Portable Kit)

The chain described while analyzing the best combination can achieve the goal of:

- Balanced output (4.4mm)
- External power injection (power bank → DAC)
- OTG digital audio stream (Xperia → DAC)
- Analytical, neutral sound for high-end listening

So, we can confirm as a portable kit the following:

LINDY Y-Cable OTG splitter

   - Routes digital audio from Xperia → DAC while injecting 5 V power from power bank into DAC. Proper OTG wiring ensures Xperia enters USB host mode.
   - Same for both KA13 Setup and KA17 Setup

USB-C Power Bank – technically / theoretically any brand w/ USB-A out

   - Feeds DAC clean, stable power for max performance, avoiding Xperia’s limited USB power budget. Choose Anker 737 or Shargeek Storm for clean output, >20 W capacity.
   - Same for both KA13 Setup and KA17 Setup (needed)

Portable DAC/Amp: 

   - High‑resolution USB DAC + balanced headphone amplifier.
      - In the box: DAC/Amp unit, USB‑C ↔ USB‑C low‑profile cable, USB‑A ↔ USB‑C low‑profile cable, documentation
   - For FiiO KA13
      - Max 5.2 V RMS balanced
      - 550 mW @ 32 Ω
      - Best for ≤ 300 Ω dynamics & most planars
   - For FiiO KA17
      - Max 6.2 V RMS balanced
      - 650 mW @ 32 Ω
      - Drives 600 Ω Beyers, high‑current planars (Arya, LCD‑2) with ease

Balanced 4.4mm Cable: high-quality cable for the lowest noise, best channel isolation configuration

   - Connects DAC balanced output → headphone balanced input. Go for high‑purity OCC copper or pure silver for lowest resistance, max separation.
   - Brands: Effect Audio, Moon Audio, Oyaide.
   - Same for both KA13 Setup and KA17 Setup (needed)

High-impedance Headphone – balanced headphones for analytical use

   - Neutral / resolving picks:
      - 300 Ω dynamics: Sennheiser HD 600 / 650 / 660S2
      - 600 Ω: Beyerdynamic DT 880 / 990 Pro (KA17 only)
      - Planars: Hifiman Sundara, Ananda, Arya (KA17 ideal), Audeze LCD‑2
   - For FiiO KA13:
      - 300 Ω dynamics + moderate planars
   - For FiiO KA17:
      - Any from KA13 list plus 600 Ω + current‑hungry planars
1. Playback app (Android)
   - Must bypass Android audio mixer for bit‑perfect output (Best choice: USB Audio Player PRO (UAPP) – alternative: FiiO Music (lossless / DSD512 capable, good UI).)
   - Same for both KA13 Setup and KA17 Setup (needed)

All of this benefit hugely from balanced output and clean voltage. The KA17 has:

- Voltage headroom: enough to drive any headphone you’re realistically going to carry.
- Future‑proof: won’t have to worry if you later buy 600 Ω Beyers or low‑sensitivity planars.
- Still portable: slightly bulkier than KA13, but not “desktop‑amp” territory.
- Heat: warm but manageable; use external power bank to avoid heating Xperia.

For a clean, neutral, analytical chain that drives everything from 25 Ω planars to 600 Ω dynamics, fully portable with external power injection, that works on Android (LineageOS), and also Windows / Ubuntu without extra drivers, the final recommendation is Sony Xperia 1 III → LINDY OTG Y‑Cable → KA17 DAC/Amp (balanced) → OCC/Silver 4.4 mm cable → HD 660S2 / Sundara / Arya → UAPP app. Why this works:

- Balanced output (4.4 mm) → lower crosstalk, better separation, more power.
- External power injection → stable voltage, no Xperia overheating, full DAC/Amp performance.
- UAPP app → bit‑perfect PCM/DSD with LineageOS or stock Android.
- Future‑proof → KA17 lets you explore both high‑Z dynamics and inefficient planars without adding a desktop amp.
- Cross‑platform → Plug & play on Windows / Ubuntu with the same performance.

Let’s close the loop with a purchase‑ready plan in two tiers:

| **Tier** | **Component** | **Model / Recommendation** | **Approx. Price (EUR)** | **Notes** |
| --- | --- | --- | --- | --- |
| 1. OTG Splitter | LINDY USB-C OTG Y-Cable Splitter | LINDY 43158 | ~18 € | Proven OTG wiring, supports external power injection. |
| 2. Power Bank | Premium: Shargeek Storm² Slim (99Wh)Mid: Anker 737 PowerCore 24K | ~220 € / ~150 € | Clean, stable output. 737 is lighter; Storm² has display & PPS/PD tuning. |   |
| 3. Portable DAC/Amp | Premium: FiiO KA17 (Balanced 4.4 mm)Mid: FiiO KA13 | ~179 € / ~99 € | KA17 drives 600 Ω dynamics & current-hungry planars; KA13 is lighter and fine up to ~300 Ω. |   |
| 4. Balanced Cable | Effect Audio Vogue Virtuoso 4.4 mm TRRRSOyaide HPC-35HDX (custom) | ~100–150 € | OCC copper or pure silver for best separation & low resistance. |   |
| 5. Headphones | Dynamics: Sennheiser HD 660S2 (300 Ω)Planar: Hifiman Sundara / Arya / Audeze LCD-2600 Ω (KA17 only): Beyerdynamic DT 880 / 990 | ~400 – 1500 € | Choose one main set based on taste; KA17 covers all impedance cases. |   |
| 6. Android App | USB Audio Player PRO (UAPP) | ~8 € (Play Store / official site) | Bit-perfect playback, bypasses Android mixer. |   |
| 7. Storage / Source | microSDXC 512 GB (SanDisk Extreme Pro) | ~60 € | Store FLAC/DSD locally for stable playback. |   |

The premium KA17 chain costs approximately ~965 – 2000 € depending on headphone choice (all are suitable, any high-impedance dynamics up to ~600 Ω and most planars) while the mid-tier KA13 chain costs approximately ~865 – 1500 € with up to ~300 Ω and most mid‑sensitivity planars.

[ USB-**C** **Power** Bank ]  (PD / 5V ≥ 2A output)
         │
 (**Power** leg of Y-Cable)  <─── LINDY USB-**C** OTG Splitter ───>  (Data leg of Y-Cable)
         │                                                   │
         ▼                                                   ▼
   **Power** Injection                                      [ Sony Xperia 1 III ]
   (5V only)                                            (USB Host **Mode** / OTG)
                                                               │
                                                     USB-**C** Digital Audio Stream
                                                               │
                                                               ▼
                                                      [ FiiO KA17 DAC/Amp ]
                                               (Balanced 4.4 mm / SE 3.5 mm **Out**)
                                                               │
                                                       Balanced 4.4 mm Cable
                                                               │
                                                               ▼
                                                [ High-Impedance Headphones ]

We also mapped out the physical connection diagram for this exact KA17 portable chain to have a visual “how to connect” sheet when buying all the gear.

Furthermore, a SanDisk Extreme Pro microSDXC 512 GB ticks three boxes that make it perfect for the Sony Xperia 1 III + KA17 portable audio setup:

- Speed for large Hi‑Res libraries
   - Reason: library might include 24‑bit/192 kHz FLACs, DSD128/256, and even MQA.
   - Benefit: the Extreme Pro’s A2 app performance class and U3/V30 speed rating means it loads album art, tracks, and waveforms quickly with no lag when scrolling through thousands of high‑res files.
   - Lower‑end cards (A1 or V10) can stutter when browsing large libraries.
- Reliability for portable use
   - It’s shock‑proof, temperature‑proof, waterproof, and X‑ray proof — important if you carry it in your phone everywhere.
   - Frequent hot‑swapping between phone and PC doesn’t cause corruption as easily as with cheaper cards
- Capacity that matches the goal
   - At 512 GB, one can store:
      - ~11,000 FLAC albums at CD quality
      - ~1,700 albums at 24‑bit/192 kHz
      - Hundreds of DSD albums
   - It avoids having to juggle multiple cards or offload albums constantly.

Anyway, the Sony Xperia 1 III officially supports microSDXC cards up to 1 TB, and it works fine with the largest cards on the market (as long as they’re genuine and high‑speed):

| **Model** | **Speed Class** | **Why pick it** |
| --- | --- | --- |
| SanDisk Extreme Pro microSDXC | UHS-I, V30, A2 | Best all-rounder for speed, durability, random read performance (instant music browsing) |
| Lexar Professional 1066x | UHS-I, V30, A2 | Slightly cheaper, still fast and reliable |
| Samsung Pro Plus | UHS-I, V30, A2 | Excellent sustained read/write, great for mixed use (audio + video) |

If one goes straight to 1 TB Extreme Pro, never worries about swapping or deleting albums. A genuine Extreme Pro 1 TB is still expensive, expected €130‑€160 new in 2025. The Samsung Pro Plus (new 2023/2024 model) is generally cheaper than the SanDisk Extreme Pro and still performs extremely well for the use case:

- Speeds: ~160 MB/s read, ~120 MB/s write (real‑world ~140/100 MB/s)
- Video class: V30 (sufficient for 4K/120 fps recording)
- App performance: A2-rated (fast random reads/writes, good for storing app data or UAPP library)
- Durability: Waterproof, temperature proof, X-ray proof
- Warranty: Usually 10 years

It does worth notice that UHS‑II velocity class is not needed; the phone supports UHS‑I, and high‑end UHS‑I cards are already faster than required for audio. However, Sony Xperia 1 III’s microSD slot is UHS‑I only: it physically can’t use the second row of contacts that makes UHS‑II faster. For audio, even a slow card could handle lossless audio; high‑res FLAC/DSD playback needs only a few MB/s. What matters for music is random read speed (so browsing your library is instant) and high-end UHS-I A2 cards like Extreme Pro excel here.

To be precise, for photos and videos, the phone can record 4K 120 fps and RAW stills. A V30‑rated UHS‑I card (like SanDisk Extreme Pro, Samsung Pro Plus, Lexar Professional 1066x) writes ≥30 MB/s sustained, that is, way above what the phone’s camera actually outputs. Even for continuous burst RAW shooting, a top UHS‑I card keeps up fine because the phone has an internal buffer.

![](assets/img-0035.png)

Instead, inside the FiiO Ka17’s box:

- 1× FiiO KA17 DAC/Amp
- 1× Short USB‑C ↔ USB‑C cable (data)
- 1× USB‑A ↔ USB‑C adapter
- 1× Manual / warranty card

The LINDY OTG cable + balanced cable is outside this box, for a total budget of ~€385–€475 (depending on cable choice and sales) up to now. Therefore, the confirmed portable kit can be:

| **Item** | **Model / Specs** | **Why It’s Chosen** | **Notes** |
| --- | --- | --- | --- |
| OTG Y-Cable Splitter | LINDY USB-C OTG Splitter **(USB-C Male → USB-A Female + USB-C Female Power In)** | Correct OTG wiring, stable power injection, works with power bank + Xperia simultaneously | Must plug DAC into USB-A Female and power bank into USB-C Female |
| USB-C Power Bank | Anker PowerCore 10000 PD Redux **(or Anker Nano Power Bank 10K PD)** | Compact, reliable PD power delivery, clean 5 V output for DAC stability | 10,000 mAh is enough for many hours |
| Portable DAC/Amp | FiiO KA17 **(4.4 mm balanced + 3.5 mm SE, Desktop/Turbo modes)** | Safely drives 250–600 Ω headphones, balanced out for max performance | In box: DAC, USB-C ↔ USB-C cable, USB-C ↔ USB-A adapter |
| Balanced Cable | High-quality 4.4 mm TRRRS to Beyer mini-XLR **(e.g., Periapt, Oidio, Hart Audio)** | Ensures channel separation, lower noise, max voltage swing | For DT 770 Pro balanced mod |
| Headphones | Beyerdynamic DT 770 Pro 250 Ω (Closed-back) | Portable-friendly isolation, analytical-leaning neutrality, high resolution | Strong build, great with KA17 balanced out |
| microSD Card | Samsung Pro Plus 1 TB (UHS-I, V30, A2) | Large capacity for lossless/DSD, cheaper than SanDisk Extreme Pro with very similar real-world speed | Waterproof, high endurance |
| Playback App | USB Audio Player PRO (UAPP) | Bypasses Android mixer for bit-perfect playback over USB DAC, supports DSD/MQA, EQ/DSP options | Works perfectly with KA17 |

The total approximate cost is:

- LINDY OTG Splitter DDHIFI-TC28C-PRO: ~€30
- Anker Power Bank 10K PD: ~€30 [https://www.amazon.it/Anker-PowerCore-10-000mAh-tecnologia-dispositivi/dp/B0D4MDHB21](https://www.amazon.it/Anker-PowerCore-10-000mAh-tecnologia-dispositivi/dp/B0D4MDHB21)
- ![](assets/img-0036.png)
- FiiO KA17: ~€149 [https://fiio.eu/product/fiio-ka17-dac-and-headphone-amplifier](https://fiio.eu/product/fiio-ka17-dac-and-headphone-amplifier)
- Balanced Cable (custom quality): ~€40 – €70
   - Aune AR3 4,4 mm → dual 3,5 mm
   - SJYAudio Balanced 4,4 mm → dual 3,5 mm “Horizon Closed Carbon”
   - iFi audio 4,4 mm → 4,4 mm (cavo bilanciato con rame OFHC e matrix argento, shielding minimizzato) [https://ifi-audio.com/products/4-4mm-to-4-4mm-cable?srsltid=AfmBOooZ-7S8DvMW5wnDQOLuKBBW1eF8swiOchMs3ehwceOAXhixCip1](https://ifi-audio.com/products/4-4mm-to-4-4mm-cable?srsltid=AfmBOooZ-7S8DvMW5wnDQOLuKBBW1eF8swiOchMs3ehwceOAXhixCip1)
- Beyerdynamic DT 770 Pro 250 Ω: ~€140 [https://europe.beyerdynamic.com/p/dt-770-pro](https://europe.beyerdynamic.com/p/dt-770-pro) Beyerdynamic - DT 700 Pro X [https://www.amazon.it/Beyerdynamic-700-PRO-Registrazione-monitoraggio/dp/B09G75RWN2?th=1](https://www.amazon.it/Beyerdynamic-700-PRO-Registrazione-monitoraggio/dp/B09G75RWN2?th=1)
   - Beyerdynamic DT 700 Pro X does not come with a dedicated hard case in the box (usually includes a soft pouch). Recommended hard-shell cases compatible with DT 700 Pro X:
      - Geekria Hard Case (Medium Size ~22 x 18 x 6 cm) – best choice: excellent protection, great portability, affordable. [https://shop.geekria.com/products/geekria-ultrashell-headphone-case-for-sennheiser-hd820-hd800-s-beyerdynamic-dt-1990-pro-dt-1770-pro-dt-790-dt-770-and-more-hifi-stereo-over-ear-headphones-large-hard-shell-travel-carrying-bag?variant=31163260600414](https://shop.geekria.com/products/geekria-ultrashell-headphone-case-for-sennheiser-hd820-hd800-s-beyerdynamic-dt-1990-pro-dt-1770-pro-dt-790-dt-770-and-more-hifi-stereo-over-ear-headphones-large-hard-shell-travel-carrying-bag?variant=31163260600414)
      - Beyerdynamic DT Hardcase (specifically designed for Beyerdynamic headphones and offers a sturdy hard case with a fabric coating on the outside and a velour-coated interior. It also includes a small internal pocket for storing accessories. This case is available for purchase from various retailers) [https://www.thomann.it/beyerdynamic_dt_hardcase.htm?glp=1](https://www.thomann.it/beyerdynamic_dt_hardcase.htm?glp=1)
- Samsung Pro Plus 1 TB microSD: ~€130 [https://www.samsung.com/it/memory-storage/memory-card/memory-card-pro-plus-microsd-card-1tb-mb-md1t0sa-eu/](https://www.samsung.com/it/memory-storage/memory-card/memory-card-pro-plus-microsd-card-1tb-mb-md1t0sa-eu/)
- UAPP App: ~€8 (Huawei app gallery in-app purchase)

With a total of **~€475 –  €500** for a complete premium portable, neutral-tuned chain. An Ubuntu Studio 25.04 optimized setup can be added so this exact kit works perfectly when plugged into desktop too, confirming the KA17 investment as both portable + desktop‑ready.

Because of problems with shipping to Italy and availability of cables, the OTG cable became the DDHIFI TC28C Pro, for a more portable setup. 

#### Rational behing the headphone choice

Since KA17 is now fixed in the setup, the main headphone choice comes down to sound signature preference, impedance, and portability realism. The top 3 Picks for Neutral / Analytical Portable Listening are:

| **Headphone** | **Impedance / Sensitivity** | **Price (EUR)** | **Pros** | **Cons** |
| --- | --- | --- | --- | --- |
| Sennheiser HD 660S2 | 300 Ω / 104 dB | ~500 € | True reference midrange, natural timbre, lighter clamp vs HD600 | Open-back → less isolation |
| Beyerdynamic DT 880 600 Ω | 600 Ω / 96 dB | ~250 € | Extreme clarity, analytical, huge soundstage | Needs KA17 power, bright treble |
| Hifiman Sundara | 37 Ω / 94 dB | ~350 € | Planar speed, micro-detail, airy staging | Slightly bulkier, less portable |

Among all the aformentioned choice, we narrowed the field to 3 headphones from the list because the list originally included ultra-demanding planars (e.g. Hifiman HE6s), classic but obscure 600 Ω AKGs, modern flagships, and mid-tier planars. To cut-down a little bit the choice:

- Portable realism: some headphones (HE6s, LCD‑2, Arya) need desktop amps to sound right. Even the KA17, strong as it is for a dongle, can’t make them reach their full performance ceiling without you carrying a shoebox-sized amp.
- Impedance + sensitivity match: we filtered for models the KA17 can actually drive to proper dynamic range.
   - Example: AKG K240 DF 600 Ω are very inefficient: you’d hit max volume before they “wake up”.
   - HE6s are notorious “amp killers”, thus dongles choke.
- Signature match for analytical / neutral: specifically desiring neutral + analytical, not warm/musical makes us eliminate models like the LCD‑2 (warmer, darker tuning).
- Availability & service: if one wants to be able to buy new with warranty, spare pads, and parts some vintage or niche models fail here.
- Value vs. price ceiling: some high-cost models would give you only marginal benefit over the DT 880 / HD 660S2 / Sundara in portable use, yet demand much more power.

So, the three left standing – HD 660S2, DT 880 600 Ω, and Sundara – are the sweet spot between:

- KA17’s driving ability
- Tonal goal (neutral/analytical)
- Portability
- Cost efficiency

Therefore, if one wants maximum portability realism while keeping analytical neutrality HD 660S2 is the best all‑rounder, perfect synergy with KA17’s balanced output, working in quiet indoor environments. If one wants pure analysis & treble precision DT 880 600 Ω is the choice, but this is a “critical listening” tool, not a casual headphone. DT 880 600 Ω cost less yet are still a benchmark. The Beyerdynamic DT 880 (and 990, 770) are what we call “legacy reference headphones”. They’ve been in continuous production for decades with almost no major redesign, so:

- Tooling and R&D costs were paid off decades ago → no need to recoup design investment anymore.
- Large-scale production → economies of scale keep per-unit cost low.
- Beyerdynamic sells into pro-audio (studios, broadcast) → they maintain competitive pricing for bulk buyers.
- No exotic materials like beryllium drivers or carbon-fiber shells → just extremely refined dynamic driver engineering.
- They’re open/semi‑open (DT 880 is semi‑open) so they don’t need heavy structural reinforcement like closed-backs

Despite their price, the 600 Ω DT 880 remain a measurement benchmark for neutrality in treble/mids and technical performance. They’re still used in labs, mastering studios, and audio reviews as a “flat” reference.

If you want maximum isolation with DT 880-level performance, you’d actually have to jump to Beyerdynamic DT 770 Pro 250 Ω (closed-back version of the same family), but it’s slightly less airy and a bit more bass-forward. As a final comparison we can make DT 880 600 Ω vs DT 770 250 Ω directly for your KA17 chain — that would show the trade-off between isolation and openness. Let’s compare Beyerdynamic DT 880 600 Ω vs Beyerdynamic DT 770 Pro 250 Ω specifically for FiiO KA17 portable chain with Sony Xperia 1 III + balanced cable + external power bank. More specifically, the technical compatibility with KA17 says that:

| **Spec** | **DT 880 600 Ω** | **DT 770 250 Ω** | **KA17 Impact** |
| --- | --- | --- | --- |
| Impedance | 600 Ω | 250 Ω | KA17 handles both; 600 Ω needs high gain mode |
| Sensitivity | ~96 dB/mW | ~96 dB/mW | Both moderate — KA17 in Turbo can hit full volume cleanly |
| Balanced Cable | Needs aftermarket (stock is SE) | Needs aftermarket (stock is SE) | Balanced output from KA17 gives +6 dB headroom |
| Power Demand | High voltage, low current | Moderate voltage, higher current | KA17’s 4.4 mm out is ideal |

About the tonal and analytical behavior:

| **Trait** | **DT 880 600 Ω** | **DT 770 250 Ω** |
| --- | --- | --- |
| Bass | Very linear, extends deep but not boosted | Boosted sub-bass and mid-bass — more punch, less “flat” |
| Mids | Very flat, accurate for vocals/instruments | Slightly recessed lower mids (can sound less “natural” for mid-centric music) |
| Treble | Forward upper treble, airy, great for micro-details | Also bright, but smoothed vs 880 — more forgiving |
| Soundstage | Wide, open, airy | Narrower, more “inside your head” but excellent imaging |
| Detail Retrieval | Exceptional, textbook reference | Very good but tuned for monitoring rather than ultra-flat analysis |

But when it comes to isolation, the outdoor viability of DT 770 250 Ω keeps the details intact, whereas the DT 880 600 Ω are poor in this sense. 

| **Model** | **Type** | **Isolation** | **Tonal Target** | **Classic Role** |
| --- | --- | --- | --- | --- |
| DT 880 600 Ω | Semi-open | ❌ No isolation | Neutral-bright | Mixing/mastering reference |
| DT 770 250 Ω | Closed | ✅ Strong isolation | Mildly V-shaped (slight bass lift, slightly recessed mids) | Studio tracking / broadcast monitoring |

The KA17 Balanced Turbo Mode Output supports:

- ~650 mW @ 32 Ω
- ~150 mW @ 300 Ω
- ~80–90 mW @ 600 Ω (but high voltage swing up to ~7–8 Vrms)

Both are within safe driving range. The 600 Ω DT 880 will get loud enough and retain full resolution; DT 770 will have even more headroom. So which one? If the goal is pure neutrality + analytical listening → DT 880 600 Ω:

- Gives textbook reference sound.
- Best in quiet rooms / at home / office.
- Will fully show KA17’s clean treble & channel separation.

If one wants isolation without losing too much resolution → DT 770 Pro 250 Ω. Still resolving, with added bass weight for portable use, maintains detail in noisy environments and are easier to drive than 600 Ω with more headroom left. 

Basically, the point in buying the DT 880 600 Ω instead of the lower‑impedance version (or the DT 770) is basically one thing: getting the flattest, most reference‑grade version of the DT 880, with treble and midrange tuned for maximum accuracy, not consumer warmth. A high‑voltage amp (like KA17 in Turbo) will make it sing without extra warmth or compression. Moreover, the infamous Beyer treble spike is a little better controlled in the 600 Ω than the 250 Ω. Studio engineers love the 600 Ω because it is least “fun” sounding… and that’s exactly the point for mixing/mastering accuracy.

If your goal is reference neutrality while moving around, an open‑back 600 Ω isn’t ideal, not because it won’t work, but because environmental noise will throw away the resolution you paid for. That’s why most audiophiles keep the 600 Ω for home or quiet travel (hotel, office, library), and use a closed‑back for commuting. The DT 880 600 Ω is for when you want maximum neutrality and detail retrieval at home or in quiet environments — and you have the amp to drive it, while the DT 770 250 Ω is for isolation and portable practicality even if you sacrifice a little “truth” in the sound.

Then going for DT 770 250 Ω, is KA17 overkill? No, and that’s the beauty of the KA17. With DT 770 250 Ω the KA17 is still a great match because:

- Turbo mode ensures headroom for dynamics without strain.
- Balanced output still improves channel separation and lowers noise floor.
- You’ll get better bass control and treble precision than with a weaker dongle DAC.

Future‑proofing:

- KA17 can easily handle future upgrades: 600 Ω dynamics, power‑hungry planars like Hifiman Arya, LCD‑2, or even more exotic headphones.
- Also perfect for desktop use if you connect it to a PC or Ubuntu machine.

KA17 is not overkill. It’s more like insurance for whatever headphones you might want later.

But, if you’re already OK with closed‑back for isolation and you have the KA17 (which can drive many planars), then yes — you can absolutely consider a closed‑back planar instead of the DT 770 250 Ω.

| **Feature** | **Dynamic driver (DT 770 250 Ω)** | **Planar-magnetic**<br>**(e.g., closed-back planar)** |
| --- | --- | --- |
| Bass control | Punchy, but can have slight bloom depending on seal | Extremely tight, controlled, and linear |
| Transient speed | Fast for a dynamic | Faster — ultra-quick attack/decay, better for micro-details |
| Imaging & layering | Very good for a closed-back | Often even more precise and stable |
| Tuning | Mild V-shape (boosted bass + treble) | Many are tuned neutral-ish with extended bass |
| Drive requirements | Needs decent voltage | Needs more current — but KA17 Turbo balanced output can handle most portable-friendly planars |
| Comfort | Lighter, less clamp | Planars are usually heavier — comfort varies |
| Isolation | Good | Depends on model, but many are on par with DT 770 |

These are all models the KA17 can drive well for portable use:

- Audeze LCD‑XC (2021): reference‑grade closed planar, very resolving, heavy but luxurious; expensive – is an out of budget choice
- Audeze MM‑100 (semi‑open): more neutral, lighter, but less isolation – still costing ~470€
- Dan Clark Audio Aeon 2 Closed: very portable for a planar, folds up, neutral‑leaning, comfortable – is an out of budget choice

Some still pick DT 770 over planar for portable listening for several reasons. First at all planars are  often heavier, noti deal for long walks. Planars are more delicate than the DT 770 tank‑like build. But what’s more, planars cost 2 – 4× the DT 770.

A portable-friendly closed-back planar with a KA17 would outperform DT 770 250 Ω in resolution and technicality, but for a rugged, affordable, lighter, and still good isolation, the DT 770 remains a strong choice.

Beyerdynamic DT 770 Pro 250 Ω + FiiO KA17 is a rock-solid, *future-proof* choice. Moreover, is a Plug‑and‑play via USB: KA17 is USB Audio Class 2.0 compliant, so no special drivers are needed. The 4.4 mm balanced cable for maximum headroom can be used even on desktop. Ubuntu Studio already ships with ALSA/JACK/PulseAudio/PipeWire tuned for low‑latency audio. On Ubuntu Studio one can also use:

	pw-metadata -n settings 0 clock.rate 96000

to lock your PipeWire sample rate to 96 kHz when listening — keeps things bit‑perfect with many hi‑res sources. Also, using Audacious or Qmmp with ALSA output bypasses resampling. See also Windows / Ubuntu without extra drivers.

However, there is a problem: if one wants to stay in the portable / neutral‑analytical target and keep the KA17 running balanced without doing irreversible mods like rewiring a DT 770 Pro this is not the solution. So to sum the Selection criteria for the alternative are:

- Closed‑back (for outdoor / noisy environment realism)
- Neutral to analytical tuning (no bass‑boost consumer signature)
- High enough resolution to match KA17’s capability
- Detachable cable → easy swap to 4.4 mm balanced
- Drivable from KA17 balanced Turbo without strain
- Build: rugged enough for portable use

Then, the closest match to DT 770 Pro 250 Ω but balanced‑ready is

.

[https://www.reddit.com/r/FiiO/comments/1c62b8p/just_ordered_the_ka17_with_a_balanced_cable_what/](https://www.reddit.com/r/FiiO/comments/1c62b8p/just_ordered_the_ka17_with_a_balanced_cable_what/)

#### The Y-cable DDHIFI TC28C Pro

There is no reliable Italian or European seller currently selling the "LINDY OTG Y-Cable" cable or an equivalent USB-C OTG Y splitter with power pass-through as per the ready-to-purchase diagram. This type of cable is a very niche product, used in professional or laboratory contexts and in Europe and Italy it is not widely distributed by generalist stores or large marketplaces.

If waiting time is not an issue and you simply want to buy a USB-C OTG Y splitter cable with pass-through power, here are some reliable options with shipping in Italy (although they may arrive after a few weeks). Remember that the goal is:

- USB-C → Power Bank female (Power Supply)
- DAC → USB-A female
- USB-C Male → phone

As a concrete alternative, two separate cables could be used:

- A USB-C male → USB-A female OTG cable to connect the DAC.
- A USB-C female → USB-C male cable for power (power bank).

Then you have to physically join the two cables with a passive USB-C splitter which, however, separates the power supply from the data. In practice, you need a USB-C separator power supply (power injector) to work side by side.

[https://www.aliexpress.com/ssr/300000512/BundleDeals2?spm=a2g0o.productlist.main.6.183dB7IOB7IO5o&productIds=1005008321886271:12000044603251195&pha_manifest=ssr&_immersiveMode=true&disableNav=YES&sourceName=SEARCHProduct&utparam-url=scene%3Asearch%7Cquery_from%3A](https://www.aliexpress.com/ssr/300000512/BundleDeals2?spm=a2g0o.productlist.main.6.183dB7IOB7IO5o&productIds=1005008321886271:12000044603251195&pha_manifest=ssr&_immersiveMode=true&disableNav=YES&sourceName=SEARCHProduct&utparam-url=scene%3Asearch%7Cquery_from%3A) 

iFi Audio OTG cable with power injection (OTG con porta power dedicata) 

La scelta migliore per te è il cavo OTG iFi Audio USB‑C o il ddHiFi TC07S, reperibili in Italia ed efficienti per alimentare il DAC esterno senza compromettere host OTG sul tuo Xperia 1 III

oppure

**ddHiFi TC28i Pro** o equivalenti con "power only input" [https://www.amazon.com/Linsoul-DDHIFI-Female-Adapter-Converter/dp/B0B2RWBT9R](https://www.amazon.com/Linsoul-DDHIFI-Female-Adapter-Converter/dp/B0B2RWBT9R) 

	È un OTG Power Adapter USB‑C con 2 porte femmina USB‑C: una per i dati + audio verso il DAC, l’altra per l’alimentazione esterna fino a 5 V / 1 A max, che viene iniettata separatament. Design compatto “a L”, costruzione in metallo, uscite affiancate

**⚠ Alcuni limiti → max 1 A in ingresso**

Se il DAC esterno richiede più di 1 A (es. DAC + amplificatore combinati), l’alimentazione non sarà ottimale → il DAC potrebbe non funzionare a piena potenza.

Se il tuo DAC consuma ≲ 1 A, il TC28i Pro può funzionare senza problemi, mantenendo modalità host OTG e alimentando separatamente il DAC. Il TC28i Pro va bene se il tuo DAC consuma al massimo circa 1 A.

Il DDHIFI TC28i Pro che hai linkato non è adatto se vuoi usare il KA17 in modalità desktop

perché è limitato a circa 1 A max di power injection → rischi che il KA17 resti in modalità standard o si disconnetta sotto carico.

![](assets/img-0037.png)

Per il tuo setup, il **DDHIFI TC28C Pro** [https://www.ddhifi.com/en/product/tc28cpro/](https://www.ddhifi.com/en/product/tc28cpro/), https://www.amazon.com/Linsoul-DDHIFI-Lightweight-Adapter-Converter/dp/B0CCJ6784F , [https://www.linsoul.com/products/ddhifi-tc28c-pro?variant=43947853873369](https://www.linsoul.com/products/ddhifi-tc28c-pro?variant=43947853873369)  è la scelta corretta:

Supporta **fino a 2 A / 10 W** di alimentazione esterna → sufficiente per modalità desktop del KA17.

Cablaggio OTG corretto (dati isolati dall’alimentazione).

Nessun rischio di back-powering verso il telefono.

Più compatto e con meno problemi di ingombro rispetto al TC28i Pro.

Hai individuato **il modello giusto**: il **DDHIFI TC28C Pro** è perfettamente compatibile con il tuo setup (Sony Xperia 1 III + FiiO KA17), e supporta pienamente la modalità desktop del KA17 grazie alla sua iniezione di potenza fino a circa **2 A (10 W)** oltre a un cablaggio dati/potenza ben isolato. Ho trovato il prodotto su rivenditori affidabili accessibili dall’Italia, con spedizione da Europa o Cina ma spesso con opzioni express.

**⚙️ Configurazione finale consigliata:**

**Collega il TC28C Pro alla USB-C del tuo Xperia**.

Inserisci un **alimentatore esterno USB-C** con uscita **5 V / 2 A** (tipo charger o powerbank con porta QC/PD).

Collega il **FiiO KA17** alla porta dati del TC28C Pro.

Le cuffie con uscita bilanciata da 4.4 mm si collegano al KA17.

Così il KA17 entrerà in **modalità desktop**, massimizzando la sua uscita audio senza scaricare la batteria del telefono. quel link Linsoul è perfetto.

**È il modello corretto**: DDHIFI TC28C Pro (versione più recente, compatta, supporta fino a ~2 A di alimentazione esterna).

**Spedizione dall’Europa disponibile**: se scegli “EU warehouse” al checkout, eviti dogana e riduci i tempi (di solito 5-7 giorni lavorativi).

**Prezzo corretto**: 29,99 USD è in linea col listino ufficiale.

**Compatibile con Xperia 1 III + KA17 in modalità desktop**: mantiene OTG attivo e fornisce corrente sufficiente per il DAC alla massima potenza.

Ti servirà solo un **alimentatore USB-C 5 V/2 A stabile** (PD o QC, ma bloccato a 5 V), e sei pronto.

### Final reminders

We know that one must use apps like Use USB Audio Player Pro (UAPP) or HiBy Music if want full bit-perfect playback from Android — especially for DSD or hires FLAC. Moreover:

1. Always connect power to the Y-cable first, then plug into the DAC, then the phone — some DACs initialize poorly otherwise.
1. Some DACs may stop responding if the phone sleeps. Set a wakelock or keep screen on during playback if needed.
1. Most DACs light up when connected correctly (green/blue LED). If you see no light, check OTG or power order.
1. One can use a right-angle USB-C adapter to make this more pocket-friendly.
1. Consider enabling USB tweaks via developer options (disable USB debugging, prefer USB audio, avoid charging interruptions)

Aaaaaaaaa

## The three ways of using FiiO KAx

### With a PC: a desktop headphone amp

With the FiiO KA5, one is not limited to your Sony Xperia 1 III as it works beautifully on Ubuntu Linux and Windows 11 as well. We can run bit‑perfect mode on Ubuntu or Windows with no driver headaches (only ASIO needed on Windows for native DSD). Lossless DSP/EQ for headphone correction can also be applied. 

#### Linux

The core analysis for the FiiO KA5 does not change whether you’re on Ubuntu 24.04 LTS, Xubuntu, or any other modern Linux distro and even less so for something like Anduinos OS., where KA5 behaves exactly as on Ubuntu 24.04 LTS because:

1. It’s built on the same Ubuntu base.
1. It uses the same Linux kernel (5.x/6.x) with USB Audio Class 2.0 support.
1. It inherits the same ALSA/PipeWire audio stack.

The reason is simple: Linux kernel 5.x and later has native USB Audio Class 2.0 support, which is all the KA5 needs to work plug‑and‑play. In practical terms:

   1. Plug‑and‑play recognition — no drivers needed.
   1. Selectable in PipeWire/PulseAudio as an output device.
   1. Bit‑perfect playback possible via:
   1. ALSA direct (e.g., aplay -D hw:...)
   1. PipeWire exclusive mode
   1. Players like DeadBeef, Audacious, Strawberry, or Roon Bridge.
   1. Native DSD playback if you configure DoP in your player.
   1. DSP/EQ available via EasyEffects (system‑wide parametric EQ, crossfeed, convolution).

As an example, the KA5 will behave on Anduinos OS exactly as it does on stock Ubuntu 24.04 – same setup steps, same customization options. The main difference is only in UI and workflow tweaks Anduinos brings to make ex‑Windows users feel at home.

Thus, everything connects simply by a Linnux kernel 5.x+ support and no drivers needed and plugging the balanced 4.4 mm or single-ended 3.5mm to the headphones. What is possible to do in Linux is:

1. Bit‑perfect playback using:
   1. aplay with ALSA in terminal
   1. Audacious or DeadBeef with ALSA output
   1. Qobuz / Tidal via Roon Bridge or Tidal Connect clients for Linux
   1. HQPlayer NAA if you’re into upsampling
1. Native DSD playback via players like Audacious or DeadBeef (select DoP/DSD output)
1. Hi‑res PCM up to 32‑bit / 384 kHz natively
1. Use alsamixer to control the KA5’s hardware volume directly

Ubuntu will often default to PulseAudio and to get true bit‑perfect, one needs to bypass it with ALSA directly.

![](assets/img-0038.png)

As an out-of-the-box behavior, more specifically, Kernel 6.x in 24.04 fully supports UAC2 DACs and KA5 recognized instantly. It appears in pavucontrol (PulseAudio) or pw-top (PipeWire) as a selectable sound device and no special drivers needed.

##### (TBC) Ubuntu Studio 25.04

On Ubuntu Studio 25.04 (or standard Ubuntu), the KA17 is USB Audio Class 2 compliant. This means:

- Plug & play: recognized as external DAC in PulseAudio/PipeWire/JACK.
- No driver install needed.
- The system resampling can be bypassed via
   - pavucontrol (set fixed sample rate)
   - QjackCtl (for low‑latency, direct mode)
   - Audacious / DeadBeef / Strawberry for bit‑perfect local playback.

KA17 can be also forced into Turbo Gain on Linux and Ubuntu’s system mixer can by bypassed for native DSD (DoP) playback.

#### Windows 11

Windows 10 (1803+) and Windows 11 have native USB Audio Class 2.0 drivers. For best quality, one can install FiiO’s ASIO driver, which are needed for native DSD, so that the DAC can appear as a USB DAC in Sound Settings. What is possible to do in Windows is:

1. Bit‑perfect playback via:
   1. Foobar2000 (WASAPI Exclusive or ASIO)
   1. JRiver Media Center (ASIO/WASAPI Exclusive)
   1. Roon (ASIO/WASAPI)
   1. HQPlayer (ASIO)
1. Native DSD up to DSD256 with FiiO’s ASIO driver
1. Hi‑res PCM up to 32‑bit / 384 kHz without resampling
1. Use Tidal / Qobuz / Amazon Music HD desktop apps → enable exclusive mode in their settings for bit‑perfect

If one wants uninterrupted sample rate switching for different tracks, always use WASAPI Exclusive or ASIO otherwise Windows mixer will resample.

### A pure USB DAC

Connect it via USB, switch it to line‑out mode, and feed the signal to an external amplifier. In this setup, the KA5 is only doing the conversion, leaving the actual amplification to your other gear.

### With software EQ or DSP

You can apply equalization, room correction, or other DSP processing in your computer’s audio software before sending the signal to the KA5. That way, the KA5 outputs an already-tuned signal, whether you’re using it to drive headphones directly or feeding an external amp.
