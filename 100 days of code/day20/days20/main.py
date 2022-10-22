from re import T
from turtle import  Screen
from days20.score_board import Scoreboard
from food import Food
from snake import Snake
from score_board import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snack Game")
segment = []
screen.tracer(0)


tom = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey (tom.up, "Up")
screen.onkey (tom.down, "Down")
screen.onkey (tom.left, "Left")
screen.onkey(tom.right, "Right")

continue_running = True
while continue_running:
    time.sleep(0.1) 
    screen.update()
    tom.move()
    score.update_scoreboard()
    #detect
    if tom.head.distance(food) <15:
        food.refresh()
        tom.extend()
        score.increase_score()
    if tom.head.xcor() > 280 or tom.head.xcor() < -280 or tom.head.ycor() > 280 or tom.head.ycor () < -280:
        tom.reset()
        score.reset()
    for segment in tom.segment[1:]:
        if(tom.head.distance(segment))<10:    
            tom.reset()
            score.reset()



        
    






screen.exitonclick()