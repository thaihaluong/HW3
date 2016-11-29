from turtle import *

def draw_star(x,y,z):
    import turtle
    turtle.goto(x,y)
    turtle.left(108)
    for i in range (0,5):
        turtle.forward(z)
        turtle.left(144)

speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)
