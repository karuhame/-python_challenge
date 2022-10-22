from turtle import Turtle
import os

os.chdir(r'G:\bachkhoa\-python_challenge\100 days of code\days20')
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as data:         
            self.highest_score = int(data.read())
        self.color("white")
        self.penup ()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}. High score: {self.highest_score} ", align=ALIGNMENT, font=FONT)
    def increase_score(self):
        self.score += 1
        self.clear()
    def reset(self):
        if(self.score> self.highest_score): 
            self.highest_score = self.score
            with open("data.txt",mode = "w") as data:
                data.write(f"{self.highest_score}")
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
