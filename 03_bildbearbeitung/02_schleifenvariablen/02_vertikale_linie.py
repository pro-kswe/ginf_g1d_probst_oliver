import random as rd
import PIL.Image as img

bild = img.new("RGB", (5, 10))
r = rd.randrange(0, 256)
g = rd.randrange(0, 256)
b = rd.randrange(0, 256)

for y in range(0, 10):
    bild.putpixel((2, y), (r, g, b))
bild.save("02_vertikale_linie_ergebnis.png") 
