# Übung 6, Streifen
import random as rd
import PIL.Image as img

bild = img.new("RGB", (20, 3))

for x in range(0, 20):
    r = rd.randrange(0, 256)
    g = rd.randrange(0, 256)
    b = rd.randrange(0, 256)
    bild.putpixel((x, 0), (r, g, b))
    bild.putpixel((x, 1), (r, g, b))
    bild.putpixel((x, 2), (r, g, b))

bild.save("06_streifen_ergebnis.png") 
