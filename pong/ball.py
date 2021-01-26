from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto((0, 0))
        self.setheading(45)
        self.step = 10

    def move(self):
        self.forward(self.step)

    def bounce(self):
        new_direction = 360 - self.heading()
        self.setheading(new_direction)

    def hit(self):
        new_direction = 360 - self.heading() + 180
        self.setheading(new_direction)

    def restart(self):
        self.goto((0,0))
        self.hit()

    def speed_up(self):
        self.step += 5