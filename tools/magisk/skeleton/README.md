# Scheletro di modulo Magisk

Template minimo e generico per costruire o adattare un modulo Magisk nel contesto del progetto
(per esempio i moduli prestazionali citati nel runbook gaming, o un modulo che applichi tweak di
sistema dopo il root). Non e' un modulo pronto: e' la struttura di partenza, da personalizzare.

## Struttura

```
skeleton/
  module.prop        metadati del modulo (id, name, version, author, description)
  customize.sh       script eseguito all'installazione del modulo (opzionale)
  service.sh         eseguito in late_start service, a boot avanzato (opzionale)
  post-fs-data.sh    eseguito presto a boot, prima dell'avvio del sistema (opzionale)
  system/            overlay: i file qui dentro si sovrappongono a /system con lo stesso percorso
```

Il campo `id` in `module.prop` deve essere univoco e senza spazi, perche' diventa il nome della
cartella del modulo sul dispositivo. Vanno aggiornati anche `name`, `version`, `versionCode` e
`description` prima di distribuirlo.

## Come si impacchetta e si installa

Si comprime il contenuto della cartella (non la cartella stessa) in un file `.zip`, con
`module.prop` alla radice dell'archivio. Lo zip si flasha dall'app Magisk, voce Moduli, Installa da
storage, oppure da recovery. Dopo l'installazione si riavvia.

```powershell
# esempio di packaging dello scheletro in uno zip flashabile
Compress-Archive -Path tools/magisk/skeleton/* -DestinationPath modulo-magisk.zip
```

## Avvertenza

Un modulo Magisk modifica il comportamento del sistema a basso livello e puo' impedire l'avvio se
errato. Va sempre tenuto il backup Nandroid (runbook software, fase 7) e va testato un modulo per
volta. I moduli prestazionali che disattivano il throttling termico aumentano calore e consumo.
