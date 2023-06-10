from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        # self.shapesize(stretch_len=1.2, stretch_wid=1.2)
        self.x_pos = 0
        self.y_pos = 0

    def move_ball(self):
        for i in range(2):
            self.x_pos += 10
            self.y_pos += 10
            self.goto(self.x_pos, self.y_pos)
