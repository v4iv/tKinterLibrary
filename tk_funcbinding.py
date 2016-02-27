from tkinter import *

root = Tk()
root.title("My Software")
root.minsize(width=700, height=450)


def print_name():
    printLabel = Label(root, text='My name is Vaibhav Sharma')
    printLabel.pack()


button1 = Button(root, text='Hello !', fg='white', bg='blue', command=print_name)
button1.pack()

root.mainloop()
