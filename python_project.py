    
import turtle
tom=turtle.Turtle()
color=("green")

def tyre():
    tom.setheading(0)

    tom.circle(25)


def tyre():
    tom.setheading(0)

    tom.circle(20)

def move(x,y):
    tom.penup()
    tom.goto(x,y)
    tom.pendown()

def rear():
    tom.right(30)
    tom.circle(100,-100)
    tom.right(25)
    tom.circle(200,-100)

    tom.right(52)
    tom.circle(200,-100)

    tom.right(31)
    tom.circle(-120,-10)

    tom.left(31)
    tom.forward(20)
move(-120,-100)
tyre()
move(100,-100)
tyre()
move(-120,-110)
tom.fd(200)

move(-100,-20)
rear()
move(-100,201)
tyre()
move(100,-100)
tyre()
move(-120,-100)
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
tom.bk(100)
tom.pd()
tom.right(90)
tom.forward(120)
tom.bk(100)
tom.right(90)
tom.forward(40)





#done//
turtle.done()

