from turtle import Turtle
import random as r
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"] 
STARTING_MOVE_DISTANCE =5
MOVE_INCREMENT = 10

class Car:
    """ def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("square")
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.speed = 1        
        self.penup()
        
        
    def ran_color(self):
        red = r.randint(0,255)
        green = r.randint(0,255)
        blue = r.randint(0,255)
        self.color(red,green,blue) """
    
    # def create_car(self):
    #     self.ran_color()
    #     y_position = r.randint(-250,250)
    #     self.showturtle()
    #     self.goto(250, y_position)
    #     self.goto(-250,y_position)
    def __init__ (self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
    def create_car(self):
        random_chane = r.randint(1,6)
        if(random_chane == 1):
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=3)
            new_car.penup()
            new_car.color(r.choice (COLORS))
            random_y = r.randint(-12,12)
            new_car.goto(300, random_y*20)
            self.all_cars.append (new_car)
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
    def level_up(self):
        self.car_speed += 10