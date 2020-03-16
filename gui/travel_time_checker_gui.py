from tkinter import *
from tkinter import filedialog
from features import travel_time_checker


# TODO:
#   Add comments
#   tidy up method

class TravelTimeCheckerGui:
    """
    Class to create a travel time checker and handle I/O and events
    """

    def __init__(self, master, feature):
        """
        Init method
        :param master: master window
        :param feature: information about the feature
        """
        self.master = master  # set the master
        self.title = feature[1]  # set the title

        self.inputFile = None  # set the input file
        self.outputFileName = None  # set the output file name
        self.outputFilelocation = None  # set the output file location

        self.createLayout(self.master)  # create the layout

    def setInputFile(self, f):
        """
        Method to set the input file
        :param f: file path
        :return: None
        """
        self.inputFile = f  # set the input file
        return

    def setOutputFileName(self, n):
        """
        Method to set the output file name
        :param n: name of the output file
        :return: None
        """
        self.outputFileName = n  # set the output file name
        return

    def setOutputFileLocation(self, l):
        """
        Method to set the output file location
        :param l: location for the output file
        :return: None
        """
        self.outputFilelocation = l  # set the output file location
        return

    def createLayout(self, window):
        """
        Method to create the layout
        :param window: the master window
        :return: None
        """

        inputLabel = Label(window, text="Input File:")  # input label
        inputLabel.grid(row=0, column=0)  # set the position
        openInputFileButton = Button(window, text="Open File", command=self.getInputFile)  # input file button
        openInputFileButton.grid(row=0, column=1)  # set the position

        outputFileNamelabel = Label(window, text="Output File Name:")  # output label
        outputFileNamelabel.grid(row=1, column=0)  # set the position
        outputFileName = Entry(window)  # output file name input
        outputFileName.grid(row=1, column=1)  # set the position

        outputLocationLabel = Label(window, text="Output Location")  # output location label
        outputLocationLabel.grid(row=2, column=0)  # set the position
        outputLocationButton = Button(window, text="Set Location",
                                      command=self.setOutputLocation)  # output location button
        outputLocationButton.grid(row=2, column=1)  # set the position

        calculateButton = Button(window, text="Calculate",
                                 command=lambda j=self.title: self.calculate(j))  # calculate button
        calculateButton.grid(row=3)  # set the position

        return

    def getInputFile(self):
        """
        Method to get the input file location
        :return: the input file location
        """
        inputFile = filedialog.askopenfilename(initialdir="/", title="Open Input File",
                                               filetypes=((".txt files", "*.txt"), ("All Files", "*.*")))   # open the file dialog
        self.setInputFile(inputFile)    # set the input file variable
        return inputFile    # return the input file path

    def setOutputLocation(self):
        """
        Method to set the output file location
        :return: the output file location
        """
        outputLocation = filedialog.askdirectory(initialdir="/")    # open file locator dialog
        self.setOutputFileLocation(outputLocation)  # set the output file location variable
        return outputLocation   # return the output file location

    def calculate(self):
        """
        Method to run the calculate function of the feature
        :return: None
        """
        c = travel_time_checker.TravelTimeChecker() # initialise the checker
        message = c.timeDistChecking(self.inputFile, self.outputFileName, self.outputFilelocation)  # run the feature

        if message == "OK":
            # msg okay
            return
        else:
            # something went wrong
            return
        return
