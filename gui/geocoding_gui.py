from tkinter import *
from tkinter import filedialog
from features import geocoding


# TODO:
#   tidy up method

class GeocodingGui:
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
        inputLabel.place(relx=0.2, rely=0.05, )  # set the position
        openInputFileButton = Button(window, text="Open File", command=self.getInputFile)  # input file button
        openInputFileButton.place(relx=0.5, rely=0.05)  # set the position

        outputFileNamelabel = Label(window, text="Output File Name:")  # output label
        outputFileNamelabel.place(relx=0.2, rely=0.15)  # set the position
        outputFileName = Entry(window, state="disabled")  # output file name input
        outputFileName.place(relx=0.5, rely=0.15)  # set the position

        outputLocationLabel = Label(window, text="Output Location")  # output location label
        outputLocationLabel.place(relx=0.2, rely=0.25)  # set the position
        outputLocationButton = Button(window, text="Set Location",
                                      command=self.setOutputLocation)  # output location button
        outputLocationButton.place(relx=0.5, rely=0.25)  # set the position

        calculateButton = Button(window, text="Calculate",
                                 command=self.calculate)  # calculate button
        calculateButton.place(relx=0.4, rely=0.5)  # set the position

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
        # TODO: tidy
        c = geocoding.Geocoding() # initialise the checker
        message = c.geocoding(self.inputFile, self.outputFileName, self.outputFilelocation)  # run the feature

        if message[0] == "OK":
            # msg okay
            return
        else:
            # something went wrong
            return
        return
