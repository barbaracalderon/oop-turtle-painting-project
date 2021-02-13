from turtle import Turtle, Screen
import random

jackie = Turtle()
jackie.shape("turtle")
jackie.color("dark slate gray")

colors = ["orange red", "red", "tomato", "light coral", "pink", "brown", "purple", "firebrick", "maroon"]

jackie.left(90)
jackie.penup()
jackie.forward(200)
jackie.left(90)
jackie.forward(70)
jackie.left(90)
jackie.left(90)
jackie.pendown()

def draw_shape(number_sides):
    angle = 360/number_sides
    for line in range(number_sides):
        jackie.forward(100)
        jackie.right(angle)

for shape_side_number in range(3, 13):
    jackie.pencolor(random.choice(colors))
    draw_shape(shape_side_number)

screen = Screen()
screen.exitonclick()
