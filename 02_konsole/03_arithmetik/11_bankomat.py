import random as rd

betrag = rd.randrange(100, 2001)
anzahl_1000 = betrag // 1000
rest_1 = betrag % 1000
anzahl_200 = rest_1 // 200
rest_2 = rest_1 % 200
anzahl_100 = rest_2 // 100
rest_3 = rest_2 % 100
anzahl_50 = rest_3 // 50
rest_4 = rest_3 % 50
anzahl_20 = rest_4 // 20
rest_5 = rest_4 % 20
anzahl_10 = rest_5 // 10
anzahl_einer = rest_5 % 10

print("RANDOM-Bankomat")
print(f"Es werden CHF {betrag} abgehoben.")
print(f"1000er: {anzahl_1000}")
print(f"200er: {anzahl_200}")
print(f"100er: {anzahl_100}")
print(f"50er: {anzahl_50}")
print(f"20er: {anzahl_20}")
print(f"10er: {anzahl_10}")
print(f"Münzen: {anzahl_einer}")
