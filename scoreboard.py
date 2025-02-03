from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as file:
            self.high_score = int (file.read())
        self.penup()
        self.pencolor("white")
        self.goto(x=0,y=280)
        self.print_score()
        self.hideturtle()
    def score_increment(self):
        self.score += 1
        self.print_score()
    def print_score(self):
        self.clear()
        self.write(arg=f"Score {self.score} High Score {self.high_score}", align="center", font=("Arial", 14, "normal"))
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(arg="Game Over", align="center", font=("Arial", 14, "normal"))

    def reset(self):
        if self.score > self.high_score:
            with open('data.txt','w') as file:
                self.high_score = self.score
                file.write(f"{self.high_score}")
        self.score = 0
        self.print_score()