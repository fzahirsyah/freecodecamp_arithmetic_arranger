from ast import Num
from posixpath import split
from signal import raise_signal
from traceback import print_tb
from webbrowser import get
from operator import truediv




def error_exception(Error_Number1,Error_Operator,Error_Number2):
    try:
        if Error_Operator != "+" and Error_Operator != "-":
           raise BaseException
    except:
        return "Error: Operator must be '+' or '-'."
    try:
        int(Error_Number1), int(Error_Number2)
    except:
        return "Error: Numbers must only contain digits."
    try:
        if len(Error_Number1) >4 or len(Error_Number2) >4:
            raise BaseException
    except:
        return "Error: Numbers cannot be more than four digits."
    return " "

def arithmatic_arranger(data, displayMode = False):

    indentation2 = "    "
    start = True
    line1 = line2 = line3 = line4 = ""
    try:
        if len(data) > 5:
            raise BaseException
    except:
            return "Error: Too many problems."

    for i in data:
        Split_Data = i.split()    
        number1 = Split_Data[0]
        operations = Split_Data[1]
        number2 = Split_Data[2]
        handling = error_exception(number1,operations,number2)
        
        if handling != " ":
            return handling
    
        indentation = max(len(number1),len(number2))
        num1 = int(number1)
        num2 = int(number2)

        if start == True:
            line1 += number1.rjust(indentation + 2) 
            line2 += operations+ ' ' + number2.rjust(indentation) 
            line3 += '-' * (indentation + 2) 
            if displayMode == True:
                if operations == '+':
                    line4 += str(num1 + num2).rjust(indentation + 2)
                else:
                    line4 += str(num1 - num2).rjust(indentation + 2)
            start = False
        else:
            start = False
            line1 += number1.rjust(indentation + 6) 
            line2 += operations.rjust(5)+ ' ' + number2.rjust(indentation) 
            line3 += indentation2 + '-' * (indentation + 2) 
            if displayMode == True:
                if operations == '+':
                    line4 += indentation2 + str(num1 + num2).rjust(indentation + 2)
                else:
                    line4 += indentation2 + str(num1 - num2).rjust(indentation + 2)
    if displayMode == True:
        return line1 + '\n' + line2 + '\n' + line3 + '\n' + line4
    return line1 + '\n' + line2 + '\n' + line3



    






