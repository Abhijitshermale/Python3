from tkinter import *

window = Tk()
window.title("Mile To KM Converter")
# window.minsize(width=300, height=200)
window.config(padx=20, pady=20)

text = Entry(width=7, font=("Arial", 12, "bold"))
text.grid(column=1, row=0)


label1 = Label(text="Miles", font=("Arial", 12, "bold"))
label1.grid(column=2,row=0)

label2 = Label(text="is equal to", font=("Arial", 12, "bold"))
label2.grid(column=0, row=1)

label3 = Label(text="", font=("Arial", 12, "bold"))
label3.grid(column=1, row=1)

label4 = Label(text="Km", font=("Arial", 12, "bold"))
label4.grid(column=2, row=1)

def miletokm():
    label3["text"] = round(float(text.get())*1.60934, 2)

button = Button(text="calculate", command=miletokm, font=("Arial", 12, "bold"))
button.grid(column=1, row=2)



window.mainloop()