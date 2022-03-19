# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets

from tkinter import *

window = Tk()   # instantiate an instance of a window
window.geometry("420x420")
window.title("Felipe GUI program")

favicon = PhotoImage(file='mario.png')
window.iconphoto(True, favicon)
window.config(background="#30343F")

window.mainloop()   # place window on computer screen, listen for events
