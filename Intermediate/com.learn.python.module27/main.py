from tkinter import Tk, Label, Button, Entry

windows = Tk()

windows.title("My new window in Tkinter")
windows.minsize(width=400, height=400)

label = Label(text="Label", font=("Arial", 12, "bold"))
label.pack(side="top")
label["text"] = "New Text"


# label.configure(text="Using Config Method")
# Button
def button_clicked() -> None:
    label.configure(text=text.get())


button = Button(text="click me!!", command=button_clicked)
button.pack()
text = Entry(width=40)
text.pack()

windows.mainloop()
