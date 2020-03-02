# file for handling errors

import os

def checkDirectoryExists(dir):
    if not os.path.isdir(dir):
        raise Exception("This directory does not exist! Would you like it to be created (y/n)?")
    return os.path.isdir(dir)

def checkFileExists(dir):
    if not os.path.isfile(dir):
        raise Exception("This file does not exist!")
    return os.path.isfile(dir)