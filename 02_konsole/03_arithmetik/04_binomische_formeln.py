import random as rd

a = rd.randrange(1, 101)
b = rd.randrange(1, 101)
binom_1 = a + b
binom_2 = a - b
ergebnis_1 = binom_1 * binom_1
ergebnis_2 = binom_2 ** 2
ergebnis_3 = binom_1 * binom_2
print(f"1. Binomische Formel: ({a} + {b})({a} + {b}) = {ergebnis_1}")
print(f"2. Binomische Formel: ({a} - {b})({a} - {b}) = {ergebnis_2}")
print(f"3. Binomische Formel: ({a} + {b})({a} - {b}) = {ergebnis_3}")
