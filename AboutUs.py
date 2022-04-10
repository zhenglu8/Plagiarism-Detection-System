from tkinter import *


def back():
    window.destroy()
    import LogIn
    # login.aboutus()


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

background_img = PhotoImage(file=f"AboutusImages/background.png")
background = canvas.create_image(
    369.5, 232.0,
    image=background_img)

img0 = PhotoImage(file=f"AboutusImages/img0.png")
b0 = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=back,
    relief="flat")

b0.place(
    x=443, y=331,
    width=106,
    height=41)

img1 = PhotoImage(file=f"AboutusImages/img1.png")
b1 = Button(
    image=img1,
    borderwidth=0,
    highlightthickness=0,
    command=back,
    relief="flat")

b1.place(
    x=583, y=331,
    width=106,
    height=41)

entry0_img = PhotoImage(file=f"AboutusImages/img_textBox0.png")
entry0_bg = canvas.create_image(
    562.5, 211.5,
    image=entry0_img)

entry0 = Entry(
    bd=0,
    bg="#dadada",
    highlightthickness=0)

entry0.place(
    x=396, y=102,
    width=333,
    height=217)

window.resizable(False, False)
window.mainloop()
