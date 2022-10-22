from turtle import Turtle
MOVE_DISTANCE = 20
STARTING_POINT = (0,-260)
FINISH_LINE = 280
class Duck(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("Black")
        self.setheading(90)
        self.penup()
        self.start()

    def go_up(self):
        self.forward(MOVE_DISTANCE)
    
    def start(self):
        self.goto(STARTING_POINT)


    def finish(self):
        if(self.ycor()> FINISH_LINE):
            return True
        return False

