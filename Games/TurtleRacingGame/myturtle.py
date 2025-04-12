import turtle
class MyTurtle(turtle.Turtle):
    def __init__(self, color, shape,position ):
        super().__init__(shape=shape)
        self.color(color)
        self.speed(0)
        self.penup()
        self.goto(position[0], position[1])
        self.shapesize(2,2)
        self.score = 0