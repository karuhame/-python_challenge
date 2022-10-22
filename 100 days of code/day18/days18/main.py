from turtle import Turtle, Screen
import turtle as t
import random as r


colours = ["CornflowerBlue", "Darkorchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
tom_turtle = Turtle()
tom_turtle.shape("turtle")
tom_turtle.color("black","red")
tom_turtle.pensize(15)
t.colormode(255)
tom_turtle.speed("fastest")
def ran_color():
    red = r.randint(0,255)
    green = r.randint(0,255)
    blue = r.randint(0,255)
    color = (red,green,blue)
    return color

def square(turtle):
    for i in range(4):
        turtle.right(90)
        turtle.forward(100)
def dashline(turtle, length):
    cnt = 1
    # turtle.forward(length)
    for i in range(0,length,4):
        turtle.forward(4)
        if(cnt):
            turtle.penup()
            cnt-=1
        else: 
            turtle.pendown()
            cnt+=1

def different_shape(turtle, length):

    total_angle = 360
    for num_sides in range(4,10):
        turtle.color(colours[num_sides-4])
        angle = total_angle/num_sides
        for turn in range(num_sides):
            turtle.forward(length)
            turtle.right(angle)

def random_walk(turtle, length, times):
    directions = [0,90,180,270]
    for i in range(times):
        turtle.color(ran_color())
        turtle.forward(length)
        turtle.setheading(r.choice(directions))

def sprirograph(turtle, size, rad,nums):
    turtle.pensize(size)
    for turns in range(nums):
        turtle.color(ran_color())
        turtle.circle(rad)
        turtle.right(360//nums)

# sprirograph(tom_turtle,2,100,50)

# random_walk(tom_turtle, 10, 100)
# different_shape(tom_turtle,100)   
# square(tom_turtle)
# dashline(tom_turtle,100)
screen = Screen()
screen.exitonclick()