#import colorgram
import random
import turtle
#rgb_color = []
#colors = colorgram.extract("image.jpg", 30)

#for color in colors:
    #r = color.rgb.r
    #g = color.rgb.g
    #b = color.rgb.b
    #new_color = (r, g, b)
    #rgb_color.append(new_color)

#print(rgb_color)

from turtle import Turtle, Screen
import random
colors = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

tim = Turtle()
tim.setx(0)
tim.sety(0)
turtle.colormode(255)
tim.speed(1000)
tim.hideturtle()
def move():
    for _ in range(10):
        tim.dot(10, random.choice(colors))
        tim.penup()
        tim.forward(30)
        tim.pendown()

move()

tim.penup()
tim.setx(0)
tim.sety(30)
tim.pendown()
move()

tim.penup()
tim.setx(0)
tim.sety(60)
tim.pendown()
move()

tim.penup()
tim.setx(0)
tim.sety(90)
tim.pendown()
move()

tim.penup()
tim.setx(0)
tim.sety(120)
tim.pendown()
move()

tim.penup()
tim.setx(0)
tim.sety(150)
tim.pendown()
move()

tim.penup()
tim.setx(0)
tim.sety(180)
tim.pendown()
move()

tim.penup()
tim.setx(0)
tim.sety(210)
tim.pendown()
move()

tim.penup()
tim.setx(0)
tim.sety(240)
tim.pendown()
move()

tim.penup()
tim.setx(0)
tim.sety(270)
tim.pendown()
move()

my_screen = Screen()
my_screen.exitonclick()