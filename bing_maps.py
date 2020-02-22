import requests

key = "AhoMw4Yz8HJfzN9iUL1v3i0nA9Nn8SNJudyR_IkxnqcnjYX_sbQn8XZUe2qL9_gO"
routeURL_synchronous = "http://dev.virtualearth.net/REST/V1/Routes/Driving?"


def returnRequestJSON(request):
    """
    Method to return the JSON (python dict) of a request
    :param request: the HTTP request (GET)
    :return: JSON (python dict)
    """
    return request.json()


def makeRouteRequest(latLongList):
    """
    Method to make a GET request to the bing maps API
    # wp.x indicates a way point
    :return: route - the request in its raw format
    """
    global key
    # construct the URL
    url = routeURL_synchronous + "wp.0=" + str(latLongList[0][0]) + "," + str(latLongList[0][1]) + "&wp.1=" + str(
        latLongList[1][0]) + "," + str(latLongList[1][1]) + "&key=" + key

    route = requests.get(url)  # make the request
    return route
