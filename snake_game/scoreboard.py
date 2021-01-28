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
        self.high_score = 0
        with open('data.txt') as file:
            self.high_score = int(file.read())
        self.update_board()

    def update_board(self):
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        if self.score >= self.high_score:
            self.high_score = self.score
        self.clear()
        self.update_board()

    def game_over(self):
        self.setpos(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)
        with open("data.txt", mode="w") as file:
            file.write(str(self.high_score))
