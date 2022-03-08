from tkinter import *
from tkinter import ttk
from tkinter import filedialog

window = Tk()
window.title("Plagiarism Detection System")
canvas = Canvas(window, width=600, height=300)
canvas.grid(columnspan=2, rowspan=4)

# Define a function to open the file explrer


def browsefiles():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Text files",
                                                      "*.txt*"),
                                                     ("all files",
                                                      "*.*")))


# Select Document#1 button
button1 = Button(window, text="Select Document#1", height=2, width=20,
                 font="Raleway", bg="#20bebe", fg="white", command=browsefiles)
button1.grid(row=0, column=0)

# Select Document#2 button
button2 = Button(window, text="Select Document#2", height=2, width=20,
                 font="Raleway", bg="#20bebe", fg="white", command=browsefiles)
button2.grid(row=1, column=0)


window.mainloop()
