import turtle
import random
 
# Setup the screen
wn = turtle.Screen()
wn.title("Turtle Eat Dot Game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
 
# Setup thescore display
score = 0
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
 
# Setup the player turtle
player = turtle.Turtle()
player.shape("turtle")
player.color("blue")
player.penup()
player.speed(0)
 
# Setup the dot
dot = turtle.Turtle()
dot.shape("circle")
dot.color("red")
dot.penup()
dot.speed(0)
dot.goto(random.randint(-390, 390), random.randint(-290, 290))
 
# Function to update thescore
def update_score():
    score_display.clear()
    score_display.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
 
# Function to move the player up
def go_up():
    player.setheading(90)
    y = player.ycor()
    y += 20
    if y > 290:
        y = 290
    player.sety(y)
 
# Function to move the player down
def go_down():
    player.setheading(270)
    y = player.ycor()
    y -= 20
    if y < -290:
        y = -290
    player.sety(y)
 
# Function to move the player left
def go_left():
    player.setheading(180)
    x = player.xcor()
    x -= 20
    if x < -390:
        x = -390
    player.setx(x)
 
# Function to move the player right
def go_right():
    player.setheading(0)
    x = player.xcor()
    x += 20
    if x > 390:
        x = 390
    player.setx(x)

# Check for collision with the dot
def is_collision(t1, t2):
    distance = t1.distance(t2)
    return distance < 20

# Listen for keyboard inputs
wn.listen()
wn.onkey(go_up, "Up")
wn.onkey(go_down, "Down")
wn.onkey(go_left, "Left")
wn.onkey(go_right, "Right")
 
# Main game loop
while True:
    wn.update()

   # Check for collision between the player and the dot
    if is_collision(player, dot):
        # Move the dot to a random location
        dot.goto(random.randint(-390, 390), random.randint(-290, 290))
        
       # Change colors of the player and dot
        player.color(random.choice(["blue", "green", "yellow", "purple", "cyan", "magenta"]))
        dot.color(random.choice(["red", "orange", "pink", "lime", "coral", "lavender"]))
        
       # Increase thescore
        score += 10
        update_score()
         