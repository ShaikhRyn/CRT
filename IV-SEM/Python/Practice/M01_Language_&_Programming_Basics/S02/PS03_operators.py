# x = 13 
# y = 5 
# print(x & y)
# print(x | y)
# print(x ^ y)
# print(x << 2)
# print(x >> 2)

#Memebership Operators 
#{in ,not in}

print("j" in "riyan")
print(100 in [10,20,30])

#identity operators 
#{is , is not }

x = 10 
y = 1
z = x
e = 12
print(x is y)
print(id(x))
del(x)
print(id(z))

print(id(y))

l1 = [1,2,3]
l2 = [1,2,3]
l2[1] = 4
print(l2)
print(l1 is l2)
print(id(l1),id(l2))
