import random as rd
import PIL.Image as img

bild = img.new("RGB", (10, 5))
r = rd.randrange(0, 256)
g = rd.randrange(0, 256)
b = rd.randrange(0, 256)

for x in range(0, 10):
    bild.putpixel((x, 2), (r, g, b))
bild.save("03_horizontale_linie_ergebnis.png") 
