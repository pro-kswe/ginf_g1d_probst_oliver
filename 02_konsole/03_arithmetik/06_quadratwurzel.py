import math as m
import random as rd

radikanden = [4, 25, 10, 99, 100, 42, 3600, 289, 2, 7]
radikand = rd.choice(radikanden)
x = m.sqrt(radikand)
y = x ** 2
print(f"Radikand: {radikand}")
print(f"Die Quadratwurzel von {radikand} ist {x}.")
print(f"Kontrolle: Das Quadrat von {x} ist {y}.")
