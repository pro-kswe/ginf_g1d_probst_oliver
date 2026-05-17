import PIL.Image as img
import random as rd

breite = 50
hoehe = 50
bild = img.new("RGB", (breite, hoehe))

r = rd.randrange(0, 256)
g = rd.randrange(0, 256)
b = rd.randrange(0, 256)

for _ in range(26000):
    x = rd.randrange(0, breite)
    y = rd.randrange(0, hoehe)
    bild.putpixel((x, y), (r, g, b))

bild.save("06_zufallsbild_2_ergebnis.png")
