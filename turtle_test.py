import turtle as t
import random as r
t.bgcolor('black')
t.penup()
t.speed('fastest')
t.goto(-475,300)
colors = ['green','red','purple','pink','blue','gold','black','white','yellow','orange']
while True:
    for i in range(150):
        t.write('Hello world!',font=('Arial', 20, 'normal'))
        t.color(r.choice(colors))
        t.forward(5)
        t.pensize(r.randint(1,100))
    t.right(90)
