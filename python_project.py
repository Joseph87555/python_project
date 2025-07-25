    
import turtle
tom=turtle.Turtle()
color=("green")

def tyre():
    tom.setheading(0)

    tom.circle(25)

def move(x,y):
    tom.penup()
    tom.goto(x,y)
    tom.pendown()

def rear():
    tom.right(32)
    tom.circle(100,-100)
    tom.right(25)
    tom.circle(300,-100)

    tom.right(50)
    tom.circle(221,-20)

    tom.right(31)
    tom.circle(-160,-10)

    tom.left(31)
    tom.forward(20)
move(-120,-100)
tyre()
move(100,-100)
tyre()
move(-120,-110)
tom.fd(200)

move(-100,-45)
rear()

tom.penup()
tom.bk(140)
tom.pendown()
tom.forward(140)

tom.penup()
tom.bk(140)
tom.pendown()
tom.left(150)
tom.penup()
tom.bk(70)
tom.penup()
#Start from rear
tom.forward(90)
tom.pendown()
tom.right(120)
tom.forward(50)
tom.right(41)
tom.forward(50) 
tom.right(80)
tom.forward(110)
tom.forward(90)
tom.right(90)
tom.forward(50)
tom.left(90)
tom.forward(50)
tom.right(90)
tom.forward(110)
#Stop on the front 
tom.penup()

tom.penup()
tom.bk(200)
tom.pd()
tom.right(90)
tom.forward(150)
tom.bk(100)
tom.right(90)
tom.forward(40)





#done//
turtle.done()
