from turtle import Turtle, Screen
import turtle
import random as r

tom = Turtle()
screen = Screen()

def up():
    tom.forward(20)
def down():
    tom.backward(20)
def left():
    new_heading = tom.heading() +10
    tom.setheading(new_heading)
def right():
    new_heading = tom.heading() -10
    tom.setheading(new_heading)
def clear():
    tom.clear()
    tom.penup()
    tom.home()
    tom.pendown()
screen.onkey (up, "w")
screen.onkey (down, "s")
screen.onkey (left, "a")
screen.onkey(right, "d")
screen.onkey(clear, "c")

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70,-40,-10,20,50,80]
turtle_list = []
for turtle_index in range (0, 6):
    tom = Turtle(shape="turtle")
    tom.color(colors[turtle_index])
    tom.penup()
    tom.goto(x=-230, y=y_positions[turtle_index])
    turtle_list.append(tom)
is_race_on = True
while(is_race_on):
    for turtle in turtle_list:
        if(turtle.xcor()>230):
            is_race_on= False
            winner = turtle.pencolor()
            if(winner == user_bet):
                print("YOU WON !!!")
            else: print("YOU LOSE!!!")
            print(f"The winner is {winner} turtle.")
            break
        step = r.randint(1,10)
        turtle.forward(step)


screen.exitonclick()