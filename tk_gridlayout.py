from tkinter import *

root = Tk()

userLabel = Label(root, text='Username')
passLabel = Label(root, text='Password')
userEntry = Entry(root)
passEntry = Entry(root)
remmeBox = Checkbutton(root, text='Keep Me Logged In')
loginButton = Button(root, text='Submit', fg='white', bg='blue')

userLabel.grid(row=0, sticky=E)  # N E W S = North East West South
userEntry.grid(row=0, column=1, sticky=E)
passLabel.grid(row=1, sticky=E)
passEntry.grid(row=1, column=1, sticky=E)
remmeBox.grid(row=2, columnspan=2, sticky=E)
loginButton.grid(row=3, column=1, sticky=E)

root.mainloop()
