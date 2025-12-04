import calendar as cal
import random as rd

zufallsjahr = rd.randrange(1900, 2026)
antwort = cal.isleap(zufallsjahr)

print("Zufälliges Jahr:")
print(zufallsjahr)
print("Ist es ein Schaltjahr?")
print(antwort)
