import turtle
import random

durchmesser = random.randrange(10, 31)
x = random.randrange(-100, 101)
y = random.randrange(-100, 101)
farbe = "orange"
turtle.pu()
turtle.goto(x, y)
turtle.pencolor(farbe)
turtle.dot(durchmesser)
