import random
import turtle

x_1 = random.randrange(-100, 101)
x_2 = random.randrange(-100, 101)
x_3 = random.randrange(-100, 101)
y_1 = random.randrange(-200, 276)
y_2 = random.randrange(-200, 276)
y_3 = random.randrange(-200, 276)
d = random.randrange(10, 26)
farbe_1 = "red"  # Strings sind in Python Text mit Anführungszeichen.
farbe_2 = "green"
farbe_3 = "blue"
stiftstarke = 3  # Integers oder kurz Ints sind in Python ganze Zahlen.
turtle.pensize(stiftstarke)
turtle.pu()
turtle.goto(x_1, y_1)
turtle.pd()
turtle.pencolor(farbe_1)
turtle.dot(d)
turtle.goto(x_2, y_2)
turtle.pencolor(farbe_2)
turtle.dot(d)
turtle.goto(x_3, y_3)
turtle.pencolor(farbe_3)
turtle.dot(d)
turtle.goto(x_1, y_1)
