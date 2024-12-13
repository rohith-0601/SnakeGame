from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# screen settings:
screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake Game")

# temporary variables:
game_on = True
# calling snake class by initializing it
snake = Snake()
# calling food class by initializing it
food = Food()
# calling the scoreboard to count
score =  Scoreboard(screen)


# user controls for snake movement
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move() #snake movement

    #verifying whether snake got food or not
    if snake.head.distance(food) < 15:
        food.new()
        snake.extend_body()
        score.score += 1
        score.update_score()

    #collision with wall
    if snake.head.xcor() > 380 or snake.head.xcor() < -380 or snake.head.ycor() >280 or snake.head.ycor() < -280:
        game_on = False
        score.game_over()

    #tail collision
    for body_part in snake.snakebody_list[1:]:
        if snake.head.distance(body_part) < 10:
            game_on = False
            score.game_over()


screen.exitonclick()