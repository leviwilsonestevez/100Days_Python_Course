from tkinter import Tk, Label, Button, Entry, Frame, StringVar

# Creating a new window and configurations
window = Tk()
window.title("Widget Examples Simple Implementation For Tkinter")
window.minsize(width=400, height=100)
window.config(padx=20, pady=20)


class MilesEntry(Entry):
    def __init__(self, master=None, **kwargs):
        self.var = StringVar()
        Entry.__init__(self, master, textvariable=self.var, **kwargs)
        self.old_value = ''
        self.var.trace('w', self.check)
        self.get, self.set = self.var.get, self.var.set

    def check(self, *args):
        if self.get().isdigit():
            # the current value is only digits; allow this
            self.old_value = self.get()
        else:
            # there's non-digit characters in the input; reject this
            self.set(self.old_value)


# demo:

miles = MilesEntry(window, width=25)
miles.grid(row=0, column=1)
miles_text = Label(text="Miles")
miles_text.grid(row=0, column=2)
equal_text = Label(text="is equal to")
equal_text.grid(row=1, column=0)
kilometer_text = Label(text="")
kilometer_text.grid(row=1, column=1)
km = Label(text="Km")
km.grid(row=1, column=2)


def convert() -> None:
    kilometer_text.config(text=round(float(int(miles.get()) * 1.60934), 4))


# Button
button = Button(text="Calculate", command=convert)
button.grid(row=2, column=2)
window.mainloop()
