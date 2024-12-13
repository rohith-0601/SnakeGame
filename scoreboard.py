from turtle import Screen,Turtle


class Scoreboard:
    def __init__(self,screen):
        self.screen = screen
        self.score =0
        self.update_score()
        self.game_over_snake = Turtle()
        self.game_over_snake.hideturtle()
        self.game_over_snake.penup()
        self.game_over_snake.color("white")

    def update_score(self):
        self.screen.title(f"Snake Game, Score: {self.score}")

    def game_over(self):
        self.game_over_snake.goto(0,0)
        self.game_over_snake.write(f"GAME OVER\nYour Score :{self.score}", align="center", font=('Arial', 24, 'normal'))



