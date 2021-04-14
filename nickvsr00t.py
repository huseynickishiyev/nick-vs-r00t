import turtle
import random
wn = turtle.Screen()
wn.title =("Snatch by nick")
wn.bgcolor("white")
wn.setup(width=800, height=600)
wn.tracer(0) #Stops window from updating\rn

#Scores Defined;
score_nick = 0
score_r00t = 0

# Paddle.nick
paddle_nick = turtle.Turtle()
paddle_nick.speed(0)
paddle_nick.shape("square")
paddle_nick.shapesize(stretch_wid=5, stretch_len=1)
paddle_nick.color("black")
paddle_nick.penup()
paddle_nick.goto(-350, 0)

# Paddle.r00t
paddle_r00t = turtle.Turtle()
paddle_r00t.speed(0)
paddle_r00t.shape("square")
paddle_r00t.shapesize(stretch_wid=5, stretch_len=1)
paddle_r00t.color("black")
paddle_r00t.penup()
paddle_r00t.goto(350, 0)
paddle_r00t._rotate(180)

# .ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("black")
ball.penup()
ball.goto(0,0)
ball.dx = 0.25 
ball.dy = 0.25

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("nick: 0  r00t: 0", align="center", font=("Courier", 24, "normal"))

#Functions
def paddle_nick_up():
    y = paddle_nick.ycor()
    y += 20
    paddle_nick.sety(y)

def paddle_nick_down():
    y = paddle_nick.ycor()
    y -= 20
    paddle_nick.sety(y)

def paddle_r00t_up():
    y = paddle_r00t.ycor()
    y += 20
    paddle_r00t.sety(y)

def paddle_r00t_down():
    y = paddle_r00t.ycor()
    y -= 20
    paddle_r00t.sety(y)



#Keybind
wn.listen() #tell the game to listen to the keyboard input
wn.onkeypress(paddle_nick_up, "w")
wn.onkeypress(paddle_nick_down, "s")
wn.onkeypress(paddle_r00t_up, "Up")
wn.onkeypress(paddle_r00t_down, "Down")

# Writing loops
while True:
    wn.update()

    # Ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1    

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_nick += 1
        pen.clear()
        pen.write("nick: {}  r00t: {}".format(score_nick, score_r00t), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_r00t += 1
        pen.clear()
        pen.write("nick: {}  r00t: {}".format(score_nick, score_r00t), align="center", font=("Courier", 24, "normal")) 

#Collisions;
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_r00t.ycor() + 40 and ball.ycor() > paddle_r00t.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_nick.ycor() + 40 and ball.ycor() > paddle_nick.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1