from turtle import Turtle,Screen
from duck import Duck
from car import Car
from scoreboard import ScoreBoard
import turtle as t
import time

t.colormode(255)
screen = Screen()
screen.setup(width=600, height=600)


screen.tracer(0)
duck = Duck()
car = Car()
score_board = ScoreBoard()

screen.listen()
screen.onkey(duck.go_up, "w")
is_on = True
while is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()
    for every_car in car.all_cars:
        if(every_car.distance(duck)<20):
            score_board.game_over()
            is_on = False
            
    
    if duck.finish():
        score_board.update()
        duck.start()
        car.level_up()

    





screen.exitonclick()