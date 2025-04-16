num_sides = 2


def change_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    justin.pencolor(r, g, b)


def draw_all_shapes(sides):
    for _ in range(sides):
        justin.right((360/sides))
        justin.forward(100)
        change_color()


for _ in range(8):
    num_sides += 1
    draw_all_shapes(num_sides)


def random_walk():
    """Makes the turtle object move forward then randomly change direction and color."""
    justin.forward(25)
    angles = [90, 180, 270, 360]
    turn_angle = random.choice(angles)
    justin.setheading(turn_angle)
    change_color()


turtle.colormode(255)

justin = Turtle()

justin.shape("arrow")
justin.turtlesize(0.5)
justin.speed("fastest")
justin.pensize(1)



def change_color():
    """Generates a random color for the pencolor and turtle color based on r, g, b, tuples."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    justin.pencolor(r, g, b)
    justin.fillcolor(r, g, b,)

def draw_spirograph(gap_size):
    for _ in range(int(360 / gap_size)):
        justin.circle(150)
        justin.setheading(justin.heading() + gap_size)
        change_color()

draw_spirograph(25)