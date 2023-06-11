from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.x_pos = x_pos
        self.y_pos = y_pos
        # self.hideturtle()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_len=5)
        self.tiltangle(90)
        self.penup()
        self.goto(x=self.x_pos, y=self.y_pos)
        # self.showturtle()
    
    def moveup(self):
        self.y_pos += 40
        self.goto(x=self.x_pos, y=self.y_pos)

    def movedown(self):
        self.y_pos -= 40
        self.goto(x=self.x_pos, y=self.y_pos)