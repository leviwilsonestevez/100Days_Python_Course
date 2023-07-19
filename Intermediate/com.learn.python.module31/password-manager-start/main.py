from random import choice, randint, shuffle
from tkinter import Tk, Canvas, PhotoImage, Label, Entry, Button, messagebox

import pyperclip as pyperclip
import json

END = 'end'


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password() -> None:
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_letters = [choice(letters) for _ in range(8, 10)]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save() -> None:
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="No empty fields!")
    else:
        try:
            with open("data.json", "r") as data_file:
                previous_data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(obj=new_data, fp=data_file, indent=4)
        else:
            previous_data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(obj=previous_data, fp=data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password() -> None:
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"Please the field Website is required.")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pasword Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200, highlightthickness=0)
tomato_img = PhotoImage(file="logo.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.grid(column=1)
# Labels
website_label = Label(text="Website")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username")
email_label.grid(column=0, row=2)
password_label = Label(text="Password")
password_label.grid(column=0, row=3)
# Entries
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2, sticky="ew")
email_entry = Entry(width=21)
email_entry.grid(column=1, row=2, columnspan=3, sticky="ew")
email_entry.insert(0, "leviengineer@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, columnspan=3, sticky="ew")
# Buttons
search_button = Button(text="Search", width=15, highlightthickness=0, command=find_password)
search_button.grid(column=3, row=1)
generate_button = Button(text="Generate Password", highlightthickness=0, command=generate_password)
generate_button.grid(column=3, row=3)
add_button = Button(text="Add", width=34, highlightthickness=0, command=save)
add_button.grid(column=1, row=4, columnspan=3, sticky="ew")

window.mainloop()
