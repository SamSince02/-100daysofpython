from turtle import Turtle, Screen

tim = Turtle()
my_screen = Screen()

my_screen.listen()
def move_forward():
    tim.forward(50)

def move_backwards():
    tim.backward(50)

def turn_right():
    tim.right(60)

def turn_left():
    tim.left(60)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

my_screen.onkey(key="w", fun=move_forward)
my_screen.onkey(key="s", fun=move_backwards)
my_screen.onkey(key="a", fun=turn_left)
my_screen.onkey(key="d", fun=turn_right)
my_screen.onkey(key="c", fun=clear)

my_screen.exitonclick()
