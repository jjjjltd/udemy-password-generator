from tkinter import *
from tkinter import messagebox

window = Tk()
window.config(padx=50, pady=50, width=200, height=200)
label = Label(text="Extremely simple program!!")
label.pack()

messagebox.askokcancel("Demo","Just a demo message.  Understood?")

window.mainloop()