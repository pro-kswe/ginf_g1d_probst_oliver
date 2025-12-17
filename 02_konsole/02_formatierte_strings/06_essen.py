import random as rd

speisen = ["Pommes", "Linsen-Dal", "Spaghetti"]
speise = rd.choice(speisen)
wochentage = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag"]
wochentag = rd.choice(wochentage)
anzahl = rd.randrange(1, 7)
print(f"Am {wochentag} gibt es {speise} in der Mensa.")
print("Wie finden wir das?")
for _ in range(anzahl):
    print("Juhu")
