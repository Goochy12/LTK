# to handle all files

defaultFileName = "output.txt"


def getInputFile():
    """
    Method to read the import file
    :return: importFilePath - the path to the file
    """
    importFilePath = input("Please enter the path to the import file: ")  # get the file path
    return importFilePath  # return importFilePath


def getOutputFileName():
    """
    Method to get the output file name
    :return: outputFilePath - the path to save the output file
    """
    outputFileName = input("Enter a name for the output file (leave blank for default): ")  # get the file name
    return outputFileName  # return outputFileName


def getOutputFilePath():
    """
    Method to get the output file path where the user wants the end results saved
    :return: outputFilePath - the path to save the output file
    """
    outputFilePath = input("Enter a path for the output file: ")  # get the file path
    return outputFilePath  # return outputFilePath


def getUserOutputFilePath(defaultOutputFileName=defaultFileName):
    """
    Method to get the users prefered output file path and name. A conjunction of methods to reduce code smells.
    :param defaultOutputFileName: the preferred name of the output file
    :return: outputFilePath - the path to the users output file
    """
    outputFileName = getOutputFileName()  # get the users output file name
    #  if the user opted for the default file name
    if outputFileName == "":
        outputFileName = defaultOutputFileName  # use the default output file name
    outputFilePath = getOutputFilePath()  # get the output file path
    outputFilePath += "\\" + outputFileName  # append the file name to the path

    return outputFilePath  # return the output file path


def createOutputFile(fileName=defaultFileName):
    """
    Method to create an output file
    :return: None
    """
    f = open(fileName, "w")  # create the file
    f.close()  # close the file
    return


def writeToFile(line, fileName=defaultFileName):
    """
    Method to write lines to a file
    :param line: a line to write to file
    :return: None
    """
    f = open(fileName, "a")  # open the file
    f.write(line)  # append the line to the file
    return