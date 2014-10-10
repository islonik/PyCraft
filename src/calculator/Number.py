'''
Created on 01.08.2011

@author: Lipatov
'''
class Number(object):
    iValue = 0;
    
    def __init__(self):
        self.iValue = 0;
    
    def getValue(self) :
        return self.iValue
    
    def setValue(self, value):
        self.iValue = float(value)
        
    def invertValue(self):
        self.iValue = - self.iValue
