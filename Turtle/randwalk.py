import turtle
from turtle import Turtle
import random as rand
tim = Turtle()
dir = [0, 90, 180, 270]
tim.pensize(15)
tim.speed(200)
turtle.colormode(255)

def rand_color():
    r = rand.randint(0, 255)
    g = rand.randint(0, 255)
    b = rand.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color

for _ in range(200):
    tim.forward(30)
    tim.color(rand_color())
    tim.setheading(rand.choice(dir))
