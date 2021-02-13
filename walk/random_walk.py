from turtle import Turtle, Screen
import random

jackie = Turtle()
jackie.shape("turtle")
jackie.color("dark slate gray")

colors = ["orange red", "red", "tomato", "light coral", "pink", "brown", "purple", "firebrick", "maroon"]
direction = [0, 90, 180, 270]
jackie.pensize(10)
jackie.speed("fastest")

def draw_path():
    jackie.pencolor(random.choice(colors))
    jackie.forward(25)
    jackie.setheading(random.choice(direction))

for line in range(200):
    draw_path()

screen = Screen()
screen.exitonclick()
