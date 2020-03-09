import json
import requests

def returnRequestJSON(request):
    """
    Method to return the JSON (python dict) of a request
    :param request: the HTTP request (GET)
    :return: JSON (python dict)
    """
    try:
        return request.json()  # return the json
    except json.decoder.JSONDecodeError:
        print(request.json())
