from tkinter import *
from tkinter import ttk
import pyrelog as pl
from selenium import webdriver
import webbrowser

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
    user = entry1.get()
    password = entry2.get()
    try:
        pl.login(user, password)
        window.destroy()
        import MainPage
    except:
        # switch with tkinter display of failed login
        print("login failed?")

# Define a signup function to move to signup page


def signup():
    window.destroy()
    import SignUp


def facebook():
    url = 'https://www.facebook.com/'
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

    webbrowser.get(chrome_path).open(url)


def google():
    url = 'https://google.com/'
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

    webbrowser.get(chrome_path).open(url)


def aboutus():
    window.destroy()
    import AboutUs


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

# Login button
button1 = Button(window, text="Login", height=2, width=12,
                 font="Raleway", bg="#20bebe", fg="white", command=login)
button1.grid(row=2, column=0)

# Signup button
button2 = Button(window, text="Signup", height=2, width=12,
                 font="Raleway", bg="#20bebe", fg="white", command=signup)
button2.grid(row=3, column=0)

button3 = Button(window, text="Google Login", height=2, width=12,
                 font="Raleway", bg="#20bebe", fg="white", command=google)
button3.grid(row=2, column=1)

button4 = Button(window, text="Facebook Login", height=2, width=12,
                 font="Raleway", bg="#20bebe", fg="white", command=facebook)
button4.grid(row=3, column=1)

# Clear All button
button5 = Button(window, text="Clear All", height=2, width=12,
                 font="Raleway", bg="#20bebe", fg="white", command=clear)
button5.grid(row=4, column=0)

# About Us button
button7 = Button(window, text="About Us", height=2, width=12,
                 font="Raleway", bg="#20bebe", fg="white", command=aboutus)
button7.grid(row=4, column=1)

# Exit button
button6 = Button(window, text="Exit", height=2, width=12,
                 font="Raleway", bg="#20bebe", fg="white", command=lambda: window.destroy())
button6.grid(row=5, column=0)


window.mainloop()
