from random import*
from tkinter import*
size=500
tk=Tk()
diapason=0
my_canvas = Canvas(tk, width=size, height=size)
my_canvas.pack()
while diapason<1000:
  color=choice(['red','blue', 'cyan', 'green', 'yellow'])
  x1 = randint(0, size)
  y1 = randint(0, size)
  d = randint(5, 150)
  my_canvas.create_oval(x1, y1, x1+d, y1+d, fill=color)
  tk.update()
  diapason+=1