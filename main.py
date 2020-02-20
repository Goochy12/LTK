# JDAssistance
# v0.1 - Windows
# script to help with manual JDA tasks
#   - Checking travel time
#   - Matching addresses to lat longs
# uses Google Maps API
#   - key: AIzaSyAko7wydJJaoWU313XaWd9fgr2Idunz9uk

import os
import google

def getFile():
    """
    Method to read the import file
    :return: fileName - the name of the file
    """
    fileName = input("Please enter the path to the import file: ")  # get the file path
    return fileName


def parseTimeCheckingFile(fileName):
    return


def timeChecking():
    """
    Method to check how long it takes to get from an Origin point to a Destination point.
    Uses a list of points
    :return: None
    """
    file = getFile() # get input file
    parseTimeCheckingFile(file)
    # parse into array
    # match against maps
    # write to file
    return

def geocoding():
    return

def run():
    """
    Main running method
    :return: None
    """
    os.system("cls")  # wipe the system screen
    exitCode = 3    # code user enters to exit

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
            timeChecking()  # Time Checking
        elif selection == 2:
            geocoding()  # Geocoding (Address -> Lat/Long)
        else:
            quit()


if __name__ == '__main__':
    run()  # run main program