'''
Created on 02.08.2011

@author: Lipatov
'''
import unittest

from calculator.Calculator import Calculator

class Test(unittest.TestCase):
    
    def testPlus(self):
        Calc = Calculator()
        self.assertEqual(Calc.calculate("2 + 3"), 5.0)
        pass
    
    def tesMinus(self):
        Calc = Calculator()
        self.assertEqual(Calc.calculate("2-3"), -1.0)
        pass

    def testMultiplePluses(self):
        Calc = Calculator()
        self.assertEqual(Calc.calculate("2+2+2"), 6.0)
        pass
    
    def testMultipleMinuses(self):
        Calc = Calculator()
        self.assertEqual(Calc.calculate("12-22-50"), -60.0)
        pass
    
    def testMultiplication(self):
        Calc = Calculator()
        self.assertEqual(Calc.calculate("12*2"), 24.0)
        pass
    
    def testDivision(self):
        Calc = Calculator()
        self.assertEqual(Calc.calculate("12/2"), 6.0)
        pass

    def testMultipleMultiplication(self):
        Calc = Calculator()
        self.assertEqual(Calc.calculate("12*2*10"), 240.0)
        pass
    
    def testMultipleDivision(self):
        Calc = Calculator()
        self.assertEqual(Calc.calculate("12/2/3"), 2.0)
        pass
    
    def testBrackets(self):
        Calc = Calculator()
        self.assertEqual(Calc.calculate("(2 + 2) * 2"), 8.0)
        pass
    
    def testDegree(self):
        Calc = Calculator()
        self.assertEqual(Calc.calculate("(4 - 2)^4"), 16.0)
        pass
    
    def testModulusWithZero(self):
        Calc = Calculator()
        self.assertEqual(Calc.calculate("6%3"), 0.0)
        pass
    
    def testDivisionByZero(self):
        Calc = Calculator()
        self.assertRaises(BaseException, Calc.calculate, "6/0")
        pass
    
    def testModulesByZero(self):
        Calc = Calculator()
        self.assertRaises(BaseException, Calc.calculate, "6%0")
        pass
    
    def testBracketsUnbalance(self):
        Calc = Calculator()
        self.assertRaises(BaseException, Calc.calculate, "(2 + 2 * 2")
        pass
    
    def testFunction_abs(self):
        Calc = Calculator()
        self.assertEqual(Calc.calculate("abs(-5)"), 5.0)
        pass
    
    def testFunction_log10(self):
        Calc = Calculator()
        self.assertEqual(Calc.calculate("log10(100)"), 2.0)
        pass
    
    def testFunction_sqrt(self):
        Calc = Calculator()
        self.assertEqual(Calc.calculate("sqrt(144)"), 12.0)
        pass
    
    def testFunction_acos(self):
        Calc = Calculator()
        self.assertEqual(Calc.calculate("ceil(acos(6.0))"), 2.0)
        pass
    
    def testFunction_asin(self):
        Calc = Calculator()
        self.assertEqual(Calc.calculate("asin(0)"), 0.0)
        pass
    
    def testFunction_atan(self):
        Calc = Calculator()
        self.assertEqual(Calc.calculate("atan(0)"), 0.0)
        pass
    
    def testFunction_cos(self):
        Calc = Calculator()
        self.assertEqual(Calc.calculate("cos(0)"), 1.0)
        pass
    
    def testFunction_sin(self):
        Calc = Calculator()
        self.assertEqual(Calc.calculate("sin(0)"), 0.0)
        pass
    
    def testFunction_tan(self):
        Calc = Calculator()
        self.assertEqual(Calc.calculate("tan(0)"), 0.0)
        pass
    
    def testFunction_ceil(self):
        Calc = Calculator()
        self.assertEqual(Calc.calculate("ceil(0.5)"), 1.0)
        pass
    
    def testFunction_floor(self):
        Calc = Calculator()
        self.assertEqual(Calc.calculate("floor(0.5)"), 0.0)
        pass
    
    def testFunction_sinInCeil(self):
        Calc = Calculator()
        self.assertEqual(Calc.calculate("ceil(sin(0.5))"), 1.0)
        pass
    
    def testFunction_degreeInCos(self):
        Calc = Calculator()
        self.assertEqual(Calc.calculate("cos(180))"), -1.0)
        pass
    
    def testFunction_degreeInSin(self):
        Calc = Calculator()
        self.assertEqual(Calc.calculate("floor(sin(180)))"), 0.0)
        pass
    
    def testFunction_pow(self):
        Calc = Calculator()
        self.assertEqual(Calc.calculate("pow(2, 10)"), 1024.0)
        pass
    
    def testFunction_log(self):
        Calc = Calculator()
        self.assertEqual(Calc.calculate("log(2, 1024)"), 10.0)
        pass
    
    def testFunction_min(self):
        Calc = Calculator()
        self.assertEqual(Calc.calculate("min(2, 3,4,5,6)"), 2.0)
        pass
    
    def testFunction_max(self):
        Calc = Calculator()
        self.assertEqual(Calc.calculate("max(2, 3,4,5,6)"), 6.0)
        pass
    
    def testFunction_sum(self):
        Calc = Calculator()
        self.assertEqual(Calc.calculate("sum(1, 2,3,4,5,6,7,8,9,10)"), 55.0)
        pass
    
    def testFunction_avg(self):
        Calc = Calculator()
        self.assertEqual(Calc.calculate("avg(2,4,6,8,10,12,14,16,18,20, 22)"), 12.0)
        pass
    
    def testFunction_variables(self):
        Calc = Calculator()
        self.assertEqual(Calc.calculate("key1=2+2*2"), 6.0)
        self.assertEqual(Calc.calculate("key2=3+3*3"), 12.0)
        self.assertEqual(Calc.calculate("key3=key1+key2"), 18.0)
        self.assertEqual(Calc.calculate("key3 + max(key1, key2)"), 30.0)
        pass
    
    
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testPlusMinus']
    unittest.main()