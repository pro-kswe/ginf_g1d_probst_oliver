import random as rd

zahl = rd.randrange(1, 7)
print(f"Sie haben eine {zahl} gewürfelt.")

if zahl > 3:
    print("Sie dürfen gleich nochmal würfeln.")
