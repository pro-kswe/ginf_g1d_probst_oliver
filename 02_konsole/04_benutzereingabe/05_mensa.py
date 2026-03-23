import random as rd

wochentag = input("Bitte Wochentag eingeben:")
menu = input("Bitte Menü eingeben:")
namen = ["Alice", "Bob", "Carol", "Eve"]
name = rd.choice(namen)
wertungen = ["gut", "schlecht", "so naja"]
wertung = rd.choice(wertungen)
print(f"Am {wochentag} gibt es {menu} in der Mensa.")
print(f"{name} findet das {wertung}.")
