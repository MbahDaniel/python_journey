import turtle
turtle.shape("turtle")
for i in range(0,4):
    turtle.forward (100)
    turtle.right(90)

turtle.exitonclick()

#question 2
turtle.shape("turtle")
for i in range(0,3):
    turtle.forward (100)
    turtle.left(120)

turtle.exitonclick()

#question 3
turtle.shape("turtle")
for i in range (0,360):
    turtle.forward(100)
    turtle.right(1)
turtle.hideturtle()

turtle.exitonclick()

#question 4
turtle.color("black","red")
turtle.begin_fill()
for i in range(0,4):
    turtle.forward(80)
    turtle.right(90)
turtle.penup()
turtle.end_fill()

turtle.pendown()
turtle.color("black","orange")
for i in range(0,4):
    turtle.forward(80)
    turtle.right(90)
turtle.penup()
turtle.end_fill()

turtle.pendown()
turtle.color("black","purple")
for i in range(0,4):
    turtle.forward(80)
    turtle.right(90)
turtle.penup()
turtle.end_fill()

turtle.exitonclick()


#question 5
turtle.shape("turtle")
for i in range(0,5):
    turtle.forward(80)
    turtle.right(120)

turtle.exitonclick()

#question 6
turtle.shape("turtle")
turtle.forward(100)
turtle.right(90)
turtle.penup()
turtle.forward(50)
turtle.pendown()
turtle.forward(100)
turtle.right(180)
turtle.forward(50)
turtle.right(90)
turtle.forward(100)
turtle.left(180)
turtle.forward(50)
turtle.right(90)
turtle.forward(100)
turtle.right(180)
turtle.penup()
turtle.forward(50)
turtle.pendown()
turtle.forward(100)
turtle.right(180)
turtle.forward(50)
turtle.right(90)
turtle.forward(75)
turtle.left(180)
turtle.forward(75)
turtle.right(180)
turtle.forward(50)
turtle.right(90)
turtle.forward(100)
turtle.left(180)

turtle.hideturtle()

turtle.exitonclick()


#question 7
import random
for i in range (0,8):
 turtle.color(random.choice(["orange","red","purple","blue","yellow","green"]))
 turtle.forward(60)
 turtle.right(45)

turtle.exitonclick()

#question 8
import random
for i in range(0,10):
    turtle.right(36)
    for i in range(0,5):
        turtle.forward(50)
        turtle.right(45)
turtle.hideturtle()

turtle.exitonclick()

#question 9
import random
import turtle

lines = random.randint(1,10)
for i in range (0,lines):
  length = random.randint(20,100)
  rotate = random.randint(0,360)