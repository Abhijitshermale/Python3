import turtle
import pandas
t=turtle.Turtle()

screen = turtle.Screen()
screen.title(" India States")
screen.setup(800,800)
image = "India_map.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("india_all_states.csv")
states = data.state.to_list()
count=0
guess_states = []
while len(guess_states) < 29:
    answer_state = screen.textinput(title=f"{count}/{len(states)} is correct", prompt="What's another state's name ?")
    answer_state = str(answer_state).title()
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
        t.write(f"{answer_state}", align="center", font=("Courier", 8, "bold"))
        count+=1

missingState = {
        "Missed States" : states
}
df = pandas.DataFrame(missingState)
df.to_csv("missing_states.csv")



