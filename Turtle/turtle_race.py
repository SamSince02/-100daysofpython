import turtle
from turtle import Turtle, Screen
import random

my_screen = Screen()

my_screen.setup(width=500, height=400)
y_position = [-70, -40, -10, 20, 50, 80]
colors = ["red", "yellow", "blue", "black", "brown", "cyan"]
all_turtles = []
user_turtle=my_screen.textinput("name", "Enter your turtle color: ")

for turtle_index in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)
is_race = True
while is_race:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            winning_color = turtle.pencolor()
            is_race = False
            if user_turtle==winning_color:
                print(f"You Won!!, {winning_color} has won the race")
            else:
                print(f"You Lost!!, {winning_color} has won the race")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)





my_screen.exitonclick()