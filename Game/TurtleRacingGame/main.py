import turtle
from random import randint
import random
from myturtle import MyTurtle

colors = ["red", "green", "blue", "purple",]
positions = [-250,-200, -150,-100,-50,0,50,100,150,200,250]

turtle.tracer(0)
mikales = []
for pos in positions:
    t1 = MyTurtle(random.choice(colors),'turtle',[-400,pos])
    mikales.append(t1)

x = 'abc'
while True:
    for t1 in mikales:
        t1.forward(randint(1,5))
        if t1.xcor()>450:
            x = 'stop'
            t1.write('I WON')
    if x == 'stop':
        break

    turtle.update()

for each in mikales:
    each.write(str(each.xcor()))

for each in mikales:
    each.forward(50)
turtle.update()
turtle.done()