import turtle

def draw_spiral():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    turtle.speed(0)
    turtle.bgcolor("black")
    turtle.pensize(2)
    turtle.shape("turtle")
    
    for i in range(60):
        turtle.color(colors[i % len(colors)])
        turtle.circle(100 + i * 5)
        turtle.left(10)
    
    turtle.done()

draw_spiral()