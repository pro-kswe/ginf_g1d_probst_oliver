import PIL.Image as img

bild = img.new("RGB", (5, 4))
farbe = (255, 255, 255)
for x in range(0, 5):
    bild.putpixel((x, 1), farbe)
bild.save("01_beispiel_ergebnis.png")
