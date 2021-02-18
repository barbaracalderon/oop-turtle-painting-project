import turtle as t
import random

jackie = t.Turtle()
t.colormode(255)
jackie.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

def draw_spirograph(gap_size):
    for line in range(int(360/gap_size)):
        jackie.pencolor(random_color())
        jackie.circle(70)
        jackie.left(gap_size)

draw_spirograph(1)

screen = t.Screen()
screen.exitonclick()
