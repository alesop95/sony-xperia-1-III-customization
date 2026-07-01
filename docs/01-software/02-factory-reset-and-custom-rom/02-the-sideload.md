# The sideload

## Necessità della custom recovery per i mojor Adnroid version Upgrade

[25/07/2025 17:41] Simon Tran: I installed the Lineage OS custom recovery [25/07/2025 17:41] Simon Tran: You may need this custom recovery for major Android version Upgrade [25/07/2025 17:42] Simon Tran: Minor upgrade can be done with the updater App [25/07/2025 17:42] Simon Tran: But you need to manually sideload the major versions.

## Re-installare il Google Play store

Nel caso il Google Play Store non sia più presente a seguito di un reset o di un'installazione pulita di LineageOS, è possibile sideloadare le GApps direttamente dalla recovery. Il pacchetto suggerito è MindTheGapps, compatibile con LineageOS: [https://mindthegapps.com](https://mindthegapps.com).

La procedura prevede:

Riavvio in recovery

Attivazione della modalità **ADB sideload**

Esecuzione del comando da PC:

adb sideload nomefile.zip

Questa modalità consente il trasferimento diretto di file .zip nel sistema. Tuttavia prevede l’utilizzo di ADB e fastboot.
