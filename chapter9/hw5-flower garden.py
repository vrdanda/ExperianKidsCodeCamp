import turtle
import random

# Create a new turtle screen and set its background color
screen = turtle.Screen()
screen.bgcolor("white")

# Create a new turtle object
garden = turtle.Turtle()

# Define a list of colors
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Define a function to draw a leaf
def draw_leaf(turtle, size):
    turtle.speed(0)
    turtle.begin_fill()
    turtle.forward(size)
    turtle.right(135)
    turtle.forward(size)
    turtle.right(135)
    turtle.forward(size)
    turtle.right(135)
    turtle.forward(size)
    turtle.right(135)
    turtle.end_fill()

# Define a function to draw a flower
def draw_flower(turtle, size):
    for _ in range(36):  # Draw a flower
        turtle.speed(0)
        turtle.color(random.choice(colors))  # Choose a random color
        turtle.forward(size)
        turtle.right(170)
    turtle.right(10)

# Draw a garden of flowers
for i in range(5):
    for j in range(5):
        garden.penup()
        garden.goto(i*100-200, j*100-200)  # Move to the next position
        garden.pendown()
        draw_flower(garden, 50)  # Draw a flower
        garden.right(90)  # Draw the stem
        garden.color("green")
        garden.forward(50)
        draw_leaf(garden, 20)  # Draw a leaf
        garden.backward(50)
        garden.left(90)

# Hide the turtle and display the result
garden.hideturtle()
turtle.done()
