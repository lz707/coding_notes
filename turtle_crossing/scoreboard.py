from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto((-280, 250))
        self.level = 1
        self.write(f"Level: {self.level}", align="left", font = FONT)

    def update_board(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font = FONT)

    def game_over(self):
        self.goto((0,0))
        self.write("Game Over", align="center", font=FONT)