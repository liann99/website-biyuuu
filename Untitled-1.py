import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("black")  # Set background to black

# Create a turtle object
pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(10)
pen.width(3)  # Set the width of the pen

# Function to draw a heart with gradient effect
def draw_heart():
    # First part of the heart
    pen.color("red")
    pen.begin_fill()
    pen.left(50)
    pen.forward(133)
    pen.circle(50, 200)
    pen.right(140)
    pen.circle(50, 200)
    pen.forward(133)
    pen.end_fill()

    # Adding a second layer for a gradient effect
    pen.color("pink")
    pen.left(130)
    pen.width(5)
    pen.begin_fill()
    pen.circle(60, 180)
    pen.right(90)
    pen.circle(60, 180)
    pen.end_fill()

# Function to add decorative strokes
def add_decorative_strokes():
    pen.width(2)
    pen.color("yellow")
    for i in range(36):
        pen.forward(100)
        pen.left(170)
        pen.forward(50)
        pen.left(170)
        pen.forward(100)
        pen.left(10)

# Draw the heart shape and decorative strokes
draw_heart()
add_decorative_strokes()

# Hide the turtle after drawing
pen.hideturtle()

# Keep the window open
screen.mainloop()
