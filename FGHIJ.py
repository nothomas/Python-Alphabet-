import turtle

s = turtle.getscreen()
t = turtle.Turtle()

#Starting Point
t.penup()
t.right(90)
t.forward(25)
t.left(90)
t.backward(300)
t.pendown()

#Drawing the letter F
t.pen(pencolor="black", fillcolor="red", pensize=5, speed=5)
t.begin_fill()
t.left(90)
t.forward(120)
t.right(90)
t.forward(70)
t.right(90)
t.forward(20)
t.left(90)
t.backward(40)
t.right(90)
t.forward(30)
t.left(90)
t.forward(30)
t.right(90)
t.forward(20)
t.left(90)
t.backward(30)
t.right(90)
t.forward(50)
t.left(90)
t.backward(30)
t.end_fill()

#Space
t.penup()
t.left(90)
t.forward(100)
t.right(90)
t.forward(160)

#Drawing the Letter G
t.pen(pencolor="black", fillcolor="yellow", pensize=5, speed=5)
t.begin_fill()
t.pendown()
t.circle(-40,-180)
t.right(90)
t.forward(30)
t.left(90)
t.forward(20)
t.right(90)
t.forward(15)
t.right(90)
t.forward(40)
t.right(90)
t.forward(65)
t.right(90)
t.forward(20)
t.circle(-60,200)
t.right(90)
t.forward(20)
t.right(90)
t.forward(10)
t.end_fill()

#Space
t.penup()
t.right(160)
t.forward(60)
t.left(90)
t.forward(15)
t.right(90)

#Drawing the Letter H
t.pen(pencolor="black", fillcolor="green", pensize=5, speed=5)
t.begin_fill()
t.pendown()
t.forward(30)
t.right(90)
t.forward(40)
t.left(90)
t.forward(30)
t.left(90)
t.forward(40)
t.right(90)
t.forward(30)
t.right(90)
t.forward(120)
t.left(90)
t.backward(30)
t.left(90)
t.forward(40)
t.right(90)
t.backward(30)
t.right(90)
t.forward(40)
t.left(90)
t.backward(30)
t.left(90)
t.forward(120)
t.end_fill()

#Space
t.penup()
t.right(90)
t.forward(140)

#Drawing the Letter I
t.pen(pencolor="black", fillcolor="blue", pensize=5, speed=5)
t.begin_fill()
t.pendown()
t.right(90)
t.forward(30)
t.left(90)
t.forward(30)
t.right(90)
t.forward(60)
t.left(90)
t.backward(30)
t.right(90)
t.forward(30)
t.left(90)
t.forward(90)
t.left(90)
t.forward(30)
t.right(90)
t.backward(30)
t.left(90)
t.forward(60)
t.right(90)
t.forward(30)
t.left(90)
t.forward(30)
t.right(90)
t.backward(90)
t.end_fill()

#Space
t.penup()
t.right(90)
t.forward(70)
t.left(90)
t.forward(130)

#Drawing the Letter J
t.pen(pencolor="black", fillcolor="orange", pensize=5, speed=5)
t.begin_fill()
t.pendown()
t.forward(30)
t.backward(30)
t.right(90)
t.circle(50,180)
t.forward(70)
t.right(90)
t.backward(30)
t.right(90)
t.forward(70)
t.circle(-20,180)
t.end_fill()