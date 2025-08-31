import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.allcars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        if random.randint(1,6) == 1: #slow down car generating by chance of 1/6
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1.0, stretch_len=2.0)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(300, random.randint(-250, 250))
            new_car.setheading(180)
            self.allcars.append(new_car)

    def move_cars(self):
        for car in self.allcars:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT










