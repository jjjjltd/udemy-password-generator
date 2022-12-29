from tkinter import *
from tkinter import messagebox
from os.path import dirname, join
from turtle import bgcolor
import csv
from pyperclip import copy, paste

# Dumb hard coding just to expedite training exercise!!
EMAIL = "john.joyce90@hotmail.co.uk"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#  Add password
def add_pw():
    print("Add password")
    with open("passwords.csv", "a") as pw_file:
        pw_file.write(f"{w_entry.get()},{e_entry.get()},{pw_entry.get()}\n")

    w_entry.delete(0, END)
    pw_entry.delete(0, END)
    
    # There are lots of other messagebox options - which I don't need to explore for learning purposes.
    messagebox.showinfo("Add Complete", f"Data has been added to: {pw_file.name}")
# ---------------------------- SAVE PASSWORD ------------------------------- #
from random import choice, randint, shuffle

#Password Generator Project
def gen_pw():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    copy(password)
    messagebox.showinfo("Success", "Password successfully generated, but not shown.")
    pw_entry.insert(0, paste())    
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")

current_dir = dirname(__file__)
file_path = join(current_dir, "logo.png")

canvas = Canvas(width=300, height=300, bg="white", highlightcolor="black")

lock_img = PhotoImage(file=file_path)
canvas.create_image(150, 150, image=lock_img)
canvas.grid(column=1, row=0, columnspan=2)

#  Website
w_label = Label(text="Website:", fg="black")
w_label.grid(column=0, row=1)

w_entry = Entry(width=45)
w_entry.grid(column=1, row=1, columnspan=2)
w_entry.focus()

#EMail/Username
e_label = Label(text="EMail/Username:", fg="black")
e_label.grid(column=0, row=2)

e_entry = Entry(width=45)
e_entry.grid(column=1, row=2, columnspan=2)
e_entry.insert(0, EMAIL )
# Password
pw_label = Label(text="Password:", fg="black")
pw_label.grid(column=0, row=3)

pw_entry = Entry(width=21)
pw_entry.grid(column=1, row=3)

pw_button = Button(text="Generate Password", command=gen_pw)
pw_button.grid(column=2, row=3)


add_button = Button(text="Add", command=add_pw, width=40)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()