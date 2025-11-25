import turtle as t
import random as rd

t.speed(10)
farbe = "red"
t.pencolor(farbe)

for _ in range(5):
    a = rd.randrange(50, 201)
    for _ in range(5):
        t.fd(a)
        t.rt(144)
    t.lt(72)
