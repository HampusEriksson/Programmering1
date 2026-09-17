import turtle, random

padda = turtle.Turtle()
padda.shapesize(5)
padda.shape("turtle")
padda.penup()
padda.speed(0)
turtle.screensize(1200,800)

apple = turtle.Turtle()
apple.color("red")
apple.penup()
apple.goto(random.randint(-500, 500), random.randint(-500, 500))

while True:
    padda.forward(10)
    if padda.xcor() >= 600:
        padda.hideturtle()
        padda.goto(-600,random.randint(-500, 500))
        padda.showturtle()
    if padda.distance(apple) < 50:
        break


# Få data från turtle .pos, .xcor, .ycor, .heading
# Distance (a,b)
# Skriv turtle.done() för att fönstret ska vara kvar öppet

turtle.done()