import turtle as t
import random
t_1 = t.Turtle()
t_2 = t.Turtle()

t_2.color('red')
t_1.color('blue')
t_1.forward(100)
t_2.backward(100)
t.speed("fastest")
lst = []
for i in range(100):
    lst.append(t.Turtle())
r = 10
colors = ['red','blue','green','pink','orange','purple','yellow']
for each in lst:
    each.speed('fastest')
    each.forward(100)
    each.left(90)
    each.circle(r)
    each.color(random.choice(colors))

    r +=2

t.mainloop()