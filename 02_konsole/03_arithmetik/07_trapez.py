import random as rd

a = rd.randrange(50, 501)
c = 2 * a
h = rd.randrange(100, 251)
flaecheninhalt = ((a + c) * h) / 2
print("Berechnungen am Trapez")
print(f"Seitenlängen: a: {a} und c: {c}")
print(f"Höhe: {h}")
print(f"A: {flaecheninhalt}")
