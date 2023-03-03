# Guess-the-States
You can do this game to any country u like just change the image of map
and x, y coordinates according to width of the screen and where the state is located on the screen by help of code below on main.py and put the data in 50_state.csv:


import turtle

def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()

