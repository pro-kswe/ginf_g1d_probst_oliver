import PIL.Image as img
import random as rd


bild = img.new("RGB", (20, 3))
rot = rd.randrange(0, 256)
gruen = rd.randrange(0, 256)
blau = rd.randrange(0, 256)
farbe = (rot, gruen, blau)

for x in range(0, 20):
    bild.putpixel((x, 0), farbe)

for x in range(0, 20):
    bild.putpixel((x, 1), farbe)

for x in range(0, 20):
    bild.putpixel((x, 2), farbe)

# Alternativ

# for x in range(0, 20):
#    bild.putpixel((x, 0), farbe)
#    bild.putpixel((x, 1), farbe)
#    bild.putpixel((x, 2), farbe)

bild.save("08_gefuelltes_rechteck_ergebnis.png")
