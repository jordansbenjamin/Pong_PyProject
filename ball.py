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
    
    def bounce_y(self):
        self.y_pos *= -1

    def bounce_x(self):
        self.x_pos *= -1
    
    def reset(self):
        self.goto(0,0)
        self.bounce_x()