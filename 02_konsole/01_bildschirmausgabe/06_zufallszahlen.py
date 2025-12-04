import random as rd

print("Nun erscheinen 10 Zufallszahlen.")
for _ in range(10):
    zufallszahl = rd.randrange(1, 11)
    print(zufallszahl)
print("Das waren 10 Zufallszahlen.")
