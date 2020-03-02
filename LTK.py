# LTK (Liam's ToolKit)
# v1.5 - Windows
# script to help with manual tasks
#   - Checking travel time
#   - Matching addresses to lat longs

import os
import bing_maps
import variables
from file_handler import getInputFile, getUserOutputFilePath, createOutputFile, writeToFile


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
    filePath = getInputFile()  # get input file

    latLongList = parseTimeDistanceCheckingFile(filePath)  # parse into array

    outputFilePath = getUserOutputFilePath("timeDistOutput.txt")  # get the users output path

    createOutputFile(outputFilePath)  # create a new output file

    message = "Routes Created Successfully!"  # create a success message

    # match against maps
    for eachCoord in latLongList:
        routeRequest = bing_maps.makeRouteRequest(eachCoord)  # make the route request
        routeJSON = bing_maps.returnRequestJSON(routeRequest)  # convert response to JSON (python dict)

        travelDistance = routeJSON["resourceSets"][0]["resources"][0]["travelDistance"]  # get the distance
        travelDuration = routeJSON["resourceSets"][0]["resources"][0]["travelDuration"]  # get the duration

        # write to file - origin lat long -> dest lat long | time distance
        outputLine = str(eachCoord[0][0]) + " " + str(eachCoord[0][1]) + " -> " + str(eachCoord[1][0]) + " " + str(
            eachCoord[1][1]) + " | " + str(travelDuration) + ", " + str(travelDistance)
        writeToFile(outputLine, outputFilePath)  # write line to file

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
    filePath = getInputFile()  # get input file
    addressList = parseAddressFile(filePath)  # parse into array

    outputFilePath = getUserOutputFilePath("geocodeOutput.txt")  # get the users output path

    createOutputFile(outputFilePath)  # create output file

    message = "Geocodes successfully created!"  # create success message

    # iterate through addresses and get geocodes
    for eachAddress in addressList:
        geocodeRequest = bing_maps.makeAddressToGeocodeRequest(eachAddress)  # make route request
        geocodeJSON = bing_maps.returnRequestJSON(geocodeRequest)  # convert request into JSON (python dict)

        latitude = geocodeJSON["resourceSets"][0]["resources"][0]["geocodePoints"][0]["coordinates"][0]  # get latitude
        longitude = geocodeJSON["resourceSets"][0]["resources"][0]["geocodePoints"][0]["coordinates"][
            1]  # get longitude

        #  write to file - 0 country, 1 state, 2 post_code, 3 suburb, 4 local_address -> lat long
        outputLine = eachAddress[0] + ", " + eachAddress[1] + ", " + eachAddress[2] + ", " + eachAddress[3] + ", " + \
                     eachAddress[4] + " -> " + str(latitude) + " " + str(longitude)

        writeToFile(outputLine, outputFilePath)

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
