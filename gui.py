from tkinter import *
from tkinter.ttk import *
import variables



class App:
    def __init__(self, master):
        frame = Frame(master, width=400, height=400)
        master.title(variables.applicationName)
        master.geometry("400x400")
        frame.pack()

        # gui layout
        buttonWindowList = []
        # travelTimeCheckingWindowButton = Button(frame, text=variables.featureNames[0])  # Travel Time Checking
        # geocodingWindowButton = Button(frame, text=variables.featureNames[1])  # Geocoding
        #
        # buttonWindowList.append(travelTimeCheckingWindowButton)
        # buttonWindowList.append(geocodingWindowButton)
        # travelTimeCheckingWindowButton.grid(column=0, row=1)

        for eachFeature in variables.featureNames:
            button = Button(frame, text=eachFeature)
            buttonWindowList.append(button)

        for eachButton in buttonWindowList:
            eachButton.pack(side=TOP)



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