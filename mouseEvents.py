from tkinter import *


def doSomething(event):
    print("HeMouse coordinates: " + str(event.x)+","+str(event.y))


window = Tk()

# window.bind("<Button-1>", doSomething) #    left mouse click
# window.bind("<Button-2>", doSomething) #    scroll wheel
# window.bind("<Button-3>", doSomething) #    right mouse click
# window.bind("<ButtonRelease>", doSomething) # button release
# window.bind("<Enter>", doSomething) # button enter the window
# window.bind("<Leave>", doSomething) # button leave the window
window.bind("<Motion>", doSomething) # where the mouse move

window.mainloop()
