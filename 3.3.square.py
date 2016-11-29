def draw_square(x,y):
    import turtle
    turtle.color(y)
    for i in range(0,4):
        turtle.forward(100)
        turtle.left(90)
##length = int(input("Length = "))
##color = input("Color? ")
##draw_square(length,color)
import turtle
for i in range(0,30):
    draw_square(i * 5, 'red')
    turtle.left(17)
    turtle.penup()
    turtle.forward(i * 2)
    turtle.pendown()
