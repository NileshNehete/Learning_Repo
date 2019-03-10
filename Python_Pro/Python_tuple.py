#Once a tuple is created, you cannot change its values. Tuples are unchangeable.

bikes = ("Hero","Bajaj","Honda","Suzuki","Yamaha")

print (bikes)
print (bikes[2])
'''
for i in bikes:
    print (i)

# check if Bajaj is present in tuple and show the index.
inc = 0
if "Bajaj" in bikes:
    for i in bikes:
        
        if i == "Bajaj":
            print ("Bajaj is present in the tuple at index %d" % inc)
        inc = inc + 1

if "Honda" in bikes:
    print ("HOnda is present at index %d" %(bikes.index("Honda")))

'''
tup1 = ('Robert', 'Carlos','1965','Terminator 1995', 'Actor','Florida');
tup2 = (1,2,3,4,5,6,7);
print  tup1[0]
print  tup2[1:4]

#Packing and Unpacking
x = ("Guru99", 20, "Education")    # tuple packing
(company, emp, profile) = x    # tuple unpacking
print company
print emp
print profile

#Comparing tuples
#case 1
a=(5,6)
b=(1,4)
if (a>b):print "a is bigger"
else: print "b is bigger"

#case 2
a=(5,6)
b=(5,4)
if (a>b):print "a is bigger"
else: print "b is bigger"

#case 3
a=(5,6)
b=(6,4)
if (a>b):print "a is bigger"
else: print "b is bigger"

#Tuples and dictionary
a = {'x':100, 'y':200}
b = a.items()
print b 

#Slicing of Tuple
x = ("a", "b","c", "d", "e")
print x[2:4]

'''
Method	Description	Syntax
copy()	Copy the entire dictionary to new dictionary	dict.copy()
update()	Update a dictionary by adding a new entry or a key-value pair to an
existing entry or by deleting an existing entry.	Dict.update([other])
items()	Returns a list of tuple pairs (Keys, Value) in the dictionary.	dictionary.items()
sort()	You can sort the elements	dictionary.sort()
len()	Gives the number of pairs in the dictionary.	len(dict)
cmp()	Compare values and keys of two dictionaries	cmp(dict1, dict2)
Str()	Make a dictionary into a printable string format	Str(dict)
'''
