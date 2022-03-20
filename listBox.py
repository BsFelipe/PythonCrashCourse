
def submit():

    food = []

    for index in listbox.curselection():
        food.insert(index, listbox.get(index))

    print("You have ordered:")
    for index in food:
        print(index)


def add():
    listbox.insert(listbox.size(), entryBox.get())
    listbox.config(height=listbox.size())


def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)

    listbox.config(height=listbox.size())


from tkinter import *


window = Tk()

listbox = Listbox(window,
                  bg="#f7ffde",
                  font=("Constantia", 30),
                  width=12,
                  selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1, "pizza")
listbox.insert(2, "hotdog")
listbox.insert(3, "pasta")
listbox.insert(4, "bread")
listbox.insert(5, "coffee")

listbox.config(height=listbox.size())   # use config to change any options

entryBox = Entry(window)
entryBox.pack()

frame = Frame(window)
frame.pack()

submitButton = Button(window, text="submit", command=submit)
submitButton.pack(side=LEFT)

addButton = Button(window, text="add", command=add)
addButton.pack()

deleteButton = Button(window, text="delete", command=delete)
deleteButton.pack()


window.mainloop()
