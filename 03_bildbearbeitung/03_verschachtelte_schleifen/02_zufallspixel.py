import PIL.Image as img
import random as rd

bild = img.new("RGB", (600, 400))

for x in range(0, bild.width):
    for y in range(0, bild.height):
        r = rd.randrange(0, 256)
        g = rd.randrange(0, 256)
        b = rd.randrange(0, 256)
        bild.putpixel((x, y), (r, g, b))

bild.save("02_zufallspixel_ergebnis.png")
