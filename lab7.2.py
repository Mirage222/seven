import turtle
square = turtle.Turtle()
square.color("red","green")
square.begin_fill()
for j in range(3):
    square.left(20)
    for i in range(4):
        square.forward(100)
        square.left(90)