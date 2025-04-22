import turtle

def draw_angry_smiley():
    screen = turtle.Screen()
    screen.bgcolor("white")

    smiley = turtle.Turtle()
    smiley.speed(10)

    # Рисуем лицо
    smiley.penup()
    smiley.goto(0, -200)
    smiley.pendown()
    smiley.color("yellow")
    smiley.begin_fill()
    smiley.circle(200)
    smiley.end_fill()

    # Рисуем глаза
    smiley.penup()
    smiley.goto(-80, 50)
    smiley.pendown()
    smiley.color("black")
    smiley.begin_fill()
    smiley.circle(20)
    smiley.end_fill()

    smiley.penup()
    smiley.goto(80, 50)
    smiley.pendown()
    smiley.begin_fill()
    smiley.circle(20)
    smiley.end_fill()

    # Рисуем хмурый рот (ломаная линия)
    smiley.penup()
    smiley.goto(-100, -80)
    smiley.pendown()
    smiley.width(5)
    smiley.goto(0, -120)
    smiley.goto(100, -80)

    # Рисуем нахмуренные брови
    smiley.width(7)
    smiley.penup()
    smiley.goto(-100, 120)
    smiley.pendown()
    smiley.goto(-50, 150)

    smiley.penup()
    smiley.goto(100, 120)
    smiley.pendown()
    smiley.goto(50, 150)

    smiley.hideturtle()
    screen.mainloop()

# Вызов функции
draw_angry_smiley()

