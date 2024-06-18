import turtle
import colorsys

#the draw_cocentric_circles function is the main code here, the rest is boilerplate code to draw the coordinate plane
def draw_cocentric_circles():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    turtle.speed(10)
    turtle.pensize(2)
    turtle.shape("turtle")
    
    for i in range(10):
        turtle.color(colors[i % len(colors)])
        turtle.penup()
        turtle.goto(0,-10+i*-10)
        turtle.pendown()
        turtle.circle(10 + i * 10)
    turtle.done()



# Set up the turtle screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("Concentric Circles with Axes")

# Create a turtle for drawing
pen = turtle.Turtle()
pen.speed("fastest")

# Draw the x and y axes
pen.penup()
pen.goto(-300, 0)
pen.pendown()
pen.goto(300, 0)
pen.penup()
pen.goto(0, -300)
pen.pendown()
pen.goto(0, 300)

# Add labels to the x and y axes
pen.penup()
pen.goto(320, 10)
pen.pendown()
pen.write("X", align="center", font=("Arial", 12, "normal"))
pen.penup()
pen.goto(10, 320)
pen.pendown()
pen.write("Y", align="center", font=("Arial", 12, "normal"))

# Add tick marks and labels on the x-axis
for x in range(-250, 251, 50):
    pen.penup()
    pen.goto(x, -10)
    pen.pendown()
    pen.goto(x, 10)
    pen.penup()
    pen.goto(x, -30)
    pen.pendown()
    pen.write(str(x), align="center", font=("Arial", 10, "normal"))

# Add tick marks and labels on the y-axis
for y in range(-250, 251, 50):
    pen.penup()
    pen.goto(-10, y)
    pen.pendown()
    pen.goto(10, y)
    pen.penup()
    pen.goto(-30, y)
    pen.pendown()
    pen.write(str(y), align="center", font=("Arial", 10, "normal"))




draw_cocentric_circles()



# Hide the turtle cursor
pen.hideturtle()

# Keep the window open
turtle.done()

