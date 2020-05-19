import turtle

my_turtle = turtle.Turtle()


def square(length, angle):
    my_turtle.forward(length)
    my_turtle.left(angle)
    my_turtle.forward(length)


for i in range(1000000):
    square(100, 100)

