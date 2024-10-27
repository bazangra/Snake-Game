import time
from turtle import Screen, Turtle

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

squares = []

for each in range(0, 3):
    new_square = Turtle("square")
    new_square.penup()
    new_square.color("white")
    new_square.goto(x=(-20*(each)), y=0)
    squares.append(new_square)

is_on = True

while is_on:
    screen.update()
    time.sleep(0.1)
    for square_number in range(len(squares)-1, 0, -1):
        new_x = squares[square_number - 1].xcor()
        new_y = squares[square_number - 1].ycor()
        squares[square_number].goto(new_x, new_y)
    squares[0].forward(20)

screen.exitonclick()