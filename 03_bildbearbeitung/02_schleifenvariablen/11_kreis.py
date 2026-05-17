import PIL.Image as img
import random as rd
import math as mt


bild = img.new("RGB", (1000, 1000))

for x in range(0, 20000):
    winkel = x * 0.05
    radius = x * 0.02
    x = int(500 + radius * mt.cos(winkel))
    y = int(500 + radius * mt.sin(winkel))
    
    r = rd.randrange(0, 256)
    g = rd.randrange(0, 256)
    b = rd.randrange(0, 256)
    bild.putpixel((x, y), (r, g, b))

bild.save("11_kreis_ergebnis.png")
