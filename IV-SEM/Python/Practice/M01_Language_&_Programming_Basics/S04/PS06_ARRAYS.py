'''
Arrays:
1. List ==> Built-in Dta strucutre
    1.use [] to create a list
    2. list is mutable 
    3. list is hetrogenous
    4. list is indexed
    5. list is ordered
    6. list allows duplicate values

2. Array using array module 
3. array using numpy module 
'''
'''
lis = [1,12.5,True,1,"Python",2+5j]
print(lis,type(lis))

#no of elements len()
counter = 0
for _ in (lis):
    counter += 1
print(counter)
print(len(lis))

#update
lis[2] = False
print(lis)

#Adding element ==> append()
lis.append("SUIIII")
print(lis)

# adding element ==> insert()
lis.insert(3, "MEHSII")
print(lis)

lis.insert(20, 200) #this inserts at the last
print(lis)

lis.extend([7,10,9])   # this appends multiple values
print(lis)

# Remove element from list
lis.pop()
lis.pop(1) # removing from the start
lis.pop(-1) # removes from the last 
print(lis)

#removing an element for which we dont know the index
lis.remove(200)
print(lis)

lis.clear()
print(lis)


#copy()
l1 = [1,2,3]
l2 = l1         #this shows the changes made to original list(deep copy)
l3 = l1.copy()  #just copies it(shallow copy)
print(l1, l2, l3)

l1.append(4)
print(l1, l2, l3)

'''

from array import array
arr = array('i', [10,20,30])    #'i' is a type code ,depicts int
print(arr, len(arr))

arr.append(14,32)