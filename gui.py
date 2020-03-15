from tkinter import *
from tkinter.ttk import *
import variables

class App:
    def __init__(self, master):
        frame = Frame(master, width=400, height=400)
        master.title(variables.applicationName)
        frame.pack()


root = Tk()

# m = Menu(root)
# root.configure(menu=m)
#
# filemenu = Menu(m)
# m.add_cascade(label="File", menu=filemenu)


app = App(root)

# top = Toplevel()
root.mainloop()
root.destroy()