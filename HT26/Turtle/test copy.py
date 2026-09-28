import random, turtle

screen = turtle.Screen()
a = turtle.Turtle()
a.color("red")
a.seth(180)
b = turtle.Turtle()
b.color("blue")
screen.tracer(0)

keys = {"Right": False, "d": False}


def move():
    if keys["Right"]:
        b.forward(5)
    if keys["d"]:
        a.forward(5)
    screen.update()
    screen.ontimer(move, 16)


screen.onkeypress(lambda: keys.update({"Right": True}), "Right")
screen.onkeyrelease(lambda: keys.update({"Right": False}), "Right")
screen.onkeypress(lambda: keys.update({"d": True}), "d")
screen.onkeyrelease(lambda: keys.update({"d": False}), "d")
screen.listen()
move()
screen.exitonclick()
