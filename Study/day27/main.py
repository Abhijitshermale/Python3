from tkinter import *

window = Tk()
window.title("My First Gui Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

my_label = Label(text="hi", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)

my_label.config(text="New Text")

def button_clicked():
    print("I got clicked")
    my_label["text"]=input.get()


button = Button(text="Click me", command=button_clicked)
button.grid(column=1,row=1)

button2 = Button(text="New Button")
button2.grid(column=1,row=1)


input = Entry(width=10)
input.grid(column=3, row=2)

mainloop()
