import turtle
from myturtle import MyTurtle
t1 = MyTurtle('blue', 'turtle', position=[-400,0])
t1.pendown()
def forward():
    t1.forward(50)  

def backward():
    t1.backward(50) 


def left(): 
    t1.left(1) 

def right():    
    t1.right(1)


turtle.listen()

turtle.onkey(forward, 'Up')
turtle.onkey(backward,'Down')
turtle.onkey(left, 'Left')  
turtle.onkey(right, 'Right')



turtles = []
for i in range(5):
    t = MyTurtle('red', 'turtle', position=[i*100,0])
    t.pendown()
    turtles.append(t)

t1_pos = t1.xcor(), t1.ycor()
while(True):
    # each tuetl follow t1
    if t1_pos[0] != t1.xcor() or t1_pos[1] != t1.ycor():
        others = 0
        for t in turtles:
            t.setposition(t1.xcor()-other, t1.ycor()-other)
            other = other - 50
    



turtle.done()
turtle.mainloop()