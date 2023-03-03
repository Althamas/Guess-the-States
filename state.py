from turtle import Turtle, Screen

screen = Screen()


class State(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("Black")
        self.penup()

    def place(self, x, y, state):
        self.goto(x, y)
        self.write(state, False, "Center", ("Courier", 12, "normal"))
