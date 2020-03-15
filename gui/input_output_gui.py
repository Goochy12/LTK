from tkinter import *
from tkinter import filedialog
from features import travel_time_checker

class InputOutputGui:
    def __init__(self, feature):
        self.master = feature[0]
        self.title = feature[1]

        self.inputFile = None
        self.outputFileName = None
        self.outputFilelocation = None

        self.createLayout(self.master)

    def setInputFile(self, f):
        self.inputFile = f
        return

    def setOutputFileName(self, n):
        self.outputFileName = n
        return

    def setOutputFileLocation(self, l):
        self.outputFilelocation = l
        return

    def createLayout(self, window):

        inputLabel = Label(window, text="Input File:")
        inputLabel.grid(row=0, column=0)
        openInputFileButton = Button(window, text="Open File", command=self.getInputFile)
        openInputFileButton.grid(row=0, column=1)

        outputFileNamelabel = Label(window, text="Output File Name:")
        outputFileNamelabel.grid(row=1, column=0)
        outputFileName = Entry(window)
        outputFileName.grid(row=1, column=1)

        outputLocationLabel = Label(window, text="Output Location")
        outputLocationLabel.grid(row=2,column=0)
        outputLocationButton = Button(window, text="Set Location", command=self.setOutputLocation)
        outputLocationButton.grid(row=2,column=1)

        calculateButton = Button(window, text="Calculate", command= lambda j=self.title: self.calculate(j))
        calculateButton.grid(row=3)

        return

    def getInputFile(self):
        inputFile = filedialog.askopenfilename(initialdir="/", title="Open Input File",
                                               filetypes=((".txt files", "*.txt"), ("All Files", "*.*")))
        self.setInputFile(inputFile)
        return inputFile

    def setOutputLocation(self):
        outputLocation = filedialog.askdirectory(initialdir="/")
        self.setOutputFileLocation(outputLocation)
        return outputLocation

    def calculate(self, feature):
        if feature == "Travel Time Checking":
            c = travel_time_checker.TravelTimeChecker()
            message = c.timeDistChecking(self.inputFile, self.outputFileName, self.outputFilelocation)

            if message[0] == "OK":
                # msg okay
                return
            else:
                # something went wrong
                return
        return