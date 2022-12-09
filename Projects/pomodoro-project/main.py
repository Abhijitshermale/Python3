from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK= "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
BLUE = "#0366fc"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label1.config(text="Timer", fg=GREEN)
    label2.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():

    global reps
    reps += 1
    WORK_MIN_SEC = WORK_MIN * 60
    SHORT_BREAK_MIN_SEC = SHORT_BREAK_MIN * 60
    LONG_BREAK_MIN_SEC = LONG_BREAK_MIN * 60

    if reps % 2 != 0:
        count_down(WORK_MIN_SEC)
        label1.config(text="Work Time", fg=RED)
    elif reps == 8:
        count_down(LONG_BREAK_MIN_SEC)
        label1.config(text="Long Break" ,fg=GREEN)
    else:
        count_down(SHORT_BREAK_MIN_SEC)
        label1.config(text="Short Break", fg=BLUE)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = "0" + str(count_sec)

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if(count > 0):
        global timer
        timer = window.after(1000, count_down, count -1)
    else:
        start_timer()
        mark= ""
        work_session = math.floor(reps/2)
        for i in range(work_session):
            mark += " ✔"
        label2.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodora")
window.config(padx=100, pady=50, bg=YELLOW)

label1 = Label(text="Timer", font=("Arial", 35, "bold"), bg=YELLOW, fg=GREEN)
label1.grid(column=1, row=0)




canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text=canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


label2 = Label(text="", font=("Arial", 20, "bold"))
label2.grid(column=1, row=3)
label2.config(bg=YELLOW,fg=GREEN)

button1 = Button(text="Start", command=start_timer, font=("Arial", 20, "bold"), highlightthickness=0)
button1.grid(column=0, row=2)

button2 = Button(text="Reset", font=("Arial", 20, "bold"), highlightthickness=0, command=reset_timer)
button2.grid(column=2, row=2)

window.mainloop()