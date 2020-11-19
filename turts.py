import turtle

#set up turtles
leo = turtle.Turtle()
raf = turtle.Turtle()
don = turtle.Turtle()
mik = turtle.Turtle()

leo.color("blue")
leo.shape("turtle")
leo.speed(1)

raf.color("red")
raf.shape("turtle")
raf.speed(1)

don.color("orange")
don.shape("turtle")
don.speed(1)

mik.color("purple")
mik.shape("turtle")
mik.speed(1)

#move into position while hidden

raf.hideturtle()
raf.penup()
raf.goto(0, -20)
raf.pendown()
raf.showturtle()

don.hideturtle()
don.penup()
don.goto(0, -40)
don.pendown()
don.showturtle()

mik.hideturtle()
mik.penup()
mik.goto(0, -60)
mik.pendown()
mik.showturtle()

#the race
leo.penup()
leo.goto(200, 0)
leo.pendown()

raf.penup()
raf.goto(150, -20)
raf.pendown()

don.penup()
don.goto(100, -40)
don.pendown()

mik.penup()
mik.goto(143, -60)
mik.pendown()

turtle.done()
