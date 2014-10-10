'''
Created on 29.07.2011

@author: Lipatov
'''

import calculator.Number as num
import calculator.Variables as vars
import math 

class Calculator(object):
    '''
        Enums
    '''
    TYPE_NONE        = 1
    TYPE_DELIMITER   = 2
    TYPE_NUMBER      = 3
    TYPE_FUNCTION    = 4
    TYPE_VARIABLE    = 5
    
    TYPE_DEGREE = 1
    TYPE_GRADUS = 2
    typeTangentUnit = TYPE_DEGREE 
    
    '''
        Variables
    '''
    idString    = 0 
    storString  = ""
    storToken   = ""
    typeToken   = ""
    
    def __init__(self):
        self.idString    = 0 
        self.storString  = ""
        self.storToken   = ""
        self.typeToken   = ""
        self.variables   = vars.Variables()
     
    def calculate(self, expression) :
        if len(expression) > 1024 :
            raise "Too much expression"
        self.storString = expression.lower().replace(" ", "");
        self.idString = 0;
        self.__getToken();
        if self.storToken == "" :
            raise "Not found tokens!"
        result = num.Number()
        self.__firstStepParsing(result)
        return result.getValue()
    
    def __firstStepParsing(self, number) :
        token = ""
        tempType = ""
        if (self.typeToken == self.TYPE_VARIABLE) :
            token = self.storToken
            tempType = self.TYPE_VARIABLE
            if (self.variables.contains(token) == False) :
                self.variables.add(token, 0.0)
            self.__getToken()
            if (self.storToken != "=") :
                self.__putBack()
                if (self.variables.contains(token) == False) :
                    self.variables.remove(token)
                self.storToken = token
                self.typeToken = tempType
            else :
                self.__getToken()
                self.__secondStepParsing(number)
                self.variables.add(token, number.getValue())
                return;
        self.__secondStepParsing(number)
    
    def __putBack(self) :
        i = 0
        while(i < len(self.storToken)) :
            self.idString -= 1
            i += 1
        
    def __findVar(self, key) :
        if (self.variables.contains(key) == False) :
            raise BaseException("Variable does not found!")
        return self.variables.get(key)
    
    def __secondStepParsing(self, number) :
        self.__thirdStepParsing(number);
        token = self.storToken
        while (token == "+" or token == "-") :
            self.__getToken();
            temp = num.Number()
            self.__thirdStepParsing(temp);
            if(token == "-") :
                number.setValue(number.getValue() - temp.getValue());
            elif(token == "+") :
                number.setValue(number.getValue() + temp.getValue());
            token = self.storToken
    
    def __thirdStepParsing(self, number) :
        self.__fourthStepParsing(number);
        token = self.storToken
        while(token == "*" or token == "/" or token == "%") :
            self.__getToken()
            temp = num.Number()
            self.__fourthStepParsing(temp);
            if(token == "/") :
                if (temp.getValue() == 0.0) :
                    raise BaseException("Division by zero!")
                number.setValue(number.getValue() / temp.getValue())
                token = self.storToken
            elif(token == "%") :
                if (temp.getValue() == 0.0) :
                    raise BaseException("Division by zero!")
                number.setValue(number.getValue() % temp.getValue())
                token = self.storToken
            elif(token == "*") :
                number.setValue(number.getValue() * temp.getValue())
                token = self.storToken
            
            
    def __fourthStepParsing(self, number) :
        self.__fifthStepParsing(number);
        if (self.storToken == "^") :
            self.__getToken();
            temp = num.Number()
            self.__fourthStepParsing(temp);
            number.setValue(math.pow(number.getValue(), temp.getValue()));
    
    def __fifthStepParsing(self, number) :
        str = "";
        if ((self.typeToken == self.TYPE_DELIMITER) and 
            (self.storToken == "+" or self.storToken == "-")) :
            str = self.storToken;
            self.__getToken();
        self.__sixthStepParsing(number);
        if (str == "-") :
            number.invertValue();
            
    def __sixthStepParsing(self, number) :
        if (self.storToken == "(") :
            self.__getToken();
            self.__secondStepParsing(number);
            if (self.storToken != ")") :
                raise BaseException("Brackets unbalance");
            self.__getToken();
        else :
            self.__seventhStepParsing(number);
    
    def __seventhStepParsing(self, number) :
        if self.storToken == "e" :
            number.setValue(math.e)
            self.__getToken()
            return;
        elif(self.storToken == "pi") :
            number.setValue(math.pi)
            self.__getToken()
            return;
        else :
            self.__atom(number)
        
    def __atom(self, number) :
        if self.typeToken == self.TYPE_NUMBER :
            number.setValue(self.storToken)
            self.__getToken();
            return;
        elif self.typeToken == self.TYPE_FUNCTION :
            self.__functions(number);
            return;
        elif self.typeToken == self.TYPE_VARIABLE:
            number.setValue(self.__findVar(self.storToken));
            self.__getToken();
            return;
        else :
            number.setValue(0.0)
            raise BaseException("Syntax error")
        
    def __functions(self, number):
        functionName = self.storToken;
        if(functionName == "abs") :
            self.__oneParameterFunctions(functionName, number)
        elif(functionName == "log10") :
            self.__oneParameterFunctions(functionName, number)
        elif(functionName == "sqrt") :
            self.__oneParameterFunctions(functionName, number)
        elif(functionName == "acos") :
            self.__oneParameterFunctions(functionName, number)
        elif(functionName == "asin") :
            self.__oneParameterFunctions(functionName, number)
        elif(functionName == "atan") :
            self.__oneParameterFunctions(functionName, number) 
        elif(functionName == "cos") :
            self.__oneParameterFunctions(functionName, number)
        elif(functionName == "sin") :
            self.__oneParameterFunctions(functionName, number)
        elif(functionName == "tan") :
            self.__oneParameterFunctions(functionName, number)
        elif(functionName == "ceil") :
            self.__oneParameterFunctions(functionName, number)
        elif(functionName == "floor") :
            self.__oneParameterFunctions(functionName, number)
        elif(functionName == "pow") :
            self.__twoParameterFunctions(functionName, number)
        elif(functionName == "log") :
            self.__twoParameterFunctions(functionName, number)
        elif(functionName == "min") :
            self.__multiParameterFunctions(functionName, number)
        elif(functionName == "max") :
            self.__multiParameterFunctions(functionName, number)
        elif(functionName == "avg") :
            self.__multiParameterFunctions(functionName, number)
        elif(functionName == "sum") :
            self.__multiParameterFunctions(functionName, number)
            
            
    def __oneParameterFunctions(self, functionName, number) :
        self.__getToken();
        self.__sixthStepParsing(number);
        if(functionName == "abs") :
            number.setValue(math.fabs(number.getValue()))
        elif(functionName == "log10") :
            number.setValue(math.log10(number.getValue()))
        elif(functionName == "sqrt") :
            number.setValue(math.sqrt(number.getValue()))
        elif(functionName == "acos") :
            number.setValue(math.acos(self.__gradToRad(number.getValue())))
        elif(functionName == "asin") :
            number.setValue(math.asin(self.__gradToRad(number.getValue())))
        elif(functionName == "atan") :
            number.setValue(math.atan(self.__gradToRad(number.getValue()))) 
        elif(functionName == "cos") :
            number.setValue(math.cos(self.__gradToRad(number.getValue())))
        elif(functionName == "sin") :
            number.setValue(math.sin(self.__gradToRad(number.getValue())))
        elif(functionName == "tan") :
            number.setValue(math.tan(self.__gradToRad(number.getValue())))
        elif(functionName == "ceil") :
            number.setValue(math.ceil(number.getValue()))
        elif(functionName == "floor") :
            number.setValue(math.floor(number.getValue()))
        
    def __gradToRad(self, result) :
        if(self.typeTangentUnit == self.TYPE_DEGREE ) : 
                result = result * math.pi / 180;
        elif(self.typeTangentUnit ==  self.GRADUS ) :
                result = result * math.pi / 200;
        return result;
    
    def __twoParameterFunctions(self, functionName, number) : 
        self.__getToken();
        self.__getToken();
        self.__firstStepParsing(number);
        if (self.storToken == ",") :
            self.__getToken();
            temp = num.Number()
            self.__firstStepParsing(temp)
            if(functionName == "pow") :
                number.setValue(math.pow(number.getValue(), temp.getValue()));
            elif(functionName == "log") :
                number.setValue(math.log(temp.getValue()) / math.log(number.getValue()));
            if (self.storToken == ",") :
                raise BaseException("Syntax error");
            elif (self.storToken != ")") :
                raise "Brackets unbalance"
            self.__getToken()
        else :
            raise BaseException("Syntax error");
        
    def __multiParameterFunctions(self, functionName, number) :
        self.__getToken(); 
        self.__getToken(); 
        self.__firstStepParsing(number);
        i = 1;
        while(True == True) :
            if (self.storToken == ",") :
                self.__getToken();
                temp = num.Number()
                self.__firstStepParsing(temp);
                if (functionName == "min" and number.getValue() > temp.getValue()) : 
                    number.setValue(temp.getValue())
                elif (functionName == "max" and number.getValue() < temp.getValue()) : 
                    number.setValue(temp.getValue())
                elif (functionName == "avg") : 
                    number.setValue(number.getValue() + temp.getValue())
                    i +=1;
                elif (functionName == "sum") :
                    number.setValue(number.getValue() + temp.getValue())
                    i +=1;
            elif (self.storToken == ")") :
                if(functionName == "avg") :
                    number.setValue(number.getValue() / i);
                self.__getToken();
                break;
            else :
                raise BaseException("Brackets unbalance");
      
    def __getToken(self) :
        self.typeToken = self.TYPE_NONE;
        self.storToken = "";
        strBuffer      = "";
        
        if self.idString == len(self.storString) :
            return;
        
        if self._isDelimiter(self.storString[self.idString]) :
            strBuffer += self.storString[self.idString]
            self.idString += 1
            self.typeToken = self.TYPE_DELIMITER;
        elif self._isCharacter(self.storString[self.idString]) :
            lengthName = 0;
            while self._isDelimiter(self.storString[self.idString]) == False :
                strBuffer += self.storString[self.idString];
                self.idString += 1;
                if (self.idString >= len(self.storString)) : 
                    break;
                lengthName += 1;
                if(lengthName >= 32) :
                    raise BaseException("Expression is too long");
            if (self.idString < len(self.storString) and self.storString[self.idString] == '(') : 
                self.typeToken = self.TYPE_FUNCTION;
            else :
                self.typeToken = self.TYPE_VARIABLE;
        elif self._isDigit(self.storString[self.idString]) :
            while self._isDelimiter(self.storString[self.idString]) == False :
                strBuffer += self.storString[self.idString];
                self.idString += 1
                if self.idString >= len(self.storString) :
                    break;
            self.typeToken = self.TYPE_NUMBER;
        self.storToken = strBuffer;
    
    def _isDelimiter(self, char):
        if " +-/\\*%^=(),".find(char) != -1 :
            return True
        else :
            return False

    def _isDigit(self, idString):
        if "0123456789".find(idString) != -1 :
            return True
        else :
            return False
        
    def _isCharacter(self, char):
        if "abcdefghljklmnopqrstuvwxyz".find(char) != -1 :
            return True
        else : 
            return False