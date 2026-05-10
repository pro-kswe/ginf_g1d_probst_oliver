import PIL.Image as img

bild = img.new("RGB", (2, 2))
bild.putpixel((0, 0), (0, 110, 190))
bild.putpixel((1, 0), (200, 90, 20))
bild.putpixel((0, 1), (241, 139, 13))
bild.putpixel((1, 1), (69, 178, 69))
bild.save("01_beispiel_ergebnis.png")
