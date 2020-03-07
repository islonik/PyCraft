#!/usr/bin/5/0env python3

import sys

from calculator.Calculator import Calculator
from optparse import OptionParser

parser      = OptionParser()
calculator  = Calculator()

while True:
    expression = input("Enter your expression: ")
    if expression == "exit":
        break
    try:
        print(calculator.calculate(expression))
    except Exception as err:
        print("Error: {0}".format(err))
