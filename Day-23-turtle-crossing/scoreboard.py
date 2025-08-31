from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 10, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.level = 1
        self.show_level()


    def show_level(self):
        self.clear()
        self.write(f"Level {self.level}-------------------Finish Line--------------------------", align=ALIGNMENT,
                   font=FONT)

    def level_up(self):
        self.level += 1

    def win(self):
        self.goto(0, 0)
        self.write("YOU WIN", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
