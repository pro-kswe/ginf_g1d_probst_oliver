import random as rd

temperatur_in_celsius = rd.randrange(-20, 40)
print(f"Die Temperatur beträgt {temperatur_in_celsius} Grad Celsius.")

if temperatur_in_celsius < 0:
    print("Es friert.")

if temperatur_in_celsius > 25:
    print("Es ist warm.")
    