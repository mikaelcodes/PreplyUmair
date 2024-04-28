import turtle as t
class spiralturtle(t.Turtle):
    def __init__(self) -> None:
        super().__init__()

t4 = spiralturtle()
for i in range(0,100,5):
    t4.circle(i)
    t4.left(10)
    t4.right(10)
    t4.forward(i+i)
t.mainloop()


 
