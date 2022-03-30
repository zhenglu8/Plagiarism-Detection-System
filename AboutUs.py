from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

window = Tk()
window.title("Plagiarism Detection System")
canvas = Canvas(window, width=600, height=300)
canvas.grid(columnspan=1, rowspan=4)


def back():
    window.destroy()
    import LogIn


label1 = Label(window, text="Plagiarism Detection System",
               font=("Raleway", 25))
label1.grid(row=0, column=0)

label2 = Label(window, text="Feedback", font="Raleway")
label2.grid(row=1, column=0)

st = ScrolledText(window, width=50, height=10)
st.grid(row=2, column=0)

# Submit button
button1 = Button(window, text="Submit", height=2, width=12,
                 font="Raleway", bg="#20bebe", fg="white")
button1.grid(row=3, column=0)

# Exit button
button2 = Button(window, text="Back", height=2, width=12,
                 font="Raleway", bg="#20bebe", fg="white", command=back)
button2.grid(row=4, column=0)


window.mainloop()
