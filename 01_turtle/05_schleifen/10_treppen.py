import turtle as t
import random as rd

t.speed(10)
a = rd.randrange(10, 26)

for _ in range(4):
    for _ in range(10):
        t.fd(a)
        t.rt(90)
        t.fd(a)
        t.lt(90)
    t.fd(a)
    t.rt(90)
