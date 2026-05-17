import random as rd
import PIL.Image as img

bild = img.new("RGB", (10, 20))

r = rd.randrange(0, 256)
g = rd.randrange(0, 256)
b = rd.randrange(0, 256)

x_koordinate = rd.randrange(0, 10)
for y in range(0, 20):
    bild.putpixel((x_koordinate, y), (r, g, b))

y_koordinate = rd.randrange(0, 20)
for x in range(0, 10):
    bild.putpixel((x, y_koordinate), (r, g, b))

bild.save("05_zufaelliges_kreuz_ergebnis.png") 
