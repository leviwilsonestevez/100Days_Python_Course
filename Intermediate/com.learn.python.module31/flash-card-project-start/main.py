import random
from tkinter import Tk, Canvas, PhotoImage, Button, messagebox

import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    print(original_data)
    words_pair = original_data.to_dict(orient="records")
else:
    words_pair = data.to_dict(orient="records")
current_card = {}


# ---------------------------- NEXT CARD ------------------------------- #
def next_card() -> None:
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_pair)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    window.after(3000, func=flip_card)


# ---------------------------- FLIP CARD ------------------------------- #
def flip_card() -> None:
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


# ---------------------------- FLIP CARD ------------------------------- #
def is_known_word_pair() -> None:
    to_learn.remove(current_card)
    print(len(to_learn))
    data_updated = pd.DataFrame(to_learn)
    data_updated.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)
canvas = Canvas(width=800, height=526)
card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 250, text="", font=("Ariel", 60, "bold"))

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, borderwidth=0, command=next_card)
unknown_button.grid(row=1, column=0)
unknown_button.config(padx=50, pady=0)
check_image = PhotoImage(file="images/right.png")
check_button = Button(image=check_image, highlightthickness=0, borderwidth=0, command=is_known_word_pair)

check_button.grid(row=1, column=1)
next_card()

window.mainloop()
