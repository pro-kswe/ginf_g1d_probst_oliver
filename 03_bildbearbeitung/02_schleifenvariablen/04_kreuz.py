import random as rd
import PIL.Image as img

bild = img.new("RGB", (10, 20))

r = rd.randrange(0, 256)
g = rd.randrange(0, 256)
b = rd.randrange(0, 256)

for y in range(0, 20):
    bild.putpixel((2, y), (r, g, b))

for x in range(0, 10):
    bild.putpixel((x, 1), (r, g, b))

bild.save("04_kreuz_ergebnis.png") 
