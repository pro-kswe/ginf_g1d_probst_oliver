import turtle as t
import random as rd

a = rd.randrange(25, 51)
stärke = rd.randrange(1, 6)
t.pensize(stärke)
farbe = "blue"
t.pencolor(farbe)

for _ in range(10):
    for _ in range(4):
        t.fd(a)
        t.lt(90)
    t.fd(a)
