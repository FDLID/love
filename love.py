#FDLID
import turtle
from math import pi, sin, cos

def draw_heart(w, h, iteration=0):
    if iteration >= len(colors):
        return
    
    t = turtle.Turtle()
    t.hideturtle()
    t.pensize(2.5)
    a = 0
    t.up()
    t.fillcolor(colors[iteration])
    t.begin_fill()
    while a < 2 * pi:
        x = w * (16 * sin(a) ** 3)
        y = h * (13 * cos(a) - 5 * cos(2 * a) - 2 * cos(3 * a) - cos(4 * a))
        t.goto(x, y)
        a += 0.02
        t.down()
    t.end_fill()

    draw_heart(w - 3, h - 2, iteration + 1)

    # Draw Text
    if iteration == len(colors) - 1:  # gambar teks di iterasi terakhir
        t.up()
        t.color("white")
        t.setpos(0, 0)
        t.write("I Love You epep <3", align="center", font=("verdana", 15, "bold"))
        t.down()

colors = ['pink', 'white', 'pink'] # tambahkan warna lain jika diperlukan

# setting layar
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("red")
screen.title("I Love You")

# Gambar hati <3
draw_heart(16, 16)

# membiatkan jendela tidak ditutup
turtle.done()
