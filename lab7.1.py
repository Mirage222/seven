import turtle
turtlePen = turtle.Turtle()
window = turtle.Screen()
window.bgcolor("black")
def polygon(n, size=80):
    if n > 2:
        angle = 360 / n