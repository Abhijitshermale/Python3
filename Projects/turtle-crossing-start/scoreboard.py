from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super(Scoreboard, self).__init__()
        self.hideturtle()
        self.penup()
        self.score=1
        self.goto(-280, 260)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score}", align="left", font=FONT)

    def increase_level(self):
        self.score += 1
        self.update_scoreboard()

    def gameOver(self):
        self.goto(0,0)
        self.write(f"Game Over", align="center", font=("Courier", 40, "bold"))

