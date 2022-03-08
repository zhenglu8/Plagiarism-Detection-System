from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Plagiarism Detection System")
canvas = Canvas(window, width=600, height=300)
canvas.grid(columnspan=2, rowspan=4)

# Define a new function to move to login page


def signup():
    window.destroy()
    import LogIn


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

# Sign up button
button1 = Button(window, text="Signup", height=2, width=12,
                 font="Raleway", bg="#20bebe", fg="white", command=signup)
button1.grid(row=2, column=0)

# Exit button
button2 = Button(window, text="Exit", height=2, width=12,
                 font="Raleway", bg="#20bebe", fg="white", command=lambda: window.destroy())
button2.grid(row=2, column=1)


window.mainloop()
