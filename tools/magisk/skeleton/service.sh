#!/system/bin/sh
# service.sh - eseguito in late_start service, a boot avanzato (il sistema e' gia' su).
# Adatto a tweak che richiedono il sistema pronto, es. scrittura di parametri sysfs.
# Esempio (illustrativo, da verificare sul dispositivo):
#   echo 1 > /sys/class/kgsl/kgsl-3d0/force_clk_on
