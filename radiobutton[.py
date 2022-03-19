from tkinter import *

food = ["pizza", "hamburger", "hotdog"]

def order():
    if x.get() == 0:
        print("You ordered pizza")
    elif x.get() == 1:
        print("You ordered a hamburger")
    elif x.get() == 2:
        print("You ordered a hotdog")
    else:
        print("huh?")


window = Tk()

pizzaImage = PhotoImage(file='pizza.png')
hamburgerImage = PhotoImage(file='hambuerger.png')
hotdogImage = PhotoImage(file='hotdog.png')
foodImages = [pizzaImage, hamburgerImage, hotdogImage]

x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index],     # adds text to radio buttons,
                              variable=x,   # groups radiobuttons together if they the same variable
                              value=index,  # assigns each radiobutton a different value
                              padx=25,
                              pady=25,
                              font=("Impact", 50),
                              image=foodImages[index],
                              compound='left',
                              indicatoron=0, # eliminate circle indicators
                              width=600, # set width of radio buttons
                              command=order) #set commando to a function)

    radiobutton.pack(anchor=W)

window.mainloop()
