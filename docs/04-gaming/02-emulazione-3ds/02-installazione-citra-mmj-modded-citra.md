# Installazione Citra MMJ (Modded Citra)

## Come installare e giocare

I passaggi sono I seguenti:

   1. Scarica e installa Citra MMJ dal file .apk (puoi usare APKPure, F-Droid, GitHub). Puoi scaricare Citra MMJ (fork modificato del famoso emulatore Citra) direttamente da APKPure, dove è disponibile l’APK più recente:
      - Versione:  99a89d290
      - Data: 20 giugno 2024
      - Dimensione: circa 15 MB
      - Requisiti: Android 7.0+ (architettura arm64-v8a
   1. Aggiungere I giochi:
      - I file devono essere in .3DS o .CIA
      - Puoi trasferirli su una cartella tipo:
- /storage/emulated/0/Citra/games/
- Creabile autonomamente.
   1. Configurare BIOS e file di sistema (facoltativo). Citra non richiede BIOS, ma alcuni giochi ne beneficiano. Si può allora importare:
      - nand
      - sysdata
      - cartelle SD emulata (dalla tua 3DS modificata)
   1. Impostazioni consigliate per l’Xperia 1 III
      - CPU JIT: attiva
      - GPU accurata: disattiva
      - Upscaling: 2x o 3x
      - Shader: scegli "Linear" per stabilità
      - Frame skipping: 0 o 1 se hai cali di framerate
      - Audio: attiva HLE (più veloce)

## Miglioramenti

Ti spiego tutto con semplicità e un po’ di contesto in stile "glossario pratico per emulazione", così capisci meglio cosa significano upscaling, shader, trucchi, plugin e texture pack, e come possono migliorare la tua esperienza su Citra (o in generale con gli emulatori).

### Texture pack

Le texture pack sono dei pacchetti di immagini ad alta risoluzione che **sostituiscono le texture originali** di un gioco. Le texture sono le "pelli" che ricoprono i modelli 3D (es. il viso di Mario, i muri, l’erba). Perché usarli?

1. I giochi 3DS sono nati per uno schermo piccolo e bassa risoluzione.
1. Su uno smartphone FHD+ come il tuo, i giochi possono sembrare pixellosi o sfocati.
1. Un texture pack HD migliora enormemente la grafica senza modificare il gameplay.

Per installarli si può scaricare un pacchetto (di solito formato .zip o cartelle .png) e metterlo.

Dove scaricare:

1. https://community.citra-emu.org
1. https://r-roms.github.io → segui i link verso texture/mod

### Upscaling

Fare upscaling significa aumentare la risoluzione di rendering del gioco. I giochi 3DS giravano a 240p. Sul tuo schermo da 4K sembrano sgranati. Con l’upscaling li puoi rendere molto più nitidi, simili a giochi per console più moderne. Esempio di impostazioni:

1. 1x (originale)
1. 2x (480p)
1. 3x (720p)
1. 4x (1080p)
1. … fino a 6x (dipende dal dispositivo)

Più si usa l’upscaling, **più carico sulla GPU** (il tuo Xperia regge fino a 3x o 4x in molti casi).

### Shader

Gli **shader** sono filtri grafici che modificano **come viene visualizzato un gioco**. Sono come occhiali per il rendering: cambiano luce, colore, ombre, bordi ecc. Esempi di shader comuni sono:

1. Linear: semplice, veloce, liscio
1. Bilinear: ammorbidisce i bordi
1. CRT: simula uno schermo a tubo catodico
1. Scanlines: aggiunge linee orizzontali per effetto retrò

Si possono usare per migliorare la grafica o darle un tocco artistico o per eliminare seghettature / artefatti visive. Alcuni shader pesano sulla GPU, ma l’Xperia regge bene i più leggeri.

### Mod

Su Android, però, i plugin veri e propri sono rari, mentre le mod dei giochi (patch) sono molto comuni. Esempio di mod:

1. Una patch per Pokémon che rimuove i lag nelle battaglie
1. Una traduzione in italiano di un gioco uscito solo in giapponese

1. [https://gbatemp.net](https://gbatemp.net)
1. [https://romhacking.net](https://romhacking.net)

### Cheat codes

Fare upscaling significa

1. https://www.speedfly.cn
1. https://gamehacking.org

Puoi trovare cheat su siti come:

 [https://www.speedfly.cn/category/cheat/](https://www.speedfly.cn/category/cheat/)

 Reddit o Discord dedicati a Citra

## Pacchetto completo

Un pacchetto completo di ottimizzazione per Citra MMJ sul tuo Sony Xperia 1 III con LineageOS 22.2, per spremere tutto il possibile dall’emulazione 3DS con l’obiettivo di:

1. Prestazioni al massimo (FPS stabili, input veloce)
1. Grafica pulita e nitida (upscaling + shader)
1. Nessun throttling o lag da riscaldamento
1. Supporto a trucchi, texture pack HD e mod

Innanzitutto si può creare un file config.ini in Windows 11:

**[Layout]**
SecondScreenLayout=0
SwapScreens=false

**[Renderer]**
UseHwRenderer=true
UseShaderJit=true
ResolutionFactor=3
LinearFiltering=true
AccurateMultiplication=false
EnableHardwareShader=true
ShaderDiskCache=true

**[Audio]**
EnableAudioStretching=false

**[System]**
RegionValue=-1
EnableCpuJit=true

Da mettere dentro /Android/data/org.citra.citra_mmj/files/citra-emu/config/.

anzichè avere

/Android/data/org.citra.citra_mmj/files/citra-emu/config/

ho:

/Android/data/org.citra.emu/files/ che è vuota mentre nella root folder del telefono prima di /Android ho /citra-emu/config/ va bene lo stesso?  Sì, è corretto e va benissimo.

Quello che sta succedendo è: Alcune versioni di **Citra MMJ recenti (come la tua del 20 giugno 2024)** usano una directory **personalizzata** nella **root del dispositivo**, non in Android/data/ (per via delle restrizioni di accesso su Android 11+). Quindi, la tua struttura:

/citra-emu/config/

/citra-emu/shaders/

/citra-emu/load/textures/

/citra-emu/cheats/

/citra-emu/nand/

/citra-emu/sdmc/

 **perfettamente corretta** . **Conclusione:** Usa /citra-emu/ nella root interna del dispositivo.
Non usare la Android/data/... (è limitata, e in alcune build viene ignorata da MMJ). Quindi i file di configurazione vanno in:

/citra-emu/config/

Si può poi per lo shader e l’upscaling:

1. Attiva Linear Filtering per smussare i bordi senza perdere dettaglio
1. ResolutionFactor=3 (→ 720p rescaling circa), adatto per il tuo display
1. Disattiva opzioni “Accurate GPU emulation” per meno carico sulla GPU

Se si vuole  1080p → ResolutionFactor=4, ma solo su giochi leggeri.

Per le texture pack si possono scaricare texture pack come quelle per Pokèmon X/Y HD (pack) e con formato cartelle .png metterle in:

	/citra-emu/load/textures/<ID_GIOCO>/

L’ID_GIOCO può essere Trovato avviando il gioco e poi andando su Settings > System in Citra e questo ID compare nel titolo della finestra o nel log.

Dopo le considerazioni precedenti sul percorso file. Poi bisogna attivare “Curstom Textures in Citra MMJ”. Per fare questo nell’interfaccia di Citra MMJ, per attivare il caricamento delle texture custom:

1. Apri Citra MMJ
1. Tocca l’icona menu hamburger  in alto a sinistra
1. Vai su Settings / Impostazioni
1. Vai su Graphics > Advanced
1. Attiva l’opzione “Use Custom Textures”
1. Attiva anche (opzionali ma utili):
   1.  Texture Filter: Linear
   1.  Enable Hardware Shader
   1.  Shader JIT

I trucchi sono semplice file .txt da caricare.

Per le Mod consigliate:

1. 60 FPS patches (alcuni giochi supportati, tipo Zelda, Fire Emblem)
1. Traduzioni fan-made
1. QoL patch (fix menu lag, skip intro ecc.)

 Metti le patch .ips o .xdelta in:

/Android/data/org.citra.citra_mmj/files/citra-emu/patches/

**MODULI MAGISK per POTENZIARE CITRA**

 Scaricabili (posso linkarteli direttamente se vuoi):

| **Modulo Magisk** | **Funzione** |
| --- | --- |
| Adreno Boost | Driver ottimizzati per emulatori |
| Thermal Daemon Off | Disattiva throttling termico aggressivo |
| LKT o NFSInjector | Ottimizzazione I/O e CPU schedulers |
| GPU Turbo Boost | Spinta extra su GPU Adreno |

Posso prepararti un **ZIP unico con i 4 moduli compatibili** e istruzioni per Magisk.

**Gamepad consigliato**

8BitDo Pro 2

PS4/PS5 controller (via Bluetooth)

Gamesir X2 (con supporto per Citra touch mapping)
