from tkinter import *
from tkinter import filedialog


def saveFile():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\Felipe\\PycharmProjects\\helloworld",
                                    defaultextension='.txt',
                                    filetypes=[
                                        ("Text file", ".txt"),
                                        ("HTML files", ".html"),
                                        ("PDF files", ".pdf"),
                                        ("All files", ".*")
                                    ])
    if file is None:
        return
    gettext = str(text.get(1.0, END))
    # gettext = input("enter some text: ") - input from console
    file.write(gettext)
    file.close()


# window
window = Tk()

button = Button(text='save', command=saveFile)
button.pack()

text = Text(window)
text.pack()


window.mainloop()
