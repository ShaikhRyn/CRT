'''SET:
1. use {} to create a set
2. set does not allow duplicate values
3. set is unindexed
4. set is heterogeneous
5. set is mutable
6. set is unordered

s = {True, 10, 10, 20,15, 10e-5,1, 1+1j}
print(s, type(s))
print(s[3])
'''
B = {6, 7, 8, 9, 10}
A = {1, 2, 3, 4, 5}
A.add(6)   #for single element
A.update([7, 8, 9])   #for multiple elements
A.remove(3)   #removes the specified element from the set
A.pop()   #removes and returns an arbitrary element from the set
A.discard(4)   #removes the specified element from the set if it is present
A.clear()   #removes all elements from the set


print(A)

print(A-B)   #difference of A and B
print(A|B)   #union of A and B