# file for handling errors

import os

def checkDirectoryExists(dir):
    if os.path.isdir(dir):
        return True
    return False

def checkFileExists(dir):
    if os.path.isfile(dir):
        return True
    return False