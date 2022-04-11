from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from tkinter.messagebox import showinfo, showwarning
import pyrelog as pl
import pysimilaralgorithm as pa
import os
import pyrebase
from PIL import Image, ImageTk
from matplotlib import pyplot as plt

firebaseConfig = {
    'apiKey': "AIzaSyAEp8_HarY6xSVZEgiXiko67ntgVuCXmwg",
    'authDomain': "integrationproject-8160f.firebaseapp.com",
    'databaseURL': "https://integrationproject-8160f-default-rtdb.firebaseio.com/",
    'projectId': "integrationproject-8160f",
    'storageBucket': "integrationproject-8160f.appspot.com",
    'messagingSenderId': "1053011153629",
    'appId': "1:1053011153629:web:b1f1c1a15cb213c2f88134",
    'measurementId': "G-9T553ECDE0"
}


firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()
storage = firebase.storage()


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

label1 = Label(window)
label2 = Label(window)

enc = 'utf8'

# Define a function to open the file explrer


def browsefiles():
    '''
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Word files",
                                                      "*.doc*"),
                                                     ("all files",
                                                      "*.*")))
    '''

    file = askopenfile(mode='r', filetypes=[
        ('Txt files', '*.txt'), ('all files', '*.*')])

    if file is not None:
        content = file.read()
        print(content)
        '''
        storage.child(file.name).put(file.name)
        url = storage.child(file.name).get_url(None)
        data = {"url": url}
        db.child("documents").push(data)
        '''
        try:
            with open('docs/selected_file.txt', 'w') as f:
                f.write(content)
        except FileNotFoundError:
            print("The 'docs' directory does not exist")

    showinfo(
        title='Selected File',
        message="The " + file.name + " is successfully selected"
    )

    # Document#1 filename
    label1 = Label(window, text=file.name)
    label1.grid(row=2, column=0)


def upload():
    file = askopenfile(mode='r', filetypes=[
        ('Txt files', '*.txt'), ('all files', '*.*')])

    if file is not None:
        content = file.read()

        storage.child(file.name).put(file.name)
        url = storage.child(file.name).get_url(None)
        data = {"url": url}
        db.child("documents").push(data)

        showinfo(
            title='Uploaded File',
            message="The " + file.name + " is successfully uploaded"
        )


def compare():

    checking = pa.pyrecheck('docs/selected_file.txt', pl.firebaseConfig)

    checking.connect()

    checking.connect_storage()
    checking.connect_database()

    checking.compare_against_files()

    print('result is ' + str(checking.return_results()))

    if checking.return_results() >= 0.75:
        showwarning(
            title='Similarity Score',
            message="The similarity score is " +
            str(round(checking.return_results()*100)) + " %"
        )
    else:
        showinfo(
            title='Similarity Score',
            message="The similarity score is " +
            str(round(checking.return_results()*100)) + " %"
        )


def exit():
    try:
        os.remove("docs/selected_file.txt")
    except Exception as e:
        print(e)

    window.destroy()


def chart():
    '''
    plt.style.use("fivethirtyeight")

    y = [100, 200, 300, 400, 500]
    plt.bar(x, y, color="#444444", label="All Devs")
    plt.legend()

    plt.title("Similarity Score")
    plt.xlabel("Document Names")
    plt.ylabel("Scores")

    plt.tight_layout()
    plt.show()
    '''


background_img = PhotoImage(file=f"MainImages/background.png")
background = canvas.create_image(
    364.5, 232.0,
    image=background_img)

img0 = PhotoImage(file=f"MainImages/img0.png")
b0 = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=browsefiles,
    relief="flat")

b0.place(
    x=442, y=232,
    width=106,
    height=41)

img1 = PhotoImage(file=f"MainImages/img1.png")
b1 = Button(
    image=img1,
    borderwidth=0,
    highlightthickness=0,
    command=upload,
    relief="flat")

b1.place(
    x=442, y=314,
    width=106,
    height=41)

img2 = PhotoImage(file=f"MainImages/img2.png")
b2 = Button(
    image=img2,
    borderwidth=0,
    highlightthickness=0,
    command=compare,
    relief="flat")

b2.place(
    x=580, y=232,
    width=106,
    height=41)

img3 = PhotoImage(file=f"MainImages/img3.png")
b3 = Button(
    image=img3,
    borderwidth=0,
    highlightthickness=0,
    command=exit,
    relief="flat")

b3.place(
    x=580, y=314,
    width=106,
    height=41)

window.resizable(False, False)
window.mainloop()
