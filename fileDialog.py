from tkinter import *
from tkinter import filedialog


def openFile():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\Felipe\\PycharmProjects\\helloworld",
                                          title="Open File, okay?",
                                          filetypes=(("text files", "*.txt"),
                                                     ("all files", "*.*")))
    file = open(filepath, 'r')
    print(file.read())
    file.close()


# window
window = Tk()

button = Button(text="Open", command=openFile)
button.pack()

window.mainloop()
