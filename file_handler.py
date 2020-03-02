# for file handling

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

    def getUserOutputFilePath(self, systemFileName=""):
        """
        Method to get the users preferred output file path and name. A conjunction of methods to reduce code smells.
        :param systemFileName: file name chosen by the method that called it
        :return: outputFilePath - the path to the users output file
        """
        userOutputFileName = self.getOutputFileName(systemFileName)  # get the users output file name
        #  if the user opted for the default file name
        if userOutputFileName == "":
            userOutputFileName = self.outputFileName  # use the default output file name
        outputFilePath = self.getOutputFilePath()  # get the output file path
        outputFilePath += "\\" + userOutputFileName  # append the file name to the path

        return outputFilePath  # return the output file path

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
