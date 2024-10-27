from turtle import Turtle
with open("data.txt") as file:
    data = int(file.read())


ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = data
        self.pencolor("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.draw_scoreboard()

    def draw_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def refresh_score(self):
        self.score +=1
        self.draw_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", mode="w") as file:
                file.write(str(self.score))
            self.high_score = self.score
        self.score = 0
        self.draw_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)