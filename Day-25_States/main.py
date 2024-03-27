import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. Stated game")
image = "100-days-of-python/Day-25_States/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("100-days-of-python/Day-25_States/50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states correct", prompt="What's another state's name?r").title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_Learn.csv")
        print(new_data)
        break  
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)