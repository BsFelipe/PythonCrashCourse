from tkinter import *

def openFile():
    print("You open a file")

def saveFile():
    print("Save file")

def cut():
    print("cut")

def copy():
    print("copy")

def paste():
    print("past")


window = Tk()

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_cascade(label="Open", command=openFile)
fileMenu.add_cascade(label="Save", command=saveFile)
fileMenu.add_separator()
fileMenu.add_cascade(label="Exit", command=quit)

editMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_cascade(label="Cut", command=cut)
editMenu.add_cascade(label="Copy", command=copy)
editMenu.add_cascade(label="Paste", command=paste)

window.mainloop()
