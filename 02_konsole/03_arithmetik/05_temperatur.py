import random as rd

temperaturen_in_celsius = [42.5, -2, 31.5, 10, 21.2]
temperatur_in_celsius = rd.choice(temperaturen_in_celsius)
print("Temperaturumrechnung")
print(f"Temperatur in Celsius: {temperatur_in_celsius}")
temperatur_in_fahrenheit = (temperatur_in_celsius * (9 / 5)) + 32
print(f"Temperatur in Fahrenheit: {temperatur_in_fahrenheit}")
