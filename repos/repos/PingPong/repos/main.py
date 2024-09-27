import os
from tkinter import *
import turtle as t
import time
from turtle import *
import random


win = t.Screen()
win.title("Pong")
win.setup(width=800, height=600)
win.tracer(1)

def drag_turtle(x,y):
    if x > 0:
        if y < 250 and y > -250:
            paddle_a.teleport(350,y)
    if x < 0:
        if y < 250 and y > -250:
            paddle_b.teleport(-350,y)

# Score A
score_a = Turtle()
score_a.shape

# Paddle A

paddle_a = Turtle()
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5,stretch_len=0.8)
paddle_a.teleport(350,0)
paddle_a.ondrag(drag_turtle)

# Paddle B

paddle_b = Turtle()
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5,stretch_len=0.8)
paddle_b.teleport(-350,0)
paddle_b.ondrag(drag_turtle)
paddle_b.onrelease(drag_turtle)

# Ball

ball = Turtle()
ball.penup()
ball.speed(40)
ball.shape("circle")
ball.teleport(0,0)
ball.dx = 3 # Ball movement in x direction
ball.dy = -3 # Ball movement in y direction


async def ball_movement():
    while True:

        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border collision (top and bottom)
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        # Ball goes out of bounds (left and right)
        if ball.xcor() < -390:
            ball.goto(0,0)
            ball.dx *= -1

        if ball.xcor() > 390:
            ball.goto(0,0)
            ball.dx *= -1

        # Paddle collision
        if ball.dx > 0 and ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
            ball.setx(340)
            ball.dx *= -1

        if ball.dx < 0 and ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
            ball.setx(-340)
            ball.dx *= -1

        await win.ontimer(ball_movement, 20)

ball_movement()


# Start the mainloop
win.mainloop()