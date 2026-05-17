import PIL.Image as img
import random as rd

bild = img.new("RGB", (2, 2))
graustufe_1 = rd.randrange(0, 256)
graustufe_2 = rd.randrange(0, 256)
graustufe_3 = rd.randrange(0, 256)
graustufe_4 = rd.randrange(0, 256)
bild.putpixel((0, 0), (graustufe_1, graustufe_1, graustufe_1))
bild.putpixel((1, 0), (graustufe_2, graustufe_2, graustufe_2))
bild.putpixel((0, 1), (graustufe_3, graustufe_3, graustufe_3))
bild.putpixel((1, 1), (graustufe_4, graustufe_4, graustufe_4))
bild.save("04_graustufen_ergebnis.png")
