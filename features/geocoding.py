import big_maps_requests
import requests_handler
import file_handler


# TODO:
#   Add comments
#   tidy up method

class Geocoding:
    def __init__(self):
        self.fileHandler = file_handler.FileHandler()

    def parseAddressFile(self, filePath):
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

    def geocoding(self, inputFile, outputFileName, outputFileLocation):
        """
        Method to get a geocode from a list of addresses.
        :return: None
        """

        self.fileHandler.setImportFilePath(inputFile)  # set the input file
        # self.fileHandler.setOutputFileName(outputFileName)    # set the output file name
        self.fileHandler.setOutputFileName("geocodeOutput.txt")
        self.fileHandler.setOutputFileDirectory(outputFileLocation)  # set the output file directory
        self.fileHandler.createOutputFile()  # create the output file


        addressList = self.parseAddressFile(inputFile)  # parse into array

        self.fileHandler.createOutputFile()  # create output file

        # iterate through addresses and get geocodes
        if self.fileHandler.getErrorOccured() == False:
            for eachAddress in addressList:
                geocodeRequest = big_maps_requests.makeAddressToGeocodeRequest(eachAddress)  # make route request
                geocodeJSON = requests_handler.returnRequestJSON(
                    geocodeRequest)  # convert request into JSON (python dict)

                latitude = geocodeJSON["resourceSets"][0]["resources"][0]["geocodePoints"][0]["coordinates"][
                    0]  # get latitude
                longitude = geocodeJSON["resourceSets"][0]["resources"][0]["geocodePoints"][0]["coordinates"][
                    1]  # get longitude

                #  write to file - 0 country, 1 state, 2 post_code, 3 suburb, 4 local_address -> lat long
                outputLine = eachAddress[0] + ", " + eachAddress[1] + ", " + eachAddress[2] + ", " + eachAddress[
                    3] + ", " + \
                             eachAddress[4] + " -> " + str(latitude) + " " + str(longitude)

                self.fileHandler.writeToFile(outputLine)

        message = "Geocodes successfully created!"  # create success message
        # printMessage(message)  # print a success or failure message

        return
