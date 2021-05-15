import turtle as t
import random as r
t.penup()
t.goto(0,800)
colors = ['green','red','purple','pink','blue','gold','black','white','yellow','orange']
t.left(90)
while True:
    t.color(r.choice(colors))
    t.write('Hello world!')
    t.forward(1)
