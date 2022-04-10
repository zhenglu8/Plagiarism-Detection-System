from tkinter import *
import pyrelog as pl


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


def signup():
    user = entry0.get()
    password = entry1.get()
    try:
        pl.signup(user, password)
        window.destroy()
        import LogIn
    except:
        # switch with tkinter display of failed login (password under 6 character, existing email)
        print("invalid login information")


def clear():
    entry0.delete(0, END)
    entry1.delete(0, END)


def back():
    window.destroy()
    import LogIn


background_img = PhotoImage(file=f"SignupImages/background.png")
background = canvas.create_image(
    323.5, 232.0,
    image=background_img)

entry0_img = PhotoImage(file=f"SignupImages/img_textBox0.png")
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

entry1_img = PhotoImage(file=f"SignupImages/img_textBox1.png")
entry1_bg = canvas.create_image(
    564.0, 253.5,
    image=entry1_img)

entry1 = Entry(
    bd=0,
    bg="#dadada",
    highlightthickness=0)
entry1.insert(0, 'Six Characters Minimal')
entry1.place(
    x=464.5, y=235,
    width=199.0,
    height=35)


def on_click(event):
    entry1.configure(state=NORMAL)
    entry1.delete(0, END)

    # make the callback only work once
    entry1.unbind('<Button-1>', on_click_id)


on_click_id = entry1.bind('<Button-1>', on_click)

img0 = PhotoImage(file=f"SignupImages/img0.png")
b0 = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=signup,
    relief="flat")

b0.place(
    x=446, y=305,
    width=106,
    height=41)

img1 = PhotoImage(file=f"SignupImages/img1.png")
b1 = Button(
    image=img1,
    borderwidth=0,
    highlightthickness=0,
    command=clear,
    relief="flat")

b1.place(
    x=446, y=367,
    width=106,
    height=41)

img2 = PhotoImage(file=f"SignupImages/img2.png")
b2 = Button(
    image=img2,
    borderwidth=0,
    highlightthickness=0,
    command=back,
    relief="flat")

b2.place(
    x=585, y=305,
    width=106,
    height=41)

img3 = PhotoImage(file=f"SignupImages/img3.png")
b3 = Button(
    image=img3,
    borderwidth=0,
    highlightthickness=0,
    command=window.destroy,
    relief="flat")

b3.place(
    x=585, y=367,
    width=106,
    height=41)

window.resizable(False, False)
window.mainloop()
