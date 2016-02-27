import tkinter.messagebox
from tkinter import *

root = Tk()
root.title("My Software")
root.minsize(width=700, height=450)

answer = tkinter.messagebox.askquestion("Question", "Are You A Banana?")
if answer == 'yes':
    tkinter.messagebox.showinfo("Banana Nation", "Welcome to 9GAG")
else:
    tkinter.messagebox.showinfo("Sorry", "Access Denied")

root.mainloop()
