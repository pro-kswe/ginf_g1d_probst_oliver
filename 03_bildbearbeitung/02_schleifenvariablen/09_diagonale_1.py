import PIL.Image as img
import random as rd


bild = img.new("RGB", (256, 256))

for x in range(0, 256):
    bild.putpixel((x, x), (x, 0, 0))

bild.save("09_diagonale_1_ergebnis.png")
