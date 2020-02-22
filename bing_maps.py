key = "AhoMw4Yz8HJfzN9iUL1v3i0nA9Nn8SNJudyR_IkxnqcnjYX_sbQn8XZUe2qL9_gO"
import requests

routeURL_synchronous = "http://dev.virtualearth.net/REST/V1/Routes/Driving?"


# latLongList = [[-34.210721,142.0635644],[-37.8015951,144.8645087]]

# url = routeURL_synchronous + "wp.0="+ str(latLongList[0][0]) + "," + str(latLongList[0][1]) + "&wp.1=" + str(latLongList[1][0]) + "," + str(latLongList[1][1]) + "&key="+key
# print(url)

# route = requests.get(url)
# routeJSON = route.json()
# travelDuration = routeJSON["resourceSets"][0]["resources"][0]["travelDistance"]
# print(travelDuration)

def returnRequestJSON(request):
    return request.json()

def makeRouteRequest(latLongList):
    """
    Method to make a GET request to the bing maps API
    :return: route - the request in its raw format
    """
    # construct the URL
    # wp.x indicates a waypoint
    url = routeURL_synchronous + "wp.0=" + str(latLongList[0][0]) + "," + str(latLongList[0][1]) + "&wp.1=" + str(
        latLongList[1][0]) + "," + str(latLongList[1][1]) + "&key=" + key

    route = requests.get(url)  # make the request
    return route
