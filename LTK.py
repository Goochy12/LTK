# LTK (Liam's ToolKit)
# v1.5 - Windows
# script to help with manual tasks
#   - Checking travel time
#   - Matching addresses to lat longs

# TODO: Possible errors
#       File doesn't exist
#       Directory doesn't exist
#       Wrong import file
#       Import file wrong format
#       Creating a file that already exists

import os
import bing_maps
import json_handler
import variables
import file_handler
import error_handler

fileHandler = None


def parseTimeDistanceCheckingFile(filePath):
    """
    Method to parse the file in the format for checking time and distance
    :param filePath: The path to the input file
    :return: latLongList - a list of origin and destination points
    """
    f = open(filePath, "r")  # open the input file

    latLongList = []  # initalise the lat and long list

    # iterate through the lines in the file

    for eachLine in f:
        r = eachLine.split(" ")  # split each line by a space -> origin_lat origin_long dest_lat dest_long

        # iterate through each coordinate and convert to a float
        for i in range(len(r)):
            r[i] = float(r[i])  # convert to a float

        origin = [r[0], r[1]]  # origin coordinates
        dest = [r[2], r[3]]  # destination coordinates

        latLongList.append([origin, dest])  # append the coordinates

    return latLongList  # return the list of lats and longs


def getInputFile():
    """
    Method to read the import file
    :return: None
    """
    # TODO: add error checking for input
    global fileHandler  # get the global fileHandler

    importFilePath = None  # initalise importFilePath

    while importFilePath == None:
        # error checking
        try:
            importFilePath = input("Please enter the path to the import file: ")  # get the file path
            error_handler.checkFileExists(importFilePath)  # check if the file exists
        except:
            print("The file could not be found!")  # print an error message
            importFilePath = None  # reset the input

    fileHandler.setImportFilePath(importFilePath)  # set the importFilePath


def getUserOutputFilePath(systemFileName="output.txt"):
    """
    Method to get the output path
    :param systemFileName:
    :return: None
    """

    global fileHandler  # get the global fileHandler

    getUserOutputFileName(systemFileName)  # get the user output file name
    getUserOutputFileDirectory()  # get the user output file directory

    outputFilePath = fileHandler.getOutputFileDirectory() + "\\" + fileHandler.getOutputFileName()  # create the output file path
    fileHandler.setOutputFilePath(outputFilePath)  # set the output file path

    return


def getUserOutputFileDirectory(systemFileName="output.txt"):
    """
    Method to get the output file path where the user wants the end results saved
    :return: None
    """
    global fileHandler  # get the global fileHandler

    userOutputFileDirectory = None  # initalise importFilePath

    while userOutputFileDirectory == None:
        # error checking
        try:
            userOutputFileDirectory = input("Enter a directory path for the output file: ")  # get the file directory
            error_handler.checkDirectoryExists(userOutputFileDirectory)  # check if the file exists
        except:
            createDirectory = input(
                "The path could not be found! Would you like it to be created for you (y/n)?")  # print an error message / ask to create directory
            if createDirectory == "y":
                fileHandler.createDirectory(userOutputFileDirectory)
            else:
                userOutputFileDirectory = None  # reset the input

    fileHandler.setOutputFileDirectory(userOutputFileDirectory)  # set the output file directory

    return


def getUserOutputFileName(systemFileName="output.txt"):
    """
    Method to get the output file name
    :param systemFileName: file name chosen by the method that called it
    :return: None
    """
    global fileHandler  # get the global fileHandler

    # TODO: add error checking for input
    userOutputFileName = input("Enter a name for the output file (leave blank for default): ")  # get the file name

    fileHandler.setOutputFileName(userOutputFileName)  # set the output file name

    if userOutputFileName == "":
        fileHandler.setOutputFileName(systemFileName)  # if the user chooses the default name

    return


