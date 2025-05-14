# Eduardo Paz
# 04/07/2025
# P4LAB1B
# Initials

import turtle

# Setup screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Initials: EP")

# Draw E
e = turtle.Turtle()
e.color('blue')
e.pensize(5)

e.penup()
e.goto(-200, 100)
e.setheading(270)
e.pendown()
e.forward(100)

# Top line
e.penup()
e.goto(-200, 100)
e.setheading(0)
e.pendown()
e.forward(60)

# Middle line
e.penup()
e.goto(-200, 50)
e.pendown()
e.forward(40)

# Bottom line
e.penup()
e.goto(-200, 0)
e.pendown()
e.forward(60)

# Draw P
p = turtle.Turtle()
p.color('purple')
p.pensize(5)

p.penup()
p.goto(100, -50)
p.setheading(90)
p.pendown()
p.forward(100)

p.right(90)
p.circle(-25, 180)

# Hide turtles
e.hideturtle()
p.hideturtle()

# Keep the window open
turtle.done()
