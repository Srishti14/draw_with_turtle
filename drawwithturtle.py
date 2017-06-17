import turtle
def draw_square():
    screen = turtle.Screen()
    screen.bgcolor("pink")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("black")

    brad.forward(200)
    brad.right(90)
    brad.forward(200)
    brad.right(90)
    brad.forward(200)
    brad.right(90)
    brad.forward(200)
    brad.right(90)

    screen.exitonclick()

draw_square()
