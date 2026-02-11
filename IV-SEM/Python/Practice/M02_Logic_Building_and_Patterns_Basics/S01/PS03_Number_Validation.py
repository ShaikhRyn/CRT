# 1) write a python code for factorial of a number
n = int(input())
if n == 1 and n == 0:
    print (1) 

fact = 1
for i in range(1, n+1):
    fact *= i
print(fact)

# 2) write a python code to check whether a number is Armstrong or not 
# example: 153--->1,5,3--->(1 ** 3) + (5 ** 3) + (3 ** 3) == 153
'''
n = int(input())
var = str(n)
length = len(var)

total = 0
for d in var:
    total += int(d) ** length
if total == n:
    print("Armstrong")
else:
    print("Not Armstrong")


#3)prime numbers 
n = int(input())

count = 0
for i in range(1, n+1):
    if n % i == 0:
        count += 1

if count == 2:
    print("Yes")
else:
    print("No")


#4)print the prime numbers with a range
a = int(input())
b = int(input())

for n in range(a, b+1):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            print(n)
'''
'''
#5)monotonic of an array
arr = list(map(int, input().split()))

inc = sorted(arr)
dec = sorted(arr, reverse=True)
if arr == inc or arr == dec:
    print("Monotonic")
else:
    print("Not monotonic")

'''



#reverse an integer
# n = int(input())
# rev = 0
# while n:
#     rev = rev*10 + n%10
#     n//=10 
# print(rev)

#int to roman
num = int(input())

vals = [1000, 900, 500, 400, 100, 90, 50, 40,
        10, 9, 5, 4, 1]
rom = ["M", "CM", "D", "CD", "C", "XC", "L", "XL","X", "IX", "V", "IV", "I"]
res = ""
for i in range(len(vals)):
    while num >= vals[i]:
        res += rom[i]
        num -= vals[i]

print(res)


