import turtle
def draw_rhombus(some_turtle):
    for i in range(1,3):
        some_turtle.forward(100)
        some_turtle.right(45)
        some_turtle.forward(100)
        some_turtle.right(135)

def draw_line(some_line):
    some_line.right(90)
    some_line.forward(300)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("white")
    brad = turtle.Turtle()
    brad.shape("circle")
    brad.color("blue")
    brad.speed(10)

    for _ in range(1,37):
        draw_rhombus(brad)
        brad.right(10)

    for x in range(1,2):
       draw_line(brad)

    window.exitonclick()

draw_art()
