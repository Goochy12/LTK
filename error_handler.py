# file for handling errors

import os

def checkDirectoryExists(dir):
    if not os.path.isdir(dir):
        raise Exception("This directory does not exist!")
    return os.path.isdir(dir)

def checkFileExists(dir):
    if os.path.isfile(dir):
        return True
    return False