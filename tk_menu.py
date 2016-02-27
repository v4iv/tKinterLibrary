from tkinter import *


def doNothing():
    print("Fine I won't!")


root = Tk()
root.title("My Software")
root.minsize(width=700, height=450)
# ******** Menu Bar **********
menu = Menu(root)
root.config(menu=menu)

fileMenu = Menu(menu)
menu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New Project...", command=doNothing)
fileMenu.add_command(label="New...", command=doNothing)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=root.quit)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=doNothing)

# ******** Toolbar **********
toolbar = Frame(root, bg='gray')
findIcon = Button(toolbar, text="Find", command=doNothing)
findIcon.pack(side=LEFT, padx=2, pady=2)
printIcon = Button(toolbar, text="Print", command=doNothing)
printIcon.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

# ******** Status Bar **********
status = Label(root, text="Initializing...", bd=1, relief=SUNKEN, anchor=W, bg="dark gray")
status.pack(side=BOTTOM, fill=X)

root.mainloop()