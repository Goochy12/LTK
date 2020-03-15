import big_maps_requests
import requests_handler
import file_handler

class TravelTimeChecker:
    def __init__(self):
        self.fileHandler = file_handler.FileHandler()

    def parseTimeDistanceCheckingFile(self, filePath):
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


    def timeDistChecking(self, inputFile, outputFileName, outputFileLocation):
        """
        Method to get time and distance from an Origin point to a Destination point.
        Uses a list of points
        :return: None
        """

        self.fileHandler.setImportFilePath(inputFile)
        # self.fileHandler.setOutputFileName(outputFileName)
        self.fileHandler.setOutputFileName("test")
        self.fileHandler.setOutputFileDirectory(outputFileLocation)
        self.fileHandler.createOutputFile()

        latLongList = self.parseTimeDistanceCheckingFile(inputFile)  # parse into array

        # match against maps
        for eachCoord in latLongList:
            routeRequest = big_maps_requests.makeRouteRequest(eachCoord)  # make the route request
            routeJSON = requests_handler.returnRequestJSON(routeRequest)  # convert response to JSON (python dict)

            travelDistance = routeJSON["resourceSets"][0]["resources"][0]["travelDistance"]  # get the distance
            travelDuration = routeJSON["resourceSets"][0]["resources"][0]["travelDuration"]  # get the duration

            # write to file - origin lat long -> dest lat long | time distance
            outputLine = str(eachCoord[0][0]) + " " + str(eachCoord[0][1]) + " -> " + str(eachCoord[1][0]) + " " + str(
                eachCoord[1][1]) + " | " + str(travelDuration) + ", " + str(travelDistance)
            self.fileHandler.writeToFile(outputLine)  # write line to file

        message = "Routes Created Successfully!"  # create a success message
        # printMessage(message)  # print a success or fail message
        return