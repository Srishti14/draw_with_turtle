import turtle
def draw_square(some_turtle):
    for i in range (4):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("red")
    zac = turtle.Turtle()
    zac.shape("turtle")
    zac.color("yellow")
    zac.speed(4)


    for _ in range(1,37):
        draw_square(zac)
        zac.right(10)



    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)
    angie.speed(2)

    #hailee = turtle.Turtle()
    #hailee.shape("arrow")
    #hailee.color("pink")
    #hailee.speed(2)

    #for x in range(3):
        #hailee.backward(200)
        #hailee.right(120)

    window.exitonclick()

draw_shapes()
