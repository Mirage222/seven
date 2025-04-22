import turtle
bg_color = "yellow" 
circle_color = "purple"
screen = turtle.Screen()
screen.bgcolor(bg_color)
t = turtle.Turtle()
circle_size = 10
num_circles = 10
circle_spacing = 15
start_x = -200
start_y = 200
t.penup()
t.goto(start_x, start_y)
t.pendown()
for i in range(num_circles):
   for j in range(num_circles):
       t.fillcolor(circle_color)
       t.begin_fill()
       t.circle(circle_size)
       t.end_fill()
       t.penup()
       t.forward(circle_size + circle_spacing)
       t.pendown()
   t.penup()
   t.goto(start_x, t.ycor() - (circle_size + circle_spacing))
   t.pendown()
screen.exitonclick()