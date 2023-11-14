# import required modules
from turtle import Turtle

# GLOBAL VARIABLES
FONT = ("Courier", 12, "normal")

# create Scoreboard class
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 260)
        self.write(arg=f"Score = {self.score} High Score = {self.high_score}", move=False, align="center", font=FONT)

    # method to increase score
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    # method to update scoreboard
    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score = {self.score} High Score: {self.high_score}", move=False, align="center", font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()




#    def game_over(self):
#        self.goto(0, 0)
#        self.write(arg="GAME OVER.", move=False, align="center", font=("Courier", 24, "normal"))
