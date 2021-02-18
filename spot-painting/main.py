import colorgram

# color_list = []
# all_colors = colorgram.extract('damien_hirst.jpg', 100)
# for c in all_colors:
#     r = c.rgb.r
#     g = c.rgb.g
#     b = c.rgb.b
#     color_tuples = (r, g, b)
#     color_list.append(color_tuples)
#
# print(color_list)

color_list = [(135, 164, 199), (221, 153, 105), (30, 42, 60), (200, 137, 148), (157, 63, 53), (234, 212, 92), (50, 101, 141), (138, 180, 162), (147, 63, 72), (157, 31, 27), (163, 28, 34), (52, 46, 43), (53, 41, 44), (60, 114, 98), (230, 164, 170), (236, 166, 158), (210, 83, 71), (33, 59, 53), (17, 95, 70), (194, 97, 106), (171, 189, 220), (34, 60, 104), (108, 125, 160), (21, 80, 100), (174, 201, 191), (38, 150, 206), (64, 66, 57), (96, 146, 136), (165, 203, 214), (164, 122, 88)]

import turtle as t
import random

jackie = t.Turtle()
jackie.shape("circle")
t.colormode(255)
jackie.hideturtle()
jackie.penup()
jackie.backward(220)
jackie.right(90)
jackie.forward(220)
jackie.left(90)


def random_color(color_list):
    random_color_is = random.choice(color_list)
    return random_color_is


def draw_row():
    for line in range(9):
        jackie.color(random_color(color_list))
        jackie.stamp()
        jackie.forward(50)
        jackie.color(random_color(color_list))
        jackie.stamp()


for r in range(5):
    draw_row()
    jackie.left(90)
    jackie.forward(50)
    jackie.left(90)
    draw_row()
    jackie.right(90)
    jackie.forward(50)
    jackie.right(90)
jackie.clearstamp(1)

screen = t.Screen()
screen.exitonclick()
