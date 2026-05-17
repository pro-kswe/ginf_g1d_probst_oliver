import PIL.Image as img
import random as rd


bild = img.new("RGB", (500, 500))

for x in range(0, 500):
    r = (x * 2) % 256
    g = (x * 5) % 256
    b = (x * 8) % 256
    bild.putpixel((x, x), (r, g, b))

bild.save("10_diagonale_2_ergebnis.png")
