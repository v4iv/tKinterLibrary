from tkinter import *

root = Tk()
root.title("My Software")

arrowImage = PhotoImage(file='./images/Arrow.png')
checkImage = PhotoImage(file='./images/Checkmark.png')
xclaimImage = PhotoImage(file='./images/Exclaim.png')
xImage = PhotoImage(file='./images/X.png')

arrowLabel = Label(root, image=arrowImage)
checkLabel = Label(root, image=checkImage)
xclaimLabel = Label(root, image=xclaimImage)
xLabel = Label(root, image=xImage)

arrowLabel.pack(side=LEFT)
checkLabel.pack(side=LEFT)
xclaimLabel.pack(side=LEFT)
xLabel.pack(side=LEFT)

root.mainloop()
