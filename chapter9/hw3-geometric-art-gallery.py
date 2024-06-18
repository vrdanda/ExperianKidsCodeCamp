import turtle
import random
import colorsys

# Set up the screen
win = turtle.Screen()
win.bgcolor("black")

# Create a turtle
t = turtle.Turtle()
t.speed(0)  # Fastest speed

# Function to draw a colorful square
def draw_square(size):
    for _ in range(4):
        hue = random.random()  # Random hue for each side
        rgb_color = colorsys.hsv_to_rgb(hue, 1, 1)
        t.color(rgb_color)
        t.forward(size)
        t.right(90)

# Function to draw a colorful triangle
def draw_triangle(size):
    for _ in range(3):
        hue = random.random()  # Random hue for each side
        rgb_color = colorsys.hsv_to_rgb(hue, 1, 1)
        t.color(rgb_color)
        t.forward(size)
        t.right(120)

# Function to draw a colorful circle
def draw_circle(size):
    hue = random.random()  # Random hue for the circle
    rgb_color = colorsys.hsv_to_rgb(hue, 1, 1)
    t.color(rgb_color)
    t.circle(size)

# Draw your unique geometric artwork
# Feel free to experiment with shapes, sizes, and colors!
for _ in range(1000):
    x = random.randint(-500, 500)
    y = random.randint(-500, 500)
    t.penup()
    t.goto(x, y)
    t.pendown()

    shape = random.choice(["square", "triangle", "circle"])
    size = random.randint(20, 100)

    if shape == "square":
        draw_square(size)
    elif shape == "triangle":
        draw_triangle(size)
    elif shape == "circle":
        draw_circle(size)

# Hide the turtle cursor
t.hideturtle()

# Keep the window open until manually closed
turtle.done()
