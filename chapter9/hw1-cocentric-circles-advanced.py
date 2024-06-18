import turtle
import colorsys

# Set up the screen
win = turtle.Screen()
win.bgcolor("black")

# Create a turtle
t = turtle.Turtle()
t.speed(0)  # Fastest speed

# Number of circles
num_circles = 40

# Draw concentric circles with different colors
for i in range(num_circles):
    # Calculate the hue (color) based on the circle index
    hue = i / num_circles
    rgb_color = colorsys.hsv_to_rgb(hue, 1, 1)
    t.color(rgb_color)

    # Draw the circle
    t.penup()
    t.goto(0, -i * 10)  # Adjust the spacing between circles
    t.pendown()
    t.circle(10 + i * 10)  # Increase the circle radius

# Hide the turtle cursor
t.hideturtle()

# Keep the window open until manually closed
turtle.done()