import turtle as t
import random

jackie = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


direction = [0, 90, 180, 270]
jackie.pensize(10)
jackie.speed("fastest")


for line in range(200):
    jackie.pencolor(random_color())
    jackie.forward(25)
    jackie.setheading(random.choice(direction))


screen = t.Screen()
screen.exitonclick()
