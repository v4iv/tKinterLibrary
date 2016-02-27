from tkinter import *

root = Tk()
root.title("My Software")
root.minsize(width=700, height=450)

one = Label(root, text='NEO', fg='white', bg='black')
one.pack()
two = Label(root, text='OWT', fg='white', bg='green')
two.pack(fill=X)
three = Label(root, text='EERHT', fg='white', bg='blue')
three.pack(side=LEFT, fill=Y)

root.mainloop()
