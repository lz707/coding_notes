import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.level = 1
        self.segments = []
        self.add_car()

    def create_traffic(self):
        self.add_car()
        distance = STARTING_MOVE_DISTANCE + MOVE_INCREMENT*(self.level-1)
        for seg in self.segments:
            seg.forward(distance)

    def add_car(self):
        random_chance = random.randint(0, 6)
        if random_chance == 6:
            car = Turtle()
            car.shape("square")
            car.shapesize(stretch_len=2)
            car.color(random.choice(COLORS))
            car.penup()
            car.setheading(180)
            car.goto((300, random.randint(-280, 280)))
            self.segments.append(car)






