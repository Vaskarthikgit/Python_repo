# List data type and methods (Mutable)
'''
append(x)	    Adds an item x to the end of the list
extend(iter)	Adds all elements from an iterable (e.g., list, tuple) to the end
insert(i, x)	Inserts item x at index i
remove(x)	    Removes the first occurrence of item x
pop([i])	    Removes and returns item at index i (default is last item)
clear()	        Removes all items from the list
index(x)	    Returns the index of the first occurrence of item x
count(x)	    Returns the number of times item x appears
sort()	        Sorts the list in ascending order (can take key and reverse arguments)
reverse()	    Reverses the list in place
copy()	        Returns a shallow copy of the list
'''

lst=[1,2,3,4,5,3]
lst.insert(1,8)
lst.append(44)
lst2=[99,88,7,"Karthik"]
lst.extend(lst2)
#print(lst)
#lst.sort()
print(lst)
lst.remove(88)
print(lst)
print(lst.index(44))
print(lst.count(99))
'''
lst.reverse()
print(lst)
lst.sort(reverse=True)
print(lst)
'''
print(lst)
lst.pop(7)

lst3=lst.copy()
lst3.append("abc")
print(lst)
print(lst3)
print(len(lst))
# for i in lst:
#  print(i)

lst=['a','b','n']
print("-".join(lst))


#=====================================================================================
# Tuple data type and methods (Immutable)
'''
count(x)	Returns the number of times x appears in the tuple
index(x)	Returns the index of the first occurrence of x
'''
tup=(1,9,2,6,3,7,6,"Karthik")
tup=(1,9,2,6,3,7,6,"VK")

print(tup)
for i in tup:
     print(i)

print(tup.count(3))
print(tup.index(3))
print(len(tup))

#=====================================================================================
# Set data type and methods (Mutable)
'''
add(x)	            Adds element x to the set
remove(x)	        Removes element x; raises error if not found
discard(x)	        Removes element x; does not raise error if not found
pop()	            Removes and returns an arbitrary element
clear()	            Removes all elements from the set
copy()	            Returns a shallow copy of the set
update(iterable)	Adds elements from another iterable (e.g., list, set)
'''
my_set={11,22,3,"Kart"}
my_set2={8,9}

print("=====Set=======")
my_set.add(4)
my_set.remove(3)
my_set.discard(33)
print(my_set)
v=my_set.pop()
print("pop",v)
my_set.update(my_set2)
print(my_set)

#=====================================================================================
# Dictionary data type and methods 
'''
.get(key)	Returns value for key, or None if missing
.keys()	Returns all keys
.values()	Returns all values
.items()	Returns all key-value pairs
.pop(key)	Removes key and returns its value
.clear()	Removes all items
'''
dic={
     "name":"Karthik",
     "age":35,
     "city":"Salem"
}

for i in dic.keys():
     print(i)

for i in dic.values():
     print(i)

for key, value in dic.items():
     print(key,"-",value)

print(dic.get("name"))
#dic.pop("name")
print(dic)
print(dic.popitem())
print(dic)
print(len(dic))
