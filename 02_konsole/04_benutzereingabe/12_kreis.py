import random as rd
import math as m

r = float(input("Wie lautet der Radius?"))
u = 2 * m.pi * r
u_gerundet = round(u, 1)
flaecheninhalt = m.pi * r ** 2
flaecheninhalt_gerundet = round(flaecheninhalt, 1)
print(f"u: {u} und gerundet: {u_gerundet}")
print(f"A: {flaecheninhalt} und gerundet: {flaecheninhalt_gerundet}")
