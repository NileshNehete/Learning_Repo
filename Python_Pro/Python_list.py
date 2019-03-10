bikes = ["Hero","Bajaj","Honda","Suzuki","Yamaha"]
print "First record : %s" % bikes[0]
print "Last record : %s" % bikes[-1]

# Loop through List
'''
for i in bikes:
    print i
'''
# Check if Item exist

if "Bajaj" in bikes:
    print ("Yes ! Bajaj is present in List.")

# List length

print len(bikes)

# append the record at the end of the list.

bikes.append("Trumph")
print ("Value Trumph is appended.")
print bikes

# insert adds the record at specified position.

print ("Values Enfield, Banana and Fruit are adding.")
bikes.insert(2,"Enfield")
bikes.insert(3,"Banana")
bikes.insert(4,"Fruit")

print bikes

# remove deletes the record.

print ("Value Fruit is removing.")
bikes.remove("Fruit")
print bikes

# pop deletes the record at specified position. also gives option to save in var before deleting.
# pop() removed last item.
print ("Remoing Value Banana using Pop and assigning to pop_var.")
pop_var = bikes.pop(3)
print ("Value %s at position 3 is poped." % pop_var)
print bikes

# del delete specified index or complete list id index is not specified.

del bikes[2]
print bikes

fruits =["Banana","Apple","Grapes","Orange","WaterMelon"]
#print fruits
#fruits.clear() # clear() is not present in this version of python
#print fruits # this will give error as fruits list is deleted.


'''
Method 	        Description
append()	Adds an element at the end of the list
clear()	        Removes all the elements from the list
copy()	        Returns a copy of the list
count()	        Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	        Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	        Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	        Sorts the list
sort([fun])
'''

print fruits[2:]






