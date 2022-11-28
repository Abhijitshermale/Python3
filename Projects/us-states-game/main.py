import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S.States")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
count=0
guess_states = []
while len(guess_states) < 50:
    answer_state = screen.textinput(title=f"{count}/{len(states)} is correct", prompt="What's another state's name ?")
    answer_state = str(answer_state).capitalize()
    if answer_state == "Exit":
        break
    if answer_state in states:
        guess_states.append(answer_state)
        states.remove(answer_state)
        x_cor = int(data.x[data["state"] == answer_state])
        y_cor = int(data.y[data["state"] == answer_state])
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.color("black")
        t.goto(x_cor, y_cor)
        t.write(f"{answer_state}", align="center", font=("Courier", 8, "normal"))
        count+=1

missingState = {
        "Missed States" : states
}
df = pandas.DataFrame(missingState)
df.to_csv("missing_states.csv")




