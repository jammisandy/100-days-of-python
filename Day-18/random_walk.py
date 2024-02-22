import turtle as t
import random

tim = t.Turtle()

directions = [0, 90, 180, 270]
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
tim.pensize(15)
tim.speed("fastest")


for _ in range(200):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))