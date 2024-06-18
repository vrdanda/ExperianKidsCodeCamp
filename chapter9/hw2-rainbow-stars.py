import random
import turtle
import colorsys

# Set up the screen
win = turtle.Screen()
win.bgcolor("black")

# Create a turtle
t = turtle.Turtle()
t.speed(0)  # Fastest speed

# Number of stars
num_stars = 100

# Draw stars
for _ in range(num_stars):
    # Random position for each star
    x = random.randint(-500, 500)
    y = random.randint(-500, 500)
    t.penup()
    t.goto(x, y)
    t.pendown()

    # Draw a colorful star
    for _ in range(5):
        hue = random.random()  # Random hue for each point
        rgb_color = colorsys.hsv_to_rgb(hue, 1, 1)
        t.color(rgb_color)
        t.forward(100)
        t.right(144)

# Hide the turtle cursor
t.hideturtle()

# Keep the window open until manually closed
turtle.done()
