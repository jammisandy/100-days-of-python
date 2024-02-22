import turtle as t
import random

tim = t.Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_of_sides):
    angle = 360 / num_of_sides
    for _ in range(num_of_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side in range(3, 10):
    tim.color(random.choice(colours))
    draw_shape(shape_side)










# from turtle import Turtle, Screen

# tim = Turtle()
# tim.shape("turtle")
# tim.color("red")
# # tim.forward(100)
# # tim.right(90)

# i = 3
# while True:

#   def cal_length():
#       n = int(360 / i)
#       return n

#   x = cal_length()
#   print(x)

#   for _ in range(0,i):
#      tim.forward(100)
#      tim.right(x)

#   i = i+1




# screen = Screen()
# screen.exitonclick()