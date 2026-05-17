import PIL.Image as img

bild = img.new("RGB", (10, 10))
rot = (225, 26, 39)
weiss = (255, 255, 255)

for x in range(0, 10):
    bild.putpixel((x, 0), rot)
    bild.putpixel((x, 1), rot)
    bild.putpixel((x, 2), rot)
    bild.putpixel((x, 3), rot)
    bild.putpixel((x, 4), rot)
    bild.putpixel((x, 5), rot)
    bild.putpixel((x, 6), rot)
    bild.putpixel((x, 7), rot)
    bild.putpixel((x, 8), rot)
    bild.putpixel((x, 9), rot)

for x in range(1, 9):
    bild.putpixel((x, 4), weiss)
    bild.putpixel((x, 5), weiss)

for y in range(1, 9):
    bild.putpixel((4, y), weiss)
    bild.putpixel((5, y), weiss)

bild.save("07_schweizer_kreuz_ergebnis.png")
