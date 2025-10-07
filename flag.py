import turtle
import math

# Параметры флага
FLAG_WIDTH = 600
FLAG_HEIGHT = 400
R = 80                # радиус диска солнца
NUM_RAYS = 40         # число лучей
RAY_OUT = 20          # длина луча вне круга
TUNDUK_LINE_GAP = 10  # расстояние между параллельными линиями түндука
TUNDUK_ANGLE = 45     # центральный угол обоих наборов линий

# Настройка экрана
screen = turtle.Screen()
screen.setup(FLAG_WIDTH+20, FLAG_HEIGHT+20)
screen.bgcolor("red")
screen.title("Флаг Кыргызстана")

# «Черепашка» для рисования
t = turtle.Turtle()
t.hideturtle()
t.speed("fastest")
t.penup()
t.goto(0, -FLAG_HEIGHT//2)  # сместим систему координат по центру
t.pendown()
t.setheading(0)

# 1) Солнце и лучи
t.penup()
t.goto(0, 0)
for i in range(NUM_RAYS):
    angle = 360 / NUM_RAYS * i
    t.setheading(angle)
    t.forward(R)
    t.pendown()
    t.forward(RAY_OUT)
    t.penup()
    t.backward(R + RAY_OUT)

# диск солнца
t.goto(0, -R)
t.setheading(0)
t.pendown()
t.color("yellow")
t.begin_fill()
t.circle(R)
t.end_fill()
t.penup()

# 2) Түндүк (символ крыши юрты)
t.color("red")
t.pensize(3)
length = R * 1.8  # длина линий, чтобы они выходили за кружок немного

# функция для рисования набора из трёх параллельных линий под углом alpha
def draw_tunduk_set(alpha):
    for offset in (-TUNDUK_LINE_GAP, 0, TUNDUK_LINE_GAP):
        t.goto(0, 0)
        t.setheading(alpha)
        # сдвиг линии перпендикулярно направлению
        perp = alpha + 90
        t.penup()
        t.setheading(perp)
        t.forward(offset)
        # возвращаемся к центру смещённой линии
        t.setheading(alpha)
        t.backward(length/2)
        t.pendown()
        t.forward(length)
        t.penup()

# две перекрещивающиеся «решётки»
draw_tunduk_set(TUNDUK_ANGLE)
draw_tunduk_set(180 - TUNDUK_ANGLE)

# Ждём клика, чтобы закрыть окно
screen.exitonclick()