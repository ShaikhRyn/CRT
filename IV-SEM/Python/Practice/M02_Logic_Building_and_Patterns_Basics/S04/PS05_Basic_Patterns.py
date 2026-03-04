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


#5) Repeated number pattern
n = int(input())
for i in range(1, n+1):
    for j in range(1, i+1):
        print(i, end=" ")
    print()



#6) Alphabet triangle
n = int(input())
for i in range(n):
    for j in range(i+1):
        print(chr(65+j),end="")
    print()



#7) FLoyd triangle
n = 5
var = 0
for i in range(1, n+1):
    var +=1
    for j in range(i):
        print(var+j, end=" ")
    print()

    '''

#8) hollow square
n = 4
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1:
            print("*", end="")
        else:
            if j==0 or j==n-1:
                print("*", end="")
            
            print()