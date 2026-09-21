# För att använda turtle måste modulen importeras
import turtle, random, math

# Skapa en turtle
padda = turtle.Turtle()

# Ändra på turtle
# Shape - "arrow", "turtle", "circle", "square", "triangle", "classic"
padda.shape("turtle")

# Shapesize,
padda.shapesize(2)

# Speed - 1 till 10, men 0 är snabbast
padda.speed(4)
# Röra på turtle - .forward, .back, .goto, .setx, .sety
padda.forward(300)
padda.goto(250, -300)
padda.setx(-100)

# Rotera - .right, .left, .seth
padda.right(180)
padda.forward(100)

# pensize
padda.pensize(5)
padda.forward(200)
# Penup, pendown
padda.penup()
padda.goto(0, 0)
padda.pendown()

# Byt med text - .pencolor
padda.pencolor("red")
padda.forward(200)

# .hideturtle(), .showturtle()
padda.hideturtle()
padda.goto(250, 250)
# Circle (radie, vinkel, streck)
padda.circle(50, 180, 3)

# Dot (storlek, färg)
padda.dot(30, "blue")
# Få data från turtle .pos, .xcor, .ycor, .heading
padda.showturtle()
padda.pencolor("green")
for _ in range(100):
    padda.forward(random.randint(30, 200))
    padda.right(random.randint(10, 360))
    if math.abs(padda.xcor()) > 320 or math.abs(padda.ycor()) > 320:
        padda.goto(0, 0)

# Distance (a,b)
apple = turtle.Turtle()
apple.shape("circle")
apple.color("red")

if padda.distance(apple) < 15:
    apple.goto(random.randint(-200, 200), random.randint(-200, 200))
# Skriv turtle.done() för att fönstret ska vara kvar öppet
turtle.done()
