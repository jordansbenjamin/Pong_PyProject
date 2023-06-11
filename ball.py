from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_pos = 10
        self.y_pos = 10

    def move_ball(self):
        x = self.xcor() + self.x_pos
        y = self.ycor() + self.y_pos
        self.goto(x,y)
    
    def bounce(self):
        self.y_pos *= -1

    
