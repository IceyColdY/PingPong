import os
from re import X
from tkinter import *
import turtle as t
import time
from turtle import *
import turtle
import random


win = turtle.Screen()
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
ball.speed(40)
ball.shape("circle")
ball.penup()
ball.goto(0,0)
ball.dx = 0.2 # Ball movement in x direction
ball.dy = -0.2 # Ball movement in y direction



while True:
    win.update()