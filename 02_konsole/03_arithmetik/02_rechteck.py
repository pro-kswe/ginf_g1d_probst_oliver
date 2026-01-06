import random as rd

a = rd.randrange(100, 1001)
b = rd.randrange(100, 1001)
u = 2 * (a + b)
flaecheninhalt = a * b
print("Berechnungen am Rechteck")
print("Seitenlängen:")
print(f"a: {a}")
print(f"b: {b}")
print(f"Umfang: {u}")
print(f"Flächeninhalt: {flaecheninhalt}")
