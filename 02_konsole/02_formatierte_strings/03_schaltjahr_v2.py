import calendar as cal
import random as rd

jahr = rd.randrange(1900, 2026)
antwort = cal.isleap(jahr)
print(f"Es ist das Jahr {jahr}. Ist es ein Schaltjahr? {antwort}")
