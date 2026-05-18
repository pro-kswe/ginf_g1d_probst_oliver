import PIL.Image as img
import random as rd

bild = img.new("RGB", (1200, 750))

for x in range(0, bild.width):
    r = rd.randrange(0, 256)
    g = rd.randrange(0, 256)
    b = rd.randrange(0, 256)
    for y in range(0, bild.height):
        bild.putpixel((x, y), (r, g, b))
        
bild.save("03_vertikale_streifen_ergebnis.png")
