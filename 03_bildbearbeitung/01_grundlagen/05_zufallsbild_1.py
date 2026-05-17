import PIL.Image as img
import random as rd

breite = 100
hoehe = 100
bild = img.new("RGB", (breite, hoehe))

for _ in range(7500):
    r = rd.randrange(0, 256)
    g = rd.randrange(0, 256)
    b = rd.randrange(0, 256)
    x = rd.randrange(0, breite)
    y = rd.randrange(0, hoehe)
    bild.putpixel((x, y), (r, g, b))

bild.save("05_zufallsbild_1_ergebnis.png")
