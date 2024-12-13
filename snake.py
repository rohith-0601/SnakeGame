from turtle import Turtle

# temporary variable
DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    # creating initial body:
    def __init__(self):
        self.snakebody_list = []
        self.create_snake()
        self.head = self.snakebody_list[0]

    def create_snake(self):
            x = 0 #change x here for starting position
            for i in range(3):
                self.add_body((x,0))
                x -= 20

    def add_body(self,position):
        snake_body = Turtle("square")
        snake_body.penup()
        snake_body.color("white")
        snake_body.goto(position)
        self.snakebody_list.append(snake_body)

    def extend_body(self):
        self.add_body(self.snakebody_list[-1].position())

    def move(self):
        for snakebody_parts in range(len(self.snakebody_list) - 1, 0, -1):
            x = self.snakebody_list[snakebody_parts - 1].xcor()
            y = self.snakebody_list[snakebody_parts - 1].ycor()
            self.snakebody_list[snakebody_parts].goto(x, y)
        self.head.forward(DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading()!= RIGHT:
            self.head.setheading(LEFT)


