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


for line in range(20):
    jackie.pencolor(random_color())
    jackie.circle(70)
    jackie.left(18)

screen = t.Screen()
screen.exitonclick()
