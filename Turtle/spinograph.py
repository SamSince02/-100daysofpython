import turtle
from turtle import Turtle
import random as rand

tim = Turtle()
turtle.colormode(255)
tim.speed(100)

def rand_color():
    r = rand.randint(0, 255)
    g = rand.randint(0, 255)
    b = rand.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color

for _ in range(200):
    tim.color(rand_color())
    tim.circle(100)
    tim.right(5)
