
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
    tom.right(31)
    tom.circle(100,-20)
    tom.right(20)
    tom.circle(300,-10)

    tom.right(50)
    tom.circle(220,-20)

    tom.right(31)
    tom.circle(-160,-10)

    tom.left(31)
    tom.forward(200)
'''    

move(-150,-100)
tyre()

move(100,-100)

tyre()


move(-120,-95)
tom.fd(200)
'''
move(-180,-95)
rear()

'''
tom.penup()
tom.bk(140)
tom.pendown()
tom.forward(140)
tom.penup()
tom.bk(140)
tom.pendown()
tom.left(160)
#start for rear
tom.penup()
tom.bk(70)
tom.forward(90)
tom.pendown()
tom.right(45)
tom.forward(50)
tom.right(41)
tom.forward(50)
tom.right(80)
tom.forward(150)
tom.forward(90)
tom.right(90)
tom.forward(50)
tom.left(90)
tom.forward(50)
tom.right(170)
tom.forward(100)
tom.penup()
'''

#done//
turtle.done()

'''
jyjhyrjhy
