import random as rd

print("Bestimmen Sie Ihren Teamchef zufällig!")
name_1 = input("Name der 1. Person:")
name_2 = input("Name der 2. Person:")
name_3 = input("Name der 3. Person:")
name_4 = input("Name der 4. Person:")
namen = [name_1, name_2, name_3, name_4]
name_chef = rd.choice(namen)
print(f"{name_chef} ist der Teamchef.")
