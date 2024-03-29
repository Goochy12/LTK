import requests
import variables

headersGlobal = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}

# route URL - http://dev.virtualearth.net/REST/V1/Routes/Driving?o=xml&wp.0=london&wp.1=leeds&avoid=minimizeTolls&key=BingMapsKey
routeURL_synchronous = "http://dev.virtualearth.net/REST/V1/Routes/Driving?"

# location details URL - http://dev.virtualearth.net/REST/v1/Locations/US/WA/98052/Redmond/1%20Microsoft%20Way?o=xml&key={BingMapsKey}
URL_addressToGeocode = "http://dev.virtualearth.net/REST/v1/Locations/"


def makeRouteRequest(latLongs):
    """
    Method to make a GET request to the bing maps API
    # wp.x indicates a way point
    :return: request - the request in its raw format
    """
    global headersGlobal, routeURL_synchronous  # get global variables

    key = variables.bingMapsAPIKey  # api key
    # construct the URL
    url = routeURL_synchronous + "wp.0=" + str(latLongs[0][0]) + "," + str(latLongs[0][1]) + "&wp.1=" + str(
        latLongs[1][0]) + "," + str(latLongs[1][1]) + "&key=" + key

    request = requests.get(url, headers=headersGlobal)  # make the request
    return request  # return the request


def makeAddressToGeocodeRequest(address):
    """
    Method to make an address to geocode request
    :param address: the address in the request - 0 country, 1 state, 2 post code, 3 suburb, 4 local address (street)
    :return: request - the request in its raw format
    """
    global headersGlobal, URL_addressToGeocode # get global variables

    key = variables.bingMapsAPIKey  # api key

    # construct the url
    url = URL_addressToGeocode + str(address[0]) + "/" + str(address[1]) + "/" + str(address[2]) + "/" + str(
        address[3]) + "/" + str(address[4]) + "?key=" + key

    request = requests.get(url, headers=headersGlobal)  # make the request
    return request  # return the request
