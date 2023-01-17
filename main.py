# ###This code will not work in repl.it as there is no access to the colorgram package here.###
# ##We talk about this in the video tutorials##
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('download.jpg', 30)
# for color in colors:
#     red = color.rgb.r
#     green = color.rgb.g
#     blue = color.rgb.b
#     hirst = (red, blue, green)
#     rgb_colors.append(hirst)
#
# print(rgb_colors)
import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.speed("fastest")
timmy.hideturtle()
timmy.penup()
turtle.colormode(255)
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)

color_list = [(236, 83, 225), (202, 72, 5), (198, 10, 164), (235, 129, 51), (206, 11, 76), (108, 218, 179), (219, 103, 162), (234, 6, 225), (30, 108, 188), (23, 173, 106), (13, 64, 23), (17, 175, 28), (213, 176, 135), (9, 214, 185), (205, 142, 29), (229, 197, 168), (125, 162, 189), (8, 28, 49), (37, 73, 132), (125, 233, 219), (67, 8, 22), (61, 26, 11), (111, 211, 89), (142, 201, 216), (190, 5, 15), (238, 31, 63)]
dots = 100
for dot_count in range(1, dots+1):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)
    if dot_count % 10 == 0:
        timmy.left(90)
        timmy.forward(50)
        timmy.left(90)
        timmy.forward(500)
        timmy.setheading(0)
screen = Screen()
screen.exitonclick()