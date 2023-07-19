from tkinter import Tk, Label, Button, Entry

# Creating a new window and configurations
window = Tk()
window.title("Widget Examples Simple Implementation For Tkinter")
window.minsize(width=400, height=100)
window.config(padx=30, pady=30)
# Label Widget
label = Label(text="This is old text")
label.grid(row=0, column=0)
# Buttons
button1 = Button(text="New Button")
button1.grid(row=0, column=2)
button2 = Button(text="Button")
button2.grid(row=1, column=1)
# Entries
entry = Entry(width=30, text="entry")
entry.grid(row=2, column=3)
window.mainloop()
