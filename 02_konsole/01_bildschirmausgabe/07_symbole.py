import random as rd

print("Variante A")
symbole = ["****", "$$$$", "€€€€"]
symbol = rd.choice(symbole)
for _ in range(4):
    print(symbol)

print("Variante B")
symbole = ["*", "$", "€"]
symbol = rd.choice(symbole)
for _ in range(4):
    print(4 * symbol)
