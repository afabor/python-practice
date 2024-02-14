from turtle import Turtle
from random import randint

Fred = Turtle()
Samantha = Turtle()

Fred.color('green')
Fred.shape('turtle')

Samantha.color('purple')
Samantha.shape('turtle')

Fred.penup()
Fred.goto(-160,70)
Fred.pendown()

Samantha.penup()
Samantha.goto(-160, 50)
Samantha.pendown()

for movement in range(100):
    Fred.forward(randint(1,5))
    Samantha.forward(randint(1,5))

input('Enter to close')