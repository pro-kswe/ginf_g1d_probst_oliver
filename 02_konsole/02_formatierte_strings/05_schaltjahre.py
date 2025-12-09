import random as rd
import calendar as cal

anzahl = rd.randrange(10, 21)
print(f"Es werden {anzahl} zufällige Jahre überprüft.")
for _ in range(anzahl):
    jahr = rd.randrange(1900, 2025)
    antwort = cal.isleap(jahr)
    print(f"Ist {jahr} ein Schaltjahr? {antwort}")
