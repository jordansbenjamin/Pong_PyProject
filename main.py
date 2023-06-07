from turtle import Screen
from paddle import Paddle

screen = Screen()

screen.setup(width=800,height=600)
screen.bgcolor('black')
screen.title('Pong')

paddle = Paddle()
screen.listen()

screen.onkey(fun=paddle.moveup, key='Up')
screen.onkey(fun=paddle.movedown, key='Down')

screen.exitonclick()