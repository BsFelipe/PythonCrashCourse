from tkinter import *

# grid() = geometry manager that organizes widgets in a table-lie structure

window = Tk()

firstName = Label(window, text="First name: ", width=20, bg="red").grid(row=0, column=0)
firstNameEntry = Entry(window).grid(row=0, column=1)

lastName = Label(window, text="Last name: ", bg="green").grid(row=1, column=0)
lastNameEntry = Entry(window).grid(row=1, column=1)

email = Label(window, text="Last name: ", bg="blue", width=30).grid(row=2, column=0)
emailEntry = Entry(window).grid(row=2, column=1)

submitButton = Button(window,text="Submit").grid(row=3, column=0, columnspan=2)

window.mainloop()