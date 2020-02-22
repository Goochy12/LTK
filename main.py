# JDAssistance
# v0.1 - Windows
# script to help with manual JDA tasks
#   - Checking travel time
#   - Matching addresses to lat longs

import os
import bing_maps

fileName = "output.txt"


def getFile():
    """
    Method to read the import file
    :return: importFilePath - the path to the file
    """
    importFilePath = input("Please enter the path to the import file: ")  # get the file path
    return importFilePath  # return importFilePath


def createOutputFile():
    """
    Method to create an output file
    :return: None
    """
    global fileName  # get the global output file name
    f = open(fileName, "w")  # create the file
    f.close()  # close the file
    return


def writeToFile(line):
    """
    Method to write lines to a file
    :param line: a line to write to file
    :return: None
    """
    global fileName  # get the global output file name
    f = open(fileName, "a")  # open the file
    f.write(line)  # append the line to the file
    return


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


def timeDistChecking():
    """
    Method to get time and distance from an Origin point to a Destination point.
    Uses a list of points
    :return: None
    """
    filePath = getFile()  # get input file

    latLongList = parseTimeDistanceCheckingFile(filePath)  # parse into array
    # latLongList = [[[-34.210721, 142.0635644], [-37.8015951, 144.8645087]]]

    createOutputFile()  # create a new output file
    message = "Routes Created Successfully!"  # create a success message

    # match against maps
    for eachCoord in latLongList:
        route = bing_maps.makeRouteRequest(eachCoord)  # make the route request
        routeJSON = bing_maps.returnRequestJSON(route)  # convert response to JSON (python dict)

        travelDistance = routeJSON["resourceSets"][0]["resources"][0]["travelDistance"]  # get the distance
        travelDuration = routeJSON["resourceSets"][0]["resources"][0]["travelDuration"]  # get the duration

        # write to file - origin lat long -> dest lat long | time distance
        outputLine = str(eachCoord[0][0]) + "/" + str(eachCoord[0][1]) + " -> " + str(eachCoord[1][0]) + "/" + str(
            eachCoord[1][1]) + " | " + str(travelDuration) + ", " + str(travelDistance)
        writeToFile(outputLine)  # write line to file

    printMessage(message)
    return


def geocoding():
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

    print("Welcome to JDAssistance!")  # print welcome message
    selection = ""  # initialise user selection

    while selection != exitCode:
        # iterate while user does not quit
        print("Please select one of the following options:")  # instruction message
        print("\t1. Travel Time Checking.")
        print("\t2. Geocoding (Address -> Lat/Long).")
        print("\t4. Exit.")

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
