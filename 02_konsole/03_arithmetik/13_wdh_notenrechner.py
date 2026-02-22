import random as rd

erreichte_punktzahl = rd.randrange(0, 61)
maximale_punktzahl = rd.randrange(50, 101)
note = (erreichte_punktzahl * 5 / maximale_punktzahl) + 1
print(f"Erreichte Punktzahl: {erreichte_punktzahl}")
print(f"Maximale Punktzahl: {maximale_punktzahl}")
print(f"Note: {note}")
