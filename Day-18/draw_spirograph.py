import turtle as t
import random
from turtle import Screen

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = [r, g, b]
    return color


tim.speed("fastest")

def spirograph(gap_size):
  for _ in range(int(360/gap_size)):
     tim.color(random_color())
     tim.circle(100)
     tim.setheading(tim.heading() + gap_size)


spirograph(5)


screen = Screen()
screen.exitonclick()