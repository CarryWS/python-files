import turtle
import random
colors = ['black','green','red','blue','yellow','brown','gray']
p = turtle.Turtle()
p.speed('fastest')
for i in range(2000):
    p.fd(i)
    p.pencolor(random.choice(colors))
    p.right(91)
