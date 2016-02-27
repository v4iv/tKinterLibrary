from tkinter import *

root = Tk()

topFrame = Frame(root)
topFrame.pack()  # by default at the top
botFrame = Frame(root)
botFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text='Lorem', fg='red')
button2 = Button(topFrame, text='Ipsum', fg='red')
button3 = Button(topFrame, text='Lorem', fg='blue')
button4 = Button(botFrame, text='Ipsum', fg='blue')

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

root.mainloop()
