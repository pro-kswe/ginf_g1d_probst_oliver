import random as rd
import calendar as cal

jahr = int(input("Bitte eine Jahreszahl eingeben:"))
antwort = cal.isleap(jahr)
print(f"Es ist das Jahr {jahr}. Ist es ein Schaltjahr? {antwort}")
