import random as rd

# Eckige Klammern ergeben eine Liste.
# Die folgende Liste speichert vier Strings.
speisen = ["Pommes", "Linsen-Dal", "Spaghetti", "Coq au Vin"]
speise = rd.choice(speisen)
# Noch eine Liste. Die Liste speichert sieben Strings.
wochentage = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
wochentag = rd.choice(wochentage)
print(f"Am {wochentag} gibt es {speise} in der Mensa.")
print("Wie finden wir das?")
zahlen = [5, 42, 16, 8, 99]
anzahl = rd.choice(zahlen)
for _ in range(anzahl):
    print("Juhu")
