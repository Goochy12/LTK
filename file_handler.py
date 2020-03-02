# for file handling

import os


class FileHandler:
    def __init__(self):
        self.outputFileName = "output.txt"
        self.importFilePath = "input.txt"
        self.outputFilePath = ""
        self.outputFileDirectory = ""

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

    def createOutputFile(self):
        """
        Method to create an output file
        :return: None
        """
        f = open(self.outputFilePath, "w")  # create the file
        f.close()  # close the file
        return

    def writeToFile(self, line):
        """
        Method to write lines to a file
        :param line: a line to write to file
        :return: None
        """
        f = open(self.outputFilePath, "a")  # open the file
        f.write(line)  # append the line to the file
        return

    def createDirectory(self, dir):
        """
        Method to create a directory
        :param dir: path of the directory
        :return: None
        """
        os.mkdir(dir)  # create the directory
        return
