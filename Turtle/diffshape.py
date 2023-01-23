from turtle import Turtle, Screen

tommy = Turtle()

#TRIANGLE
tommy.pencolor("blue")
for _ in range(3):
    tommy.forward(100)
    tommy.right(120)

#SQUARE
tommy.pencolor("red")
for _ in range(4):
    tommy.forward(100)
    tommy.right(90)


#PENTAGON
tommy.pencolor("black")
for _ in range(5):
    tommy.forward(100)
    tommy.right(72)


#HEXAGON
tommy.pencolor("blue")
for _ in range(6):
    tommy.forward(100)
    tommy.right(60)

#HEPTAGON
tommy.pencolor("brown")
a = 360/7
for _ in range(7):
    tommy.forward(100)
    tommy.right(a)

#OCTAGON
tommy.pencolor("red")
for _ in range(8):
    tommy.forward(100)
    tommy.right(45)

#NANOGON
tommy.pencolor("black")
for _ in range(9):
    tommy.forward(100)
    tommy.right(40)

#DECAGON
tommy.pencolor("blue")
for _ in range(10):
    tommy.forward(100)
    tommy.right(36)

my_screen = Screen()
my_screen.exitonclick()
