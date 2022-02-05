from turtle import Turtle


tommy = Turtle()
dave = Turtle()
jonny = Turtle()
peter = Turtle() 
#names of the turtle

tommy.color('red')
tommy.shape('turtle')

dave.color('blue')
dave.shape('turtle')

jonny.color('green')
jonny.shape('turtle')

peter.color('yellow')
peter.shape('turtle')

tommy.penup()
tommy.goto(-160, 100)
tommy.pendown

dave.penup()
dave.goto(-160, 70)
dave.pendown

jonny.penup()
jonny.goto(-160, 40)
jonny.pendown

peter.penup()
peter.goto(-160, 10)
peter.pendown

from random import randint

for i in range(100):
    tommy.forward(randint(1,5))
    dave.forward(randint(1,5))
    jonny.forward(randint(1,5))
    peter.forward(randint(1,5))


input("Press Enter to close")

