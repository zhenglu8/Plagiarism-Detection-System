from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from tkinter.messagebox import showinfo
import pyrelog as pl
import pysimilaralgorithm as pa
import os
import pyrebase

firebaseConfig = {
  'apiKey': "AIzaSyAEp8_HarY6xSVZEgiXiko67ntgVuCXmwg",
  'authDomain': "integrationproject-8160f.firebaseapp.com",
  'databaseURL': "https://integrationproject-8160f-default-rtdb.firebaseio.com/",
  'projectId': "integrationproject-8160f",
  'storageBucket': "integrationproject-8160f.appspot.com",
  'messagingSenderId': "1053011153629",
  'appId': "1:1053011153629:web:b1f1c1a15cb213c2f88134",
  'measurementId': "G-9T553ECDE0"
};


firebase=pyrebase.initialize_app(firebaseConfig)

db=firebase.database()
storage=firebase.storage()

window = Tk()
window.title("Plagiarism Detection System")
canvas = Canvas(window, width=1000, height=400)
canvas.grid(columnspan=2, rowspan=4)

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

        storage.child(file.name).put(file.name)
        url = storage.child(file.name).get_url(None)
        data = {"url": url}
        db.child("documents").push(data)

        try:
            with open('docs/selected_file.txt', 'w') as f:
                f.write(content)
        except FileNotFoundError:
            print("The 'docs' directory does not exist")

    showinfo(
        title='Selected File',
        message=file.name
    )

    # Document#1 filename
    label1 = Label(window, text=file.name)
    label1.grid(row=1, column=0)


def compare():
    checking = pa.pyrecheck('docs/selected_file.txt', pl.firebaseConfig)

    checking.connect()

    checking.connect_storage()
    checking.connect_database()

    checking.compare_against_files()
    print(checking.return_results())


def exit():
    try:
        os.remove("docs/selected_file.txt")
    except Exception as e:
        print(e)

    window.destroy()


# Select Document#1 button
button1 = Button(window, text="Select Document#1", height=2, width=20,
                 font="Raleway", bg="#20bebe", fg="white", command=browsefiles)
button1.grid(row=0, column=0)

# Select Document#2 button

# Compare button
button3 = Button(window, text="Compare", height=2, width=20,
                 font="Raleway", bg="#20bebe", fg="white", command=compare)
button3.grid(row=0, column=1)

# Exit button
button4 = Button(window, text="Exit", height=2, width=20,
                 font="Raleway", bg="#20bebe", fg="white", command=exit)
button4.grid(row=2, column=1)

window.mainloop()