def timeDistChecking():
    """
    Method to get time and distance from an Origin point to a Destination point.
    Uses a list of points
    :return: None
    """
    global fileHandler  # get the global fileHandler

    getInputFile()  # get input file

    latLongList = parseTimeDistanceCheckingFile(fileHandler.getImportFilePath())  # parse into array

    getUserOutputFilePath("timeDistOutput.txt")  # get the users output path

    fileHandler.createOutputFile()  # create a new output file

    message = "Routes Created Successfully!"  # create a success message

    # match against maps
    for eachCoord in latLongList:
        routeRequest = bing_maps.makeRouteRequest(eachCoord)  # make the route request
        routeJSON = json_handler.returnRequestJSON(routeRequest)  # convert response to JSON (python dict)

        travelDistance = routeJSON["resourceSets"][0]["resources"][0]["travelDistance"]  # get the distance
        travelDuration = routeJSON["resourceSets"][0]["resources"][0]["travelDuration"]  # get the duration

        # write to file - origin lat long -> dest lat long | time distance
        outputLine = str(eachCoord[0][0]) + " " + str(eachCoord[0][1]) + " -> " + str(eachCoord[1][0]) + " " + str(
            eachCoord[1][1]) + " | " + str(travelDuration) + ", " + str(travelDistance)
        fileHandler.writeToFile(outputLine)  # write line to file

    printMessage(message)  # print a success or fail message
    return


def parseAddressFile(filePath):
    """
    Method to parse an input file of addresses
    :param filePath: the path to the input file
    :return: addressList - a list of address in the correct format -> 0 country, 1 state, 2 post_code, 3 suburb, 4 local_address
    """
    file = open(filePath, "r")  # open the file
    addressList = []  # create a list of addresses

    # iterate through each line of the file
    for eachLine in file:
        line = eachLine.split(",")  # split the file on a comma
        addressList.append(line)  # append the address to the list

    return addressList  # return the address list


def geocoding():
    """
    Method to get a geocode from a list of addresses.
    :return: None
    """

    global fileHandler  # get the global fileHandler

    getInputFile()  # get input file
    addressList = parseAddressFile(fileHandler.getImportFilePath())  # parse into array

    getUserOutputFilePath("geocodeOutput.txt")  # get the users output path

    fileHandler.createOutputFile()  # create output file

    message = "Geocodes successfully created!"  # create success message

    # iterate through addresses and get geocodes
    for eachAddress in addressList:
        geocodeRequest = bing_maps.makeAddressToGeocodeRequest(eachAddress)  # make route request
        geocodeJSON = json_handler.returnRequestJSON(geocodeRequest)  # convert request into JSON (python dict)

        latitude = geocodeJSON["resourceSets"][0]["resources"][0]["geocodePoints"][0]["coordinates"][0]  # get latitude
        longitude = geocodeJSON["resourceSets"][0]["resources"][0]["geocodePoints"][0]["coordinates"][
            1]  # get longitude

        #  write to file - 0 country, 1 state, 2 post_code, 3 suburb, 4 local_address -> lat long
        outputLine = eachAddress[0] + ", " + eachAddress[1] + ", " + eachAddress[2] + ", " + eachAddress[3] + ", " + \
                     eachAddress[4] + " -> " + str(latitude) + " " + str(longitude)

        fileHandler.writeToFile(outputLine)

    printMessage(message)

    return


def printMessage(message):
    """
    Method to print a message to the user
    :return:
    """
    os.system("cls")  # clear the console
    print(message)  # print the message
    print()

    return


def run():
    """
    Main running method
    :return: None
    """
    os.system("cls")  # wipe the system screen
    exitCode = 3  # code user enters to exit

    print("Welcome to " + variables.applicationName + "!")  # print welcome message
    selection = ""  # initialise user selection

    global fileHandler  # get the global fileHandler
    fileHandler = file_handler.FileHandler()  # initalise the global fileHandler

    while selection != exitCode:
        # iterate while user does not quit
        print("Please select one of the following options:")  # instruction message
        print("\t1. Travel Time Checking.")
        print("\t2. Geocoding (Address -> Lat/Long).")
        print("\t3. Exit.")

        selection = int(input("Option: "))  # get user input

        while selection < 1 or selection > exitCode:
            # while the selection is invalid
            print()
            print("Please make a valid selection.")
            selection = int(input())

        if selection == 1:
            timeDistChecking()  # Time Checking
        elif selection == 2:
            geocoding()  # Geocoding (Address -> Lat/Long)
        else:
            quit()


if __name__ == '__main__':
    run()  # run main program
