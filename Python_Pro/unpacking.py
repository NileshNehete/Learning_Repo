def display (a,b,c):
     print ( str(a) +","+ str(b) +","+ str(c))

myList = [4,6,9]
myDict = {'name':'Nilesh','age':'40','city':'Pune'}
display(*myList)


def sum (*args):
    sum = 0
    for i in range(0,len(args)):
        sum = sum + args[i]
    print sum

sum(1,2,3,4,5)
sum(10,20)


# A Python program to demonstrate both packing and 
# unpacking.


def fun2(a,b,c):
    print ("Arguments after change :" + a+b+c )
    


def fun3(*args):

    print("Arguments before change:")
    print args
    
    args = list(args)
    args[0] = 'I'
    args[1] = 'Love'

    fun2(*args)
   

fun3('Hello','Beautiful','World!')
