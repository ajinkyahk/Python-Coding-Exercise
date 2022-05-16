from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def mov_forwards():
    tim.forward(10)

def mov_backwards():
    tim.back(10)


def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def turn_left():
    #new_heading = tim.heading()+10
    #tim.setheading(new_heading)
    tim.left(10)

def clear_drawing():
    tim.reset()

screen.listen()
screen.onkey(mov_forwards, "w")
screen.onkey(mov_backwards, "s")
screen.onkey(turn_left,"a")
screen.onkey(turn_right, "d")
screen.onkey(key="c", fun=clear_drawing)

screen.exitonclick()

