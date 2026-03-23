import random as rd

dezimalzahl = rd.randrange(0, 256)
ergebnis_0 = dezimalzahl // 2
rest_0 = dezimalzahl % 2
ergebnis_1 = ergebnis_0 // 2
rest_1 = ergebnis_0 % 2
ergebnis_2 = ergebnis_1 // 2
rest_2 = ergebnis_1 % 2
ergebnis_3 = ergebnis_2 // 2
rest_3 = ergebnis_2 % 2
ergebnis_4 = ergebnis_3 // 2
rest_4 = ergebnis_3 % 2
ergebnis_5 = ergebnis_4 // 2
rest_5 = ergebnis_4 % 2
ergebnis_6 = ergebnis_5 // 2
rest_6 = ergebnis_5 % 2
ergebnis_7 = ergebnis_6 // 2
rest_7 = ergebnis_6 % 2
print(f"Dezimalzahl: {dezimalzahl}")
print(f"Binärzahl: {rest_7}{rest_6}{rest_5}{rest_4}{rest_3}{rest_2}{rest_1}{rest_0}")
