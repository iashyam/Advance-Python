import random
import turtle

turtle.showturtle()
turtle.pensize(3)
turtle.speed(1)
turtle.pendown()
#giving starting position 
x = 0
y = 0
step = 20
#nuber of steps
numberOfSteps = 80

visited = {(0,0)}
i=0
while i < numberOfSteps:
    steps = [(step,0),(-step,0),(0,1*step),(0,-1*step)]
    dx, dy = random.choice(steps)
    x += dx
    y += dy
    # if (x,y) in visited:
    #     continue
    # else:
    turtle.goto(x,y)
    visited.add((x,y))
    i+=1

turtle.done()
