'''
#comprahension
li = [1,2,3,4,5]
#op = [2,4,6,8,10]
res =[]
for ele in li:
    res.append(ele*2)
print(res)

#but for one line code we can do this using list comprehension
print([ele*2 for ele in li])


li = [1,2,3,4,5]
#op = even numbers from the list
res = []
for ele in li:
    if ele % 2 == 0:
        res.append(ele)
print(res)

print([ele for ele in li if ele % 2 == 0])
print(tuple(ele for ele in li if ele % 2 == 0))
print({ele for ele in li if ele % 2 == 0})


lis1 = ['a', 'b', 'c']
#op = "a b c"
charac = " "
for ch in lis1:
    charac = charac + ch + " "
print(charac)
    
#using join
print(" ".join(lis1))
'''

n = 4

# #1) Pyramid Pattern
# res = " "
# for i in range(1,n+1):
#     print(" " * (n-i) + "* "*i)
    

# reverse pyramid pattern
# for i in range(n,0,-1):
#     print(" " * (n-i) + "* "*i)
    
    

#diammond pattern
# for i in range(1,n+1):
#     print(" "*(n-i) + "* "*i)

# for i in range(n-1, 0, -1):
#     print(" "* (n-i) + "* "*i)
    

#5) Palindrome pattern