from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.pencolor("white")
        self.goto(x=0,y=280)
        self.print_score(self.score)
        self.hideturtle()
    def score_increment(self):
        self.score += 1
        self.clear()
        self.print_score(self.score)
    def print_score(self,score):
        self.write(arg=f"Score {score}", align="center", font=("Arial", 14, "normal"))
    def game_over(self):
        self.goto(0,0)
        self.write(arg="Game Over", align="center", font=("Arial", 14, "normal"))
