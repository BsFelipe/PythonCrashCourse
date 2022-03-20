from tkinter import *

def submit():
    print("The temperature is: "+ str(scale.get()) + " degrees C")


window = Tk()
window.geometry("1200x1200")

hotImage = PhotoImage(file='hot.png')
hotLabel = Label(image=hotImage)
hotLabel.pack()

scale = Scale(window,
              from_=100,
              to=0,
              length=600,
              orient=VERTICAL,
              font=('Arial', 15),
              tickinterval=10,
              #showvalue=0,
              resolution=5,
              troughcolor='#69EAFE',
              fg='#FF1c00',
              bg='black')

scale.set(((scale['from']-scale['to'])/2)+scale['to'])

scale.pack()

coldImage = PhotoImage(file='cold.png')
coldLabel = Label(image=coldImage)
coldLabel.pack()

button = Button(window,
                text='submit',
                command=submit)
button.pack()

window.mainloop()