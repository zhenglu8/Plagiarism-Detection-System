from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Plagiarism Detection System")
canvas = Canvas(window, width=600, height=400)
canvas.grid(columnspan=2, rowspan=6)

# Define a clear function to clear all entries


def clear():
    entry1.delete(0, END)
    entry2.delete(0, END)

# Define a login function to move to main page


def login():
    window.destroy()
    import MainPage

# Define a signup function to move to signup page


def signup():
    window.destroy()
    import SignUp


label1 = Label(window, text="Username", font="Raleway")
label1.grid(row=0, column=0)

label2 = Label(window, text="Password", font="Raleway")
label2.grid(row=1, column=0)

username_text = StringVar()
entry1 = Entry(window, textvariable=username_text)
entry1.grid(row=0, column=1)

password_text = StringVar()
entry2 = Entry(window, textvariable=password_text)
entry2.grid(row=1, column=1)

# Login button
button1 = Button(window, text="Login", height=2, width=12,
                 font="Raleway", bg="#20bebe", fg="white", command=login)
button1.grid(row=2, column=0)

# Signup button
button2 = Button(window, text="Signup", height=2, width=12,
                 font="Raleway", bg="#20bebe", fg="white", command=signup)
button2.grid(row=3, column=0)

button3 = Button(window, text="Google Login", height=2, width=12,
                 font="Raleway", bg="#20bebe", fg="white")
button3.grid(row=2, column=1)

button4 = Button(window, text="Facebook Login", height=2, width=12,
                 font="Raleway", bg="#20bebe", fg="white")
button4.grid(row=3, column=1)

# Clear All button
button5 = Button(window, text="Clear All", height=2, width=12,
                 font="Raleway", bg="#20bebe", fg="white", command=clear)
button5.grid(row=4, column=0)

# Exit button
button6 = Button(window, text="Exit", height=2, width=12,
                 font="Raleway", bg="#20bebe", fg="white", command=lambda: window.destroy())
button6.grid(row=4, column=1)


window.mainloop()
