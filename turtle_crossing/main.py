import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


FINISH_LINE_Y = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score_board = Scoreboard()
screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_traffic()

    if player.ycor() >= FINISH_LINE_Y:
        player.finish()
        car.level += 1
        score_board.level += 1
        score_board.update_board()

    for seg in car.segments:
        if seg.distance(player) < 20:
            score_board.game_over()
            game_is_on = False


screen.exitonclick()