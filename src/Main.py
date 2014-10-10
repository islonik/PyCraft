import sys

from calculator import Calculator as calc
from optparse   import OptionParser

parser      = OptionParser()
calculator  = calc.Calculator()

while(True == True) :
    expression = input("Enter your expression: ")
    if(expression == "exit") :
        break 
    print(calculator.calculate(expression))
