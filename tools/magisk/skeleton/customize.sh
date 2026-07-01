#!/system/bin/sh
# customize.sh - eseguito da Magisk durante l'installazione del modulo.
# Usare per impostare permessi, copiare file condizionatamente, o stampare messaggi all'utente.
# Lasciare vuoto se non serve. Esempi:
#   ui_print "Installazione modulo Xperia 1 III"
#   set_perm_recursive $MODPATH/system/bin 0 0 0755 0755
