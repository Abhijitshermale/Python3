from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle((380, 0))
l_paddle = Paddle((-390, 0))
ball =Ball()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 350 or ball.distance(l_paddle) < 50 and ball.xcor() < -360:
        ball.bounce_x()

    if ball.xcor()>380 :
        ball.bounce_x()
        scoreboard.r_point()
        ball.ball_speed=0.1


    if ball.xcor() <-390:
        ball.bounce_x()
        scoreboard.l_point()
        ball.ball_speed = 0.1

screen.exitonclick()