from turtle import Turtle, Screen

tommy = Turtle()
for _ in range(10):
    tommy.forward(10)
    tommy.penup()
    tommy.forward(10)
    tommy.pendown()

my_screen = Screen()
my_screen.exitonclick()