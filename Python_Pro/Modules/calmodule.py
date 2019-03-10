ITERATOR=0

def add (num1,num2):
    sum = num1 + num2
    print ("Addition of two numbers: %d" % sum)
    print ("=" *50)

def sub (num1,num2):
    if (num1<num2):
        print ("Sorry!! Enter First number greater than Second!!")
    else:
        sub = num1 - num2
        print ("Substraction of two numbers: %d" % sub)
        print ("=" *50)

def mult (num1,num2):
    mult = num1 * num2
    print ("Multiplication of two numbers: %d" % mult)
    print ("=" *50)

def divi(num1,num2):
    div = num1 / num2
    rem = num1 % num2
    print ("Division of two numbers: %d and reminder :%d" % (div,rem))
    print ("=" *50)
           
'''        
if(__name__ == '__main__'):
    add(5,4)
    sub(6,3)
    mult(4,3)
    divi(17,5)

  '''  
               
    
    
