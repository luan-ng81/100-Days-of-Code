###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
# import colorgram
import turtle
from turtle import Turtle
from random import  choice

COLS = 10
ROWS = 10
SPACING = 50
DOT = 20

start_x = -(COLS - 1) * SPACING / 2
start_y = -(ROWS - 1) * SPACING / 2

pen = Turtle()
pen.penup()
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
print(len(color_list))
turtle.colormode(255)  # allow RGB colors
pen.setposition(start_x, start_y)
pen.pendown()

for r in range(1, ROWS + 1):
    for c in range(COLS):
        pen.dot(DOT, choice(color_list))
        pen.penup()
        pen.forward(SPACING)
        pen.pendown()
    next_x = -(COLS - 1) * SPACING / 2
    next_y = -(ROWS - 1 - r) * SPACING / 2
    pen.penup()
    pen.setposition(next_x, next_y)
    pen.pendown()



turtle.done()
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
#
# print(rgb_colors)