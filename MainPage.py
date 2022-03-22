from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.messagebox import showinfo

window = Tk()
window.title("Plagiarism Detection System")
canvas = Canvas(window, width=1000, height=400)
canvas.grid(columnspan=2, rowspan=4)

label1 = Label(window)
label2 = Label(window)

# Define a function to open the file explrer


def browsefiles1():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Word files",
                                                      "*.doc*"),
                                                     ("all files",
                                                      "*.*")))

    showinfo(
        title='Selected File',
        message=filename
    )

    label1 = Label(window, text=filename)
    label1.grid(row=1, column=0)


def browsefiles2():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Word files",
                                                      "*.doc*"),
                                                     ("all files",
                                                      "*.*")))

    showinfo(
        title='Selected File',
        message=filename
    )

    label2 = Label(window, text=filename)
    label2.grid(row=3, column=0)


# Select Document#1 button
button1 = Button(window, text="Select Document#1", height=2, width=20,
                 font="Raleway", bg="#20bebe", fg="white", command=browsefiles1)
button1.grid(row=0, column=0)

# Document#1 filename


# Select Document#2 button
button2 = Button(window, text="Select Document#2", height=2, width=20,
                 font="Raleway", bg="#20bebe", fg="white", command=browsefiles2)
button2.grid(row=2, column=0)

# Compare button
button3 = Button(window, text="Compare", height=2, width=20,
                 font="Raleway", bg="#20bebe", fg="white")
button3.grid(row=0, column=1)

# Exit button
button4 = Button(window, text="Exit", height=2, width=20,
                 font="Raleway", bg="#20bebe", fg="white", command=lambda: window.destroy())
button4.grid(row=2, column=1)

window.mainloop()
