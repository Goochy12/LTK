import unittest
import main

class MyTestCase(unittest.TestCase):
    def test_fileCreation(self):
        main.createOutputFile()
        f = open("output.txt","r")
        # self.assertTrue(f.readlines()=="")
        # self.assertFalse(f.readlines()=="")



if __name__ == '__main__':
    unittest.main()
