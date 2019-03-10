Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
Boys = {'Tim': 18,'Charlie':12,'Robert':25}
Girls = {'Tiffany':22}
temp = 'Today is Saturday'

# Creation of dictionary using dict constructor

Kids = dict(Tim = 18, Charlie = 12, Tiffany = 22, Robert = 25, name = 'Boys')
print Kids

for i in Girls:
    print ("||".join((i,str(Girls[i]))))

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
print "printable string:%s" % str (Dict)       


'''
for i in Dict.keys():
    if i in Boys:
        print ("key %s with value %d is prent in Boys dict" % (i,Boys[i]))
    elif i in Girls:
        print ("key %s is prent in Girls dict" % i)
    else:
        print ("key %s is wrong key" % i)


sv = Boys.values()
print sk
print sv
'''
'''
si = Boys.items()
print si

for k in si:
    for val in k:
        print val
    print ("*"*40)

sk = Boys.keys()
sk.sort()
for p in sk:
    print(":".join((p,str(Dict[p]))))
'''
