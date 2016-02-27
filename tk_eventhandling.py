from tkinter import *

root = Tk()
root.title("My Software")
root.minsize(width=700, height=450)


def left_click(event):
    print("Left Click")


def middle_click(even):
    print("Middle Click")


def right_click(event):
    print("Right Click")


pyframe = Frame(root, width=500, height=350)
pyframe.bind("<Button-1>", left_click)
pyframe.bind("<Button-2>", middle_click)
pyframe.bind("<Button-3>", right_click)
pyframe.pack()

root.mainloop()
