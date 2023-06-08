from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.x_pos = 350
        self.y_pos = 0
        # self.hideturtle()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_len=5)
        self.tiltangle(90)
        self.penup()
        self.goto(x=self.x_pos, y=self.y_pos)
        # self.showturtle()
    
    def moveup(self):
        self.y_pos += 20
        self.goto(x=self.x_pos, y=self.y_pos)

    def movedown(self):
        self.y_pos -= 20
        self.goto(x=self.x_pos, y=self.y_pos)