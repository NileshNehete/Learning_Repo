# Enter tree numbers and print the biggest and lowest number

num1 = input("Enter First Number :")
num2 = input("Enter Second Number :")
num3 = input("Enter Third Number :")

if (( num1 > num2 ) and ( num1 > num3 )):
    print ("First number %d is the biggest number" %num1)
    if ( num2 > num3 ):
        print ("Third number %d is the lowest number" %num3)
    else:
        print ("Second number %d is the lowest number" %num2)
        
if (( num2 > num1 ) and ( num2 > num3 )):
    print ("Second number %d is the biggest number" %num2)
    if ( num1 > num3 ):
        print ("Third number %d is the lowest number" %num3)
    else:
        print ("First number %d is the lowest number" %num1)

if (( num3 > num2 ) and ( num3 > num1 )):
    print ("Third number %d is the biggest number" %num3)
    if ( num2 > num1 ):
        print ("First number %d is the lowest number" %num1)
    else:
        print ("Second number %d is the lowest number" %num2)

print ( "="* 20 )

        
int = 0

while ( int < 10 ):
    print int
    int = int + 1


