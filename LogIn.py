from tkinter import *
import pyrelog as pl
import webbrowser


window = Tk()

window.geometry("753x464")
window.configure(bg="#ffffff")
window.title("Plagiarism Detection System")
canvas = Canvas(
    window,
    bg="#ffffff",
    height=464,
    width=753,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)


def clear():
    entry0.delete(0, END)
    entry1.delete(0, END)

# Define a login function to move to main page


def login():
    user = entry0.get()
    password = entry1.get()
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


background_img = PhotoImage(file=f"LoginImages/background.png", master=window)
background = canvas.create_image(
    336.0, 232.0,
    image=background_img)

entry0_img = PhotoImage(file=f"LoginImages/img_textBox0.png", master=window)
entry0_bg = canvas.create_image(
    564.0, 160.5,
    image=entry0_img)

entry0 = Entry(
    bd=0,
    bg="#dadada",
    highlightthickness=0)

entry0.place(
    x=464.5, y=142,
    width=199.0,
    height=35)

entry1_img = PhotoImage(file=f"LoginImages/img_textBox1.png", master=window)
entry1_bg = canvas.create_image(
    564.0, 253.5,
    image=entry1_img)

entry1 = Entry(
    bd=0,
    bg="#dadada",
    highlightthickness=0)

entry1.place(
    x=464.5, y=235,
    width=199.0,
    height=35)

img0 = PhotoImage(file=f"LoginImages/img0.png", master=window)
b0 = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=login,
    relief="flat",
    master=window)

b0.place(
    x=446, y=305,
    width=106,
    height=41)

img1 = PhotoImage(file=f"LoginImages/img1.png", master=window)
b1 = Button(
    image=img1,
    borderwidth=0,
    highlightthickness=0,
    command=google,
    relief="flat",
    master=window)

b1.place(
    x=445, y=351,
    width=106,
    height=41)

img2 = PhotoImage(file=f"LoginImages/img2.png", master=window)
b2 = Button(
    image=img2,
    borderwidth=0,
    highlightthickness=0,
    command=clear,
    relief="flat",
    master=window)

b2.place(
    x=446, y=402,
    width=106,
    height=41)

img3 = PhotoImage(file=f"LoginImages/img3.png", master=window)
b3 = Button(
    image=img3,
    borderwidth=0,
    highlightthickness=0,
    command=signup,
    relief="flat",
    master=window)

b3.place(
    x=585, y=305,
    width=106,
    height=41)

img4 = PhotoImage(file=f"LoginImages/img4.png", master=window)
b4 = Button(
    image=img4,
    borderwidth=0,
    highlightthickness=0,
    command=facebook,
    relief="flat",
    master=window)

b4.place(
    x=585, y=354,
    width=106,
    height=41)

img5 = PhotoImage(file=f"LoginImages/img5.png", master=window)
b5 = Button(
    image=img5,
    borderwidth=0,
    highlightthickness=0,
    command=aboutus,
    relief="flat",
    master=window)

b5.place(
    x=585, y=403,
    width=106,
    height=41)

window.resizable(False, False)
window.mainloop()
