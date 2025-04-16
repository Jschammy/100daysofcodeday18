# modules
import turtle
from turtle import Turtle, Screen
import random
import colorgram

# variables
turtle.colormode(255)
justin = Turtle()
file_colors = colorgram.extract("hirst.jpg", 30)
tuple_list = []


# functions
def populate_list(colors, rgb_list):
    """Creates a list of color tuples from an image using colorgram."""
    for color in colors:
        rgb_tuple = (color.rgb[0], color.rgb[1], color.rgb[2])
        rgb_list.append(rgb_tuple)
    return


def paint():
    """Paints a Hirst painting using colors from the tuple list. """
    x = -250
    y = -250
    for _ in range(10):
        for _ in range(10):
            justin.teleport(x, y)
            justin.dot(20, random.choice(tuple_list))
            x += 50.00
        y += 50
        x = -250


populate_list(file_colors, tuple_list)
paint()

my_screen = Screen()
my_screen.exitonclick()
