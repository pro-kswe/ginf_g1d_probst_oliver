import random as rd

kontostand = rd.randrange(100, 1001)
zinssaetze = [0.01, 0.025, 0.03, 0.035, 0.04, 0.05]
zinssatz = rd.choice(zinssaetze)
zinsatz_in_prozent = zinssatz * 100
zinsen = kontostand * zinssatz
neuer_kontostand = kontostand + zinsen
print("Jahresende - Kontoauszug")
print(f"Kontostand: CHF {kontostand}")
print(f"Zinssatz: {zinsatz_in_prozent} %")
print(f"Zinsen: CHF {zinsen}")
print(f"Neuer Kontostand: CHF {neuer_kontostand}")
print("Dank für Ihr Vertrauen in die Random-Bank")
