import sys
sys.path.append('c:\Python_Pro\Modules')
from printoutput import *

ITERATOR=0

def add (num1,num2):
    sum = num1 + num2
    printAdd(sum)

def sub (num1,num2):
    if (num1<num2):
        printError()
    else:
        sub = num1 - num2
        printSub(sub)

def mult (num1,num2):
    mult = num1 * num2
    printMult(mult)
    
def divi(num1,num2):
    div = num1 / num2
    rem = num1 % num2
    printDivi(div,rem)
           
'''       
if(__name__ == '__main__'):
    add(5,4)
    sub(6,3)
    mult(4,3)
    divi(17,5)
'''

               
    
    
