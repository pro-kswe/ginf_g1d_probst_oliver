import random as rd

wochentage = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
wochentag = rd.choice(wochentage)
print(f"Heute ist: {wochentag}")

if wochentag != "Sonntag":
    print("Heute ist ein Werktag.")
    
print("Ich wünsche Ihnen einen schönen Tag.")
