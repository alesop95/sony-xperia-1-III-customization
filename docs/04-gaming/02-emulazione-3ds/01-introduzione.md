# Introduzione

Emulare il Nintendo 3DS su Android è molto più stabile e soddisfacente rispetto alla Switch, soprattutto con il tuo Xperia 1 III (Snapdragon 888, GPU Adreno 660). Qui entri nel territorio degli emulatori maturi, in particolare Citra, disponibile in diverse versioni ottimizzate per Android.

Sony Xperia 1 III è perfetto per Framerate stabili (anche 60 fps su molti giochi), supporto grafico avanzato (shader, upscaling), buona compatibilità.

## Configurazione ottimizzata per gaming

Con il Sony Xperia 1 III + LineageOS 22.2 (che dà il massimo controllo anche per il gaming) se si vogliono massime prestazioni, miglior qualità video nei giochi, uso efficiente della GPU Adreno 660, e sfruttare le opzioni avanzate per emulatori. Si può quindi settare:

1. Profilo prestazioni massime
   1. Assicurarsi che il profilo energetico sia settato correttamente e se si ha root + LineageOS bisogna andare su Impostazioni > Batteria > Profilo Prestazioni
   1. Selezionare “Prestazioni”
- Se ci si vuole spingere ancora oltre:
   1. Kernel Manager (se si usa Kernel personalizzato)
      1. Con app come SmartPack Kernel Manager o HKTweaks (per dispositivi Snapdragon) ci sono delle impostazioni consigliate:
         1. Governor CPU: performance
         1. Scheduler I/O: cfq o noop
         1. Boost touch: ON
         1. Thermal throttling: limitato o disattivato (con cautela)

In generale, throttling termico è il tuo peggior nemico durante l’emulazione ed è consigliato usare una ventola esterna tipo Black Shark/Fan Cooler e non giocare mentre si carica il telefono per non surriscaldare e infine evitare cover spesse. 

1. Entrare su Impostazioni > Sistema > Opzioni Sviluppatore dopo aver attivato le opzioni di sviluppatore in Android (attivato dopo aver toccato 7 volte su “Build Number”). Impostare:
   1. Forza MSAA 4x: ✅ (aumenta qualità grafica nei giochi OpenGL, utile per emulatori)
   1. Disattiva overlay HW: ✅ (spinge tutto sulla GPU)
   1. Limite processi in background: 2 (opzionale)
   1. Scala animazione finestra/transizione/durata: 0.5x o off (più reattivo)
   1. GPU Profiler: ❌ (solo per debugging)
1. Se uno ha il root attivo con Magisk ci si può spingere oltre:
   1. Thermal Manager Mod o Thermal Daemon Disabler (evita il throttling termico troppo aggressivo)
      1. Se la temperatura non viene limitata dopo i 38-42°, in quel caso si può valutare il modulo Thermal Mod
   1. Adreno GPU Driver Mod (Driver custom (Es. Mesa o V@ V615/V660) con performance migliorate per emulazione)
   1. LKT, NFSInjector (moduli che ottimizzano I/O e kernel tuning per giochi)
   1. GPU Turbo Boost (in alcuni casi migliora performance con emulatori Vulkan)
1. Impostazioni Display e Touch
   1. Impostare lo schermo a 120Hz (se disponibile su Lineage) – Impostazioni > Display > Frequenza di aggiornamento
   1. Disattivare Adaptive Brightness per evitare oscillazioni
   1. Attivare la modalità a schermo intero per i giochi
1. Impostazioni emulatore (es. Citra MMJ o Strato)
   1. Per Citra MMJ:
      1. CPU JIT: ON
      1. Accurate GPU Emulation: OFF
      1. Resolution scale: 2x o 3x (3x raccomandato, 4x solo se il gioco è leggero)
      1. Enable Shader JIT: ON
      1. Linear Filtering: ON
      1. Audio Stretching: OFF (più reattivo)
      1. Hardware Shader: ON
   1. Per Strato (emulatore Switch)
      1. Accurate GPU: OFF
      1. Resolution Scale: Auto o 1x (Switch è pesante, evita oltre 1x)
      1. Shader Caching: ON
      1. Fastmem: ON
      1. Multicore Scheduling: ON
1. App aggiuntive utili
   1. Game Booster (magari via Magisk o modulo LineageOS)
   1. Gsam Battery Monitor per monitorare il throttling
   1. Activity Launcher per accedere a opzioni nascoste

L’emulatore migliore può essere una versione modificata di Citra, ottimizzata per prestazioni elevate su Android. Superiore alla versione ufficiale su molti dispositivi:

1. ✔️ Altissima compatibilità
1. ✔️ Interfaccia pulita, tantissime opzioni
1. ✔️ Salvataggi automatici, upscaling 2x/3x
1. ✔️ Supporta shader, layout schermo doppio/piccolo
1. ❌ Sviluppo discontinuo, ma stabile

Si può scaricare da APKPure cercandola con il suo nome ed essendo basato su codice open‑source, è sicuro e “virus‑free” secondo la verifica di APKPure.

L’APK è legittimo e non contiene malware, ma **non include giochi**. Devi usare ROM solo se possiedi una copia fisica del gioco 3DS – scaricare ROM pirata è illegale in Italia. L’emulatore è legale (GPL), mentre le ROM illegali no.

