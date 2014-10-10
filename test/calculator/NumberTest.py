'''
Created on 02.08.2011

@author: Lipatov
'''
import unittest
from calculator.Number import Number


class Test(unittest.TestCase):


    def testNumberSetValueGetValue(self):
        temp = Number()
        self.assertEqual(0, temp.getValue())
        temp.setValue("5.0")
        self.assertEqual(5.0, 5.0)
        pass


    if __name__ == "__main__" :
        #import sys;sys.argv = ['', 'Test.testName']
        unittest.main()