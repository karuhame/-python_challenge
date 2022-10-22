from turtle import Turtle
ALIGNMENT = "left"
FONT = ("Courier", 15, "bold")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.score = 0
        self.color("black")
        self.penup()
       
        self.goto(-280, 250)
        self.write(f"Level :{self.level}. Score: {self.score}", align=ALIGNMENT, font= FONT)
    def update(self):
        self.level +=1 
        self.score += 1

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!!!", align="center", font= FONT)
        
    