Presenta opzioni di base gratuite, più upgrade in-app (temi, filtri texture) [https://citra-emulator.com/download/android](https://citra-emulator.com/download/android). Compatibile con controller esterni. La versione moddata supporta controller Bluetooth, high‑end device, e il tuo setup Android 15 lo gestirà agevolmente.

Se vuoi qualcosa di più “ufficiale” e con aggiornamenti più recenti, puoi prendere la versione **Citra Emulator 518f723 (59,6 MB)**, rilasciata il **16 agosto 2024** [APKPure.net+3APKPure.com+3APKPure.com+3](https://apkpure.com/citra-emulator/org.citra.citra_emu/download?utm_source=chatgpt.com). Compatibile con Android 9+, architecture arm64-v8a/x86_64. Tuttavia, Citra ufficiale 518f723 (da APKPure) – Più stabile, meno flessibile:

1. ✅ Upscaling (fino a 4x-5x, dipende da gioco e device)
1. ✅ Filtro antialiasing, scaling, audio fix
1. 🚫 No supporto nativo a texture pack custom
1. 🚫 Shader personalizzati non supportati pienamente
1. 🚫 No cheat codes (se non tramite editing manuale dei salvataggi o fork esterni)
1. ⚠️ Nessun menu per modding avanzato
1. ✔️ Stabile e regolarmente aggiornato, compatibile con Android 9–15

Mentre invece Citra MMJ (moddata):

1. ✔️ Texture packs (HD & custom) ✅
1. ✔️ Shader personalizzati ✅
1. ✔️ Cheat codes ✅ (supporta file .txt o da UI)
1. ✔️ Upscaling avanzato fino a 10x ✅
1. ✔️ Config per ogni gioco ✅
1. ✔️ Interfaccia avanzata (temi, filtri, animazioni, salvataggi personalizzati) ✅
1. ❗ Non aggiornata ufficialmente → sviluppo community
1. ⚠️ Alcune build sono più "grezze", ma ideali per chi smanetta

Usando LineageOS 22.2 con libertà piena di modding, Citra MMJ è la scelta migliore per giochi in alta definizione, mod texture o shader custom, cheat code e profili per gioco. Si può avere tutto il controllo completo e l’hardware del Sony Xperia 1 III (Snapdragon 888, 12GB RAM) può reggere tutto.

### Precisazioni

SENZA ROOT/MAGISK: hai già ottime prestazioni e puoi usare il 90% delle impostazioni. Tutto ciò che è nei menu di Android si può fare SENZA root/Magisk ovvero:

1. Profilo prestazioni (se disponibile in LineageOS)
1. Opzioni sviluppatore
1. Impostazioni grafiche in emulatori
1. Modifiche a layout e texture
1. Risoluzione del display, animazioni, ecc

Quindi puoi già ottenere buone prestazioni senza root. Mentre invece ci sono delle cose che si possono fare SOLO SE si ha root + Magisk:

| **Funzione** | **Richiede Root?** | **Note** |
| --- | --- | --- |
| Disattivare throttling termico di sistema | ✅ Sì | Moduli Magisk: Thermal Daemon Disabler o Thermal Manager |
| Installare driver GPU custom (es. Adreno V615) | ✅ Sì | Via Magisk, cambia il comportamento della GPU |
| Tweak kernel avanzati | ✅ Sì | Richiede accesso a sysfs o configurazioni avanzate |
| Moduli tipo LKT / NFSInjector | ✅ Sì | Ottimizzano I/O, CPU, RAM |
| GPU Turbo Boost | ✅ Sì | Spinge le prestazioni grafiche su emulatori |

CON ROOT/MAGISK: ottieni massimo controllo e puoi eliminare throttling, caricare driver GPU ottimizzati, e migliorare fps nei giochi pesanti/emulazione. Senza Magisk/root non puoi cambiare termici, governor CPU o caricare driver GPU custom.

In tutto questo il kernel è il "motore" del sistema operativo Android e decide come la CPU, la GPU, la RAM, la batteria e l’I/O lavorano. Ogni dispositivo ha un kernel, ma i kernel stock sono molto conservativi (per sicurezza, batteria, calore). Un kernel personalizzato (custom kernel) in questo contesto è una versione modificata del kernel originale, con funzionalità extra per gaming, tweak, undervolt, governor personalizzati, ecc. Per usare un kernel personalizzato è necesario avere:

1. Root
1. Magisk
1. Hai installato un kernel modificato (es: Kirisakura, StormBreaker, NoGravity, ecc.) compatibile con Xperia 1 III

Si usa in questo senso un Kernel Manager, ovvero un’app per controllare e configurare le opzioni del kernel (ad esempio SmartPack Kernel Manager, HKTweaks, EX Kernel Manager) e questo permette di:

1. Cambiare governor CPU (es. performance, schedutil)
1. Schedulatore I/O
1. Attivare Boost Touch
1. Limitare o disattivare throttling termico (con cautela)

Queste app richiedono ROOT perché accedono a cartelle di sistema protette (es. /sys/, /proc/). 

Quindi in sintesi:

| **Azione** | **Serve ROOT/Magisk?** | **Descrizione** |
| --- | --- | --- |
| Impostare profilo prestazioni | ❌ No (se supportato da LineageOS) | Attivabile da menu batteria |
| Opzioni sviluppatore Android | ❌ No | Tutti possono usarle |
| Ottimizzazioni Citra (JIT, Shader, Upscaling) | ❌ No | Fattibili via app |
| Texture Pack e Cheat | ❌ No | File system accessibile |
| Disattivare throttling termico | ✅ Sì | Solo con Magisk o kernel mod |
| Caricare driver GPU custom (Adreno) | ✅ Sì | Solo con Magisk |
| Tweak CPU/GPU governor/scheduler | ✅ Sì | Solo via app root tipo HKTweaks |

Per fare “qualcosa in più” quindi serve avere Magisk installato, un kernel custom compatibile con Xperia 1 III, installare app tipo HKTweaks o SmartPack Kernel Manager e modificare i parametri del kernel (CPU, I/O, termici).
