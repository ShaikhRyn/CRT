n = int(input())
for i in range(1,n+1,2):
    print(i)


n = int(input())
first = 0
second = 1
for i in range(n):
    print(first, end=" ")
    c=first+second
    first,second = second,c
