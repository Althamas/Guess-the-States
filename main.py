from turtle import Turtle, Screen
from state import State
import pandas

data = pandas.read_csv("50_states.csv")
data_state = data["state"].tolist()
data_x = data["x"].tolist()
data_y = data["y"].tolist()
image = "blank_states_img.gif"
screen = Screen()
t = Turtle()
s = State()
screen.addshape(image)
screen.title("U.S State Game")
t.shape(image)
correct = 0
guessed = []
game_is_on = True
while game_is_on:
    guess = screen.textinput(f"Guessed {correct}:50 States", "Enter your next State").title()
    if guess == "Exit":
        set1 = set(data_state)
        set2 = set(guessed)
        wrong = list(set1.difference(set2))
        data = pandas.DataFrame(wrong)
        data.to_csv("wrong_answer.csv")

    if guess in data_state:
        pos = data_state.index(guess)
        x_cor = data_x[pos]
        y_cor = data_y[pos]
        s.place(x_cor, y_cor, guess)
        correct += 1
        guessed.append(guess)
    else:
        game_is_on = False
        t.write(f"GAME OVER \n Your score is {correct}: 50", False, "Center", ("Courier", 12, "normal"))

screen.mainloop()
