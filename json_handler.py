import json
import requests

def returnRequestJSON(request):
    """
    Method to return the JSON (python dict) of a request
    :param request: the HTTP request (GET)
    :return: JSON (python dict)
    """
    return request.json()  # return the json