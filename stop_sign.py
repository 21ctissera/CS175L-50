#Chrishen Tissera
#Stop Sign Code

import turtle
sign = turtle.Turtle()
sign.color("red")
sign.shape("turtle")

sign.begin_fill()
for i in range (8):
    sign.forward(50)
    sign.left(45)
sign.end_fill()
sign.penup()
sign.goto(25, -25)
sign.left(90)

stop = turtle.Turtle()
stop.color('white')
stop.penup()
stop.goto(-17, 37)
stop.write('STOP', font=('Impact', '41'))
stop.hideturtle()


