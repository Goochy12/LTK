import unittest
import LTK
import tkinter

class MyTestCase(unittest.TestCase):
    # def test_fileCreation(self):
    #     main.createOutputFile()
    #     f = open("output.txt","r")
    #     # self.assertTrue(f.readlines()=="")
    #     # self.assertFalse(f.readlines()=="")
    #
    # def test_timeDistChecker(self):
    #     main.timeDistChecking()

    # def test_geocodeChecker(self):
    #     LTK.geocoding()

    tkinter._test()


if __name__ == '__main__':
    unittest.main()
