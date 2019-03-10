# packing the unpacked disctionary

def myfunpack(**argsdict):
    print type(argsdict)
    for key in argsdict:
        print ("%s = %s" %(key,argsdict[key]))


# unpacked dictionary

def myfununpack(name,age,city):
    print name
    print age
    print city
    myfunpack(name='Nilesh',age='40',city='Pune')
     

myDict = {'name':'Nilesh','age':'40','city':'Pune'}
          
myfununpack(**myDict)

           

