'''
Created on 02.08.2011

@author: Lipatov
'''
import unittest

from calculator.Variables import Variables

class Test(unittest.TestCase):


    def testVariables(self):
        
        vars = Variables()
        vars.add("key1", 5.0)
        self.assertEqual(vars.get("key1"), 5.0)
        vars.add("key2", 6.0)
        vars.add("key3", 7.0)
        vars.remove("key2")
        self.assertEqual(vars.get("key3"), 7.0)
        self.assertEqual(vars.contains("key4"), False)
        pass


    if __name__ == "__main__" :
        #import sys;sys.argv = ['', 'Test.testName']
        unittest.main()