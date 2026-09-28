# Source - https://stackoverflow.com/a/77996806
# Posted by ggorlen, modified by community. See post 'Timeline' for change history
# Retrieved 2026-09-28, License - CC BY-SA 4.0

from random import randint
from turtle import Screen, Turtle


def tick():
    for t in turtles:
        t.forward(1)

        if randint(0, 1):
            t.left(randint(-5, 5))

    screen.update()
    screen.ontimer(tick, 1000 // 30)


screen = Screen()
screen.tracer(0)
turtles = [Turtle() for _ in range(200)]

for t in turtles:
    t.setheading(randint(0, 360))

tick()
screen.exitonclick()
