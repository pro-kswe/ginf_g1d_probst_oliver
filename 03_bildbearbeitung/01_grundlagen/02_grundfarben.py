import PIL.Image as img

bild = img.new("RGB", (3, 2))
bild.putpixel((0, 0), (255, 0, 0))
bild.putpixel((1, 0), (0, 255, 0))
bild.putpixel((2, 0), (0, 0, 255))
bild.putpixel((0, 1), (255, 255, 0))
bild.putpixel((1, 1), (0, 255, 255))
bild.putpixel((2, 1), (255, 0, 255))
bild.save("02_grundfarben_ergebnis.png")
