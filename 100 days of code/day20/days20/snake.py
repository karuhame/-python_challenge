from turtle import Turtle
STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
STEPS = 20
UP = 90
DOWN = 270
RIGHT = 0 
LEFT = 180
class Snake:
    def __init__(self):
         self.segment = []
         self.make_snake()
         self.head = self.segment[0]
         

    def make_snake(self):
        for position in STARTING_POSITION:
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color("yellow")
            new_segment.goto(position)
            self.segment.append(new_segment)
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("yellow")
        new_segment.goto(position)
        self.segment.append(new_segment)
    def extend(self):
        self.add_segment(self.segment[-1].position())
    def move(self):
        for seg_num in range(len(self.segment)-1,0,-1):
            new_x = self.segment[seg_num-1].xcor()
            new_y = self.segment[seg_num-1].ycor()
            self.segment[seg_num].goto(new_x,new_y)
        self.segment[0].forward(STEPS)
    def up(self):
        if(self.head.heading() !=DOWN):
            self.head.setheading(UP)
    def down(self):
        if(self.head.heading() !=UP):
            self.head.setheading(DOWN)
    def left(self):

        if(self.head.heading() !=RIGHT):
            self.head.setheading(LEFT)
    def right(self):
        
        if(self.head.heading() !=LEFT):
            self.head.setheading(RIGHT)
    def reset(self):
        for snake_split in self.segment:
            snake_split.goto(1000,1000)
        self.segment.clear()
        self.make_snake()
        self.head = self.segment[0]
    
    