import turtle as t

t.bgcolor('black')

colors = ['red','blue','green','yellow','orange','salmon','aqua','cyan']

for angle in range(0, 360):
    for i in colors:
        t.color(i)
        t.circle(100)
        t.left(10)
t.penup()

