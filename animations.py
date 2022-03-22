from tkinter import *
import time

WIDTH = 400
HEIGHT = 400
xVelocity = 2
yVelocity = 1

window = Tk()

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

backgroundImage = PhotoImage(file='backgroud.png')
background = canvas.create_image(0, 0, image=backgroundImage, anchor=NW)


mario = PhotoImage(file='mario.png')
marioanimation = canvas.create_image(0, 0, image=mario, anchor=NW)

image_width = mario.width()
image_height = mario.height()

while True:
    coordinates = canvas.coords(marioanimation)
    print(coordinates)

    if coordinates[0] >= (WIDTH - image_width) or coordinates[0] < 0:
        xVelocity = -xVelocity

    if coordinates[1] >= (HEIGHT - image_height) or coordinates[1] < 0:
        yVelocity = - yVelocity

    canvas.move(marioanimation, xVelocity, yVelocity)
    window.update()
    time.sleep(0.01)

window.mainloop()
