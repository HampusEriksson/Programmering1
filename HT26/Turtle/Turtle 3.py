import turtle, random, math

# Inställningar
screen = turtle.Screen()
screen.setup(width=800, height=600)
padda = turtle.Turtle()
padda.shapesize(5)
padda.penup()
screen.tracer(0)

apple = turtle.Turtle()

# Turtle för score
score_turtle = turtle.Turtle()
score_turtle.hideturtle()
score_turtle.penup()
score_turtle.goto(150, 150)
score_turtle.color("black")

score = 0


def uppdatera_score():
    global score
    score += 1
    score_turtle.clear()
    score_turtle.write(f"Score: {score}", font=("Arial", 24, "normal"))


# Funktioner som bara ändrar variabeln 'riktning'
def go_up():
    padda.setheading(90)


def go_down():
    # seth är samma som setheading
    padda.seth(270)


def go_left():
    padda.seth(180)


def go_right():
    padda.seth(0)


def go_diag():
    padda.goto(padda.xcor() + 2, padda.ycor() + 2)


# Koppla tangenter
screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")
screen.onkeypress(go_diag, "space")


# Huvudloopen som sköter rörelsen
def flytta():

    padda.forward(5)

    # Kör denna funktion igen efter 20 millisekunder
    # if math.abs(padda.xcor()) > 400 or math.abs(padda.ycor()) > 300:
    #    score -= 2
    screen.ontimer(flytta, 20)

    if math.fabs(padda.xcor()) > 400:
        padda.hideturtle()
        padda.setx(-padda.xcor())
        padda.showturtle()

    if padda.distance(apple) < 20:
        uppdatera_score()
        apple.goto(random.randint(-200, 200), random.randint(-200, 200))


flytta()  # Starta rörelsen
uppdatera_score()
screen.mainloop()
