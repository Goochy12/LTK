# for file handling

import os


class FileHandler:
    def __init__(self):
        self.outputFileName = "output.txt"
        self.importFilePath = "input.txt"
        self.outputFilePath = ""
        self.outputFileDirectory = ""
        self.errorOccured = False

    def getOutputFileName(self):
        return self.outputFileName

    def setOutputFileName(self, fileName):
        self.outputFileName = fileName

    def setImportFilePath(self, fileName):
        self.importFilePath = fileName

    def getImportFilePath(self):
        return self.importFilePath

    def getOutputFilePath(self):
        return self.outputFilePath

    def setOutputFilePath(self, path):
        self.outputFilePath = path

    def getOutputFileDirectory(self):
        return self.outputFileDirectory

    def setOutputFileDirectory(self, directory):
        self.outputFileDirectory = directory

    def getErrorOccured(self):
        return self.errorOccured

    def setErrorOccured(self, e):
        self.errorOccured = e

    def createOutputFilePath(self):
        self.setOutputFilePath(self.outputFileDirectory+"\\"+self.outputFileName+".txt")

    def createOutputFile(self):
        """
        Method to create an output file
        :return: None
        """
        try:
            self.createOutputFilePath()
            f = open(self.outputFilePath, "w")  # create the file
            f.close()  # close the file
        except OSError:
            print("\nThere was an error creating the output file.")
            self.setErrorOccured(True)

        return

    def writeToFile(self, line):
        """
        Method to write lines to a file
        :param line: a line to write to file
        :return: None
        """
        try:
            f = open(self.outputFilePath, "a")  # open the file
            f.write(line)  # append the line to the file
        except OSError:
            print("There was an error writing to the output file.")
            self.setErrorOccured(True)
        return

    def createDirectory(self, dir):
        """
        Method to create a directory
        :param dir: path of the directory
        :return: None
        """
        try:
            os.mkdir(dir)  # create the directory

        except OSError:
            print("There was an error creating the output directory.")
            self.setErrorOccured(True)
        return
