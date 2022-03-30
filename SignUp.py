from tkinter import *
from tkinter import ttk
import pyrelog as pl

window = Tk()
window.title("Plagiarism Detection System")
canvas = Canvas(window, width=600, height=300)
canvas.grid(columnspan=2, rowspan=4)

# Define a new function to move to login page


def signup():
    user = entry1.get()
    password = entry2.get()
    try:
        pl.signup(user, password)
        window.destroy()
        import LogIn
    except:
        # switch with tkinter display of failed login (password under 6 character, existing email)
        print("invalid login information")


def clear():
    entry1.delete(0, END)
    entry2.delete(0, END)


def back():
    window.destroy()
    import LogIn


label1 = Label(window, text="Username", font=("Raleway", 15))
label1.grid(row=0, column=0)

label2 = Label(window, text="Password", font=("Raleway", 15))
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
button2 = Button(window, text="Back", height=2, width=12,
                 font="Raleway", bg="#20bebe", fg="white", command=back)
button2.grid(row=2, column=1)

# Exit button
button3 = Button(window, text="Clear All", height=2, width=12,
                 font="Raleway", bg="#20bebe", fg="white", command=clear)
button3.grid(row=3, column=0)

# Exit button
button4 = Button(window, text="Exit", height=2, width=12,
                 font="Raleway", bg="#20bebe", fg="white", command=lambda: window.destroy())
button4.grid(row=3, column=1)


window.mainloop()
