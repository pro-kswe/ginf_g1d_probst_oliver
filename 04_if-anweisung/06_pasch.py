import random as rd

augenzahl_1 = rd.randrange(1, 7)
augenzahl_2 = rd.randrange(1, 7)
print(f"Die Würfel zeigen {augenzahl_1} und {augenzahl_2}.")
if augenzahl_1 == augenzahl_2:
    print("Das ist ein Pasch! Juhu!")
