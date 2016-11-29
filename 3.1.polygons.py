import turtle
turtle.color("red")
def shape(number):
    for i in range (0,number):
        if i%2==1:
            turtle.color("blue")
            turtle.forward(100)
            turtle.left(180 -(number-2)*180/number)
        else:
            turtle.color("red")
            turtle.forward(100)
            turtle.left(180 -(number-2)*180/number)
            
            
        
for i in range (4,10):
    shape(i)
