# n = int(input())
# counter = 0
# while n > 0:
#     counter += 1
#     n //= 10
# print(counter)



# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in range(len(arr)):
#     if arr[i] % 2 == 0:
#         print(arr[i],end=" ")

# for ele in arr:
#     if ele % 2 == 0:
#         print(ele, end=" ")


# str = input()
# count = 0
# li = ["a", "e", "i" ,"o", "u"]
# arr =[]
# for i in range(len(str)):
#     if arr[i]


str = input()
count = 0
for ch in str:
    if ch in "aeiouAEIOU":
        count += 1
print(count)



