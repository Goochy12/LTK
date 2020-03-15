from tkinter import *
from tkinter.ttk import *
import variables


class App:
    """
    Class to hold the frame of the application
    """

    def __init__(self, master):
        frame = Frame(master)   # create a frame
        self.setWindowName(master, variables.applicationName)   # set the window name

        appGeom = [500,500]   # width x height
        self.setWindowSize(master, appGeom[0], appGeom[1])  # set the size of the window
        self.setWindowResizable(master, False)  # set the window to FALSE resizeable (by the user)

        screenSize = self.getScreensize(master)   # get the size of the users screen
        centerGeom = self.getScreenCenterLocation(appGeom, screenSize)
        self.setWindowLocation(master, appGeom, centerGeom)  # set the location of the window, on the users screen

        frame.pack()    # pack the frame

        # gui layout
        buttonWindowList = []  # create a list for main window buttons

        for eachFeature in variables.featureNames:
            # iterate through the list of features to create a button for
            button = Button(frame, text=eachFeature, command=self.openWindow)  # create the button
            button.pack(side=TOP)  # pack the button
            buttonWindowList.append(button)  # add the button to the list

    def openWindow(self, feature):
        f = Toplevel()
        f.title(feature)

    def setWindowName(self, root, windowName):
        """
        Method to set the name of the window
        :param root: Window root
        :param windowName: Name to set the window
        :return: None
        """
        root.title(windowName)  # set the windows title
        return

    def setWindowSize(self, root, width, height):
        """
        Method to set the size of the window
        :param root: Window root
        :param width: width to set
        :param height: height to set
        :return: None
        """
        root.geometry(str(width)+"x"+str(height))  # set the width x height
        return

    def setWindowResizable(self, root, resizable):
        """
        Method to set the window to resizable
        :param root: Window root
        :param resizable: True or False
        :return: None
        """
        root.resizable(resizable, resizable)    # set resizable
        return

    def getScreensize(self, root):
        """
        Method to get the users screen size
        :param root: Window root
        :return: list of screen width and height
        """
        screenWidth = root.winfo_screenwidth()  # get the screens width
        screenHeight = root.winfo_screenheight()    # get the screens height
        return [screenWidth,screenHeight]   # return width and height

    def getScreenCenterLocation(self, appWindowSize, screenSize):
        """
        Method to get the center location of the users screen
        :return: list of x and y coordinates relational to the center of the users screen
        """
        w = appWindowSize[0]    # application window width
        h = appWindowSize[1]    # application window height
        x = (screenSize[0] / 2) - (w / 2)   # center x coordinate
        y = (screenSize[1] / 2) - (h / 2)   # center y coordinate
        return [x,y]    # return x and y coordinates

    def setWindowLocation(self, root, appWindowSize, screenGeom):
        """
        Method to set the location of the window
        :param root: Window root
        :param appWindowSize: size of the application window
        :param screenGeom: x and y coordinates to place the window
        :return: None
        """
        w = appWindowSize[0]  # application window width
        h = appWindowSize[1]  # application window height
        x = screenGeom[0]   # center x coordinate
        y = screenGeom[1]   # center y coordinate
        root.geometry("%dx%d+%d+%d" % (w,h,x,y))    # set the location of the window
        return




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
