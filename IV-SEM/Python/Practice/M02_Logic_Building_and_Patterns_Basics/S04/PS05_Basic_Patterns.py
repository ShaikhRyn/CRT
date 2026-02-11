'''
#1) square pattern
n = int(input())
for i in range(n):
    for j in range(n):
        print("*", end="")
    print()


'''
'''
#2) lower right triangle
n = int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end="")
    print()



#3) Inverted traingle
n = int(input())
for i in range(n):
    for j in range(i,n):
        print("*", end="")
    print()


#4) number triangle
n = int(input())
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

'''
#5)