from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 50, "bold")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.update()
        
        
    def update(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score,align= ALIGNMENT,font= FONT)
        self.goto(100,200)
        self.write(self.r_score,align= ALIGNMENT,font= FONT)
    
    def l_point(self):
        self.l_score +=1
        self.update()

    def r_point(self):
        self.r_score += 1
        self.update()