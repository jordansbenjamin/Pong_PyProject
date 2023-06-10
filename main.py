from turtle import Screen
from paddle import Paddle
from ball import Ball

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
    screen.update()
    # screen.exitonclick()

    # # If paddle coordinate moves
    # if r_paddle.ycor() != 0:
    # # The ball starts moving
    #     while True:
    #         screen.tracer(1)
    #         ball.x_pos += 10
    #         ball.y_pos += 10
    #         ball.goto(ball.x_pos, ball.y_pos)
    #         screen.update()
    #         if ball.xcor() == 50 or ball.ycor() == 50:
    #             break
    # If paddle coordinate moves
    if r_paddle.ycor() != 0:
    # The ball starts moving
        screen.tracer(1)
        ball.move_ball()
        screen.update()

screen.exitonclick()