import random as rd
import math as m

radien = [10, 15, 20, 25, 30, 35, 40, 45, 50]
r = rd.choice(radien)
u = 2 * m.pi * r
u_gerundet = round(u, 1)
flaecheninhalt = m.pi * r ** 2
flaecheninhalt_gerundet = round(flaecheninhalt, 1)
print("Kreisberechnungen")
print(f"r: {r}")
print(f"u: {u} und gerundet: {u_gerundet}")
print(f"A: {flaecheninhalt} und gerundet: {flaecheninhalt_gerundet}")
