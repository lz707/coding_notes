from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))
ball = Ball()
score_board = ScoreBoard()
screen.listen()
screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")
screen.onkey(paddle2.up, "w")
screen.onkey(paddle2.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Hit wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # Hit paddle
    if ball.xcor() > 320 and ball.distance(paddle1) < 50 or ball.xcor() < -330 and ball.distance(paddle2) < 50:
        ball.hit()
        ball.speed_up()

    # paddle miss
    if ball.xcor() > 380:
        ball.restart()
        score_board.left_score()

    if ball.xcor() < -380:
        ball.restart()
        score_board.right_score()































screen.exitonclick()