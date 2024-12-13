from turtle import Turtle
import random
import turtle as t
#colors to avoid caz of black screen
dark_colors = [
    (0, 0, 0),           # Black
    (169, 169, 169),      # Dark Gray
    (105, 105, 105),      # Dim Gray
    (52, 52, 52),         # Jet Black
    (53, 56, 57),         # Onyx
    (54, 69, 79),         # Charcoal
    (65, 74, 76)          # Outer Space
]

t.colormode(255)
def color():
    r = random.randint(1,255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    if (r,g,b) in dark_colors:
        return color()
    else:
        return r,g,b

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len= 1,stretch_wid=1)
        self.color(color())
        self.speed(0)
        x = random.randint(-380 ,380)
        y = random.randint(-280,280)
        self.goto(x,y)
        self.new()

    def new(self):
        x = random.randint(-380, 380)
        y = random.randint(-280, 280)
        self.goto(x, y)
        self.color(color())

