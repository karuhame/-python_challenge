from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)


r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
score_ball = ScoreBoard()

screen.listen ()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey (r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

shoud_continue = True


while shoud_continue:
    time.sleep(ball.movespeed)    
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    if (ball.distance(r_paddle) < 60 and ball.xcor() > 320) or (ball.distance(l_paddle) < 60 and ball.xcor() < -320):
        ball.bounce_x()
    
    if ball.xcor() > 380:
        ball.reset_position()
        score_ball.l_point()


    if ball.xcor() < -380:
        ball.reset_position()
        score_ball.r_point()





screen.exitonclick()
