from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.setpos(0, 275)
        self.hideturtle()
        self.color("white")
        self.penup()
        self.update_board()

    def update_board(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.update_board()

    def game_over(self):
        self.setpos(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)
