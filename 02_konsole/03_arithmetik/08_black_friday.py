import random as rd

print("Black Friday Aktion")
preis = rd.randrange(100, 1000)
rabatt_in_prozent = rd.randrange(1, 101)
print(f"Preis: CHF {preis}")
rabatt_in_chf = (rabatt_in_prozent / 100) * preis
neuer_preis = preis - rabatt_in_chf
print(f"{rabatt_in_prozent} % von CHF {preis} sind CHF {rabatt_in_chf}.")
print(f"Neuer Preis: CHF {neuer_preis}")
print("Was für ein Schnäppchen!")
