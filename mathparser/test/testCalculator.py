"""
Created on 02.08.2011

@author: Nikita Lipatov
"""
import unittest

from calculator import Calculator


class CalculatorTest(unittest.TestCase):

    def testPlus(self):
        calc = Calculator.Calculator()
        self.assertEqual(calc.calculate("2 + 3"), 5.0)
        pass

    def testMinus(self):
        calc = Calculator.Calculator()
        self.assertEqual(calc.calculate("2-3"), -1.0)
        pass

    def testMultiplePluses(self):
        calc = Calculator.Calculator()
        self.assertEqual(calc.calculate("2+2+2"), 6.0)
        pass

    def testMultipleMinuses(self):
        calc = Calculator.Calculator()
        self.assertEqual(calc.calculate("12-22-50"), -60.0)
        pass

    def testMultiplication(self):
        calc = Calculator.Calculator()
        self.assertEqual(calc.calculate("12*2"), 24.0)
        pass

    def testDivision(self):
        calc = Calculator.Calculator()
        self.assertEqual(calc.calculate("12/2"), 6.0)
        pass

    def testMultipleMultiplication(self):
        calc = Calculator.Calculator()
        self.assertEqual(calc.calculate("12*2*10"), 240.0)
        pass

    def testMultipleDivision(self):
        calc = Calculator.Calculator()
        self.assertEqual(calc.calculate("12/2/3"), 2.0)
        pass

    def testBrackets(self):
        calc = Calculator.Calculator()
        self.assertEqual(calc.calculate("(2 + 2) * 2"), 8.0)
        pass

    def testDegree(self):
        calc = Calculator.Calculator()
        self.assertEqual(calc.calculate("(4 - 2)^4"), 16.0)
        pass

    def testModulusWithZero(self):
        calc = Calculator.Calculator()
        self.assertEqual(calc.calculate("6%3"), 0.0)
        pass

    def testDivisionByZero(self):
        calc = Calculator.Calculator()
        self.assertRaises(BaseException, calc.calculate, "6/0")
        pass

    def testModulesByZero(self):
        calc = Calculator.Calculator()
        self.assertRaises(BaseException, calc.calculate, "6%0")
        pass

    def testBracketsUnbalance(self):
        calc = Calculator.Calculator()
        self.assertRaises(BaseException, calc.calculate, "(2 + 2 * 2")
        pass

    def testFunction_abs(self):
        calc = Calculator.Calculator()
        self.assertEqual(calc.calculate("abs(-5)"), 5.0)
        pass

    def testFunction_log10(self):
        calc = Calculator.Calculator()
        self.assertEqual(calc.calculate("log10(100)"), 2.0)
        pass

    def testFunction_sqrt(self):
        calc = Calculator.Calculator()
        self.assertEqual(calc.calculate("sqrt(144)"), 12.0)
        pass

    def testFunction_acos(self):
        calc = Calculator.Calculator()
        self.assertEqual(calc.calculate("ceil(acos(6.0))"), 2.0)
        pass

    def testFunction_asin(self):
        calc = Calculator.Calculator()
        self.assertEqual(calc.calculate("asin(0)"), 0.0)
        pass

    def testFunction_atan(self):
        calc = Calculator.Calculator()
        self.assertEqual(calc.calculate("atan(0)"), 0.0)
        pass

    def testFunction_cos(self):
        calc = Calculator.Calculator()
        self.assertEqual(calc.calculate("cos(0)"), 1.0)
        pass

    def testFunction_sin(self):
        calc = Calculator.Calculator()
        self.assertEqual(calc.calculate("sin(0)"), 0.0)
        pass

    def testFunction_tan(self):
        calc = Calculator.Calculator()
        self.assertEqual(calc.calculate("tan(0)"), 0.0)
        pass

    def testFunction_ceil(self):
        calc = Calculator.Calculator()
        self.assertEqual(calc.calculate("ceil(0.5)"), 1.0)
        pass

    def testFunction_floor(self):
        calc = Calculator.Calculator()
        self.assertEqual(calc.calculate("floor(0.5)"), 0.0)
        pass

    def testFunction_sinInCeil(self):
        calc = Calculator.Calculator()
        self.assertEqual(calc.calculate("ceil(sin(0.5))"), 1.0)
        pass

    def testFunction_degreeInCos(self):
        calc = Calculator.Calculator()
        self.assertEqual(calc.calculate("cos(180))"), -1.0)
        pass

    def testFunction_degreeInSin(self):
        calc = Calculator.Calculator()
        self.assertEqual(calc.calculate("floor(sin(180)))"), 0.0)
        pass

    def testFunction_pow(self):
        calc = Calculator.Calculator()
        self.assertEqual(calc.calculate("pow(2, 10)"), 1024.0)
        pass

    def testFunction_log(self):
        calc = Calculator.Calculator()
        self.assertEqual(calc.calculate("log(2, 1024)"), 10.0)
        pass

    def testFunction_min(self):
        calc = Calculator.Calculator()
        self.assertEqual(calc.calculate("min(2, 3,4,5,6)"), 2.0)
        pass

    def testFunction_max(self):
        calc = Calculator.Calculator()
        self.assertEqual(calc.calculate("max(2, 3,4,5,6)"), 6.0)
        pass

    def testFunction_sum(self):
        calc = Calculator.Calculator()
        self.assertEqual(calc.calculate("sum(1, 2,3,4,5,6,7,8,9,10)"), 55.0)
        pass

    def testFunction_avg(self):
        calc = Calculator.Calculator()
        self.assertEqual(calc.calculate("avg(2,4,6,8,10,12,14,16,18,20, 22)"), 12.0)
        pass

    def testFunction_variables(self):
        calc = Calculator.Calculator()
        self.assertEqual(calc.calculate("key1=2+2*2"), 6.0)
        self.assertEqual(calc.calculate("key2=3+3*3"), 12.0)
        self.assertEqual(calc.calculate("key3=key1+key2"), 18.0)
        self.assertEqual(calc.calculate("key3 + max(key1, key2)"), 30.0)
        pass


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testPlusMinus']
    unittest.main()
