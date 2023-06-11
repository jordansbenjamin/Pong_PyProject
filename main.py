from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
import random as rand

screen = Screen()

screen.setup(width=800,height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()

screen.listen()
screen.onkeypress(fun=r_paddle.moveup, key='Up')
screen.onkeypress(fun=r_paddle.movedown, key='Down')
screen.onkeypress(fun=l_paddle.moveup, key='w')
screen.onkeypress(fun=l_paddle.movedown, key='s')

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    # screen.tracer(1)
    screen.update()
    ball.move_ball()

    if ball.ycor() > 280 or ball.ycor() < -280:
        # directions = [-10,10]
        # x = rand.choice(directions)
        # y = rand.choice(directions)
        ball.bounce()

screen.exitonclick()