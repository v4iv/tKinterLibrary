from tkinter import *

root = Tk()
root.title("My Software")

canvas = Canvas(root, width=200, height=100)
canvas.pack()

blackLine = canvas.create_line(0, 0, 200, 50)
redLine = canvas.create_line(0, 100, 200, 50, fill='red')
greenBox = canvas.create_rectangle(20, 20, 100, 50, fill='green')

canvas.delete(blackLine)  # also All

root.mainloop()
