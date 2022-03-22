from tkinter import *
from Ball import *
import time
window = Tk()

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

volley = Ball(canvas, 0, 0, 85, 3, 2, "white")
tennis = Ball(canvas, 0, 0, 45, 5, 6, "light green")
basket = Ball(canvas, 0, 0, 100, 2, 1, "orange")

while True:
    volley.move()
    tennis.move()
    basket.move()
    window.update()
    time.sleep(0.01)


window.mainloop()
