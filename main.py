from turtle import Screen
from paddle import Paddle

screen = Screen()

screen.setup(width=800,height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

paddle = Paddle()
screen.listen()

screen.onkeypress(fun=paddle.moveup, key='Up')
screen.onkeypress(fun=paddle.movedown, key='Down')

game_is_on = True

while game_is_on:
    screen.update()
    screen.exitonclick()