from tkinter import *


class GuiButtons:
    def print_message(self):
        print("This is Awesome!")

    def __init__(self, master):  # master : main/root window
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text="Display", command=self.print_message)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="Quit", command=frame.quit)
        self.quitButton.pack(side=LEFT)


root = Tk()
gb = GuiButtons(root)
root.mainloop()
