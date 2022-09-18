import turtle
import winsound

# Create and setup window
win = turtle.Screen()
win.title('Pong by Phil Drysdale')
win.bgcolor('black')
win.setup(width=800, height=600)
win.tracer(0)

# Score variables
score_a = 0
score_b = 0

# Pen for score
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: {} | Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0,0)
# movement
ball.dx = 0.1
ball.dy = 0.1

# Functions
## Paddle A moving
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20 
    # check if hitting edge
    if paddle_a.ycor() <= 240:
        paddle_a.sety(y)
    else:
        pass
    
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20 
    # check if hitting edge
    if paddle_a.ycor() >= -220:
        paddle_a.sety(y)
    else:
        pass
## Paddle B moving
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20 
    # check if hitting edge
    if paddle_b.ycor() <= 240:
        paddle_b.sety(y)
    else:
        pass
    
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20 
    # check if hitting edge
    if paddle_b.ycor() >= -220:
        paddle_b.sety(y)
    else:
        pass

# Keyboard binding
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    win.update()

#move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

#border checking
# top border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("C:/Users/Phil/Documents/software/Python Playground/pong/bounce.wav", winsound.SND_ASYNC)
# bottom border
    if ball.ycor() < -290:    
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("C:/Users/Phil/Documents/software/Python Playground/pong/bounce.wav", winsound.SND_ASYNC)
 
# right border
    if ball.xcor() > 390:
        ball.goto(0, 0)
        score_a += 1
        pen.clear()
        pen.write("Player A: {} | Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.dx *= -1
# left border
    if ball.xcor() < -390:
        ball.goto(0, 0)
        score_b += 1
        pen.clear()
        pen.write("Player A: {} | Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.dx *= -1

# paddle collision detection
# right collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor()+50 and ball.ycor() > paddle_b.ycor()-50):
        ball.setx(340)
        winsound.PlaySound("C:/Users/Phil/Documents/software/Python Playground/pong/bounce.wav", winsound.SND_ASYNC)
        ball.dx *= -1.02

# left collision
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor()+50 and ball.ycor() > paddle_a.ycor()-50):
        ball.setx(-340)
        winsound.PlaySound("C:/Users/Phil/Documents/software/Python Playground/pong/bounce.wav", winsound.SND_ASYNC)
        ball.dx *= -1.02