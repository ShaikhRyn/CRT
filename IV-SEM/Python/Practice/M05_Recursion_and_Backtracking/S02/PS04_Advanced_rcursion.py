# def digital_root(n):
# while n >= 10: 
#     s = 0
#     while n > 0:
#         s += n % 10   
#         n // = 10

# print(digital_root(245))


#check if array is sorted using Recursion
def is_sorted(arr, n):
    if n == 1 or n == 0:
        return True
    if arr[n-1] < arr[n-2]:
        return False
    return is_sorted(arr, n-1)

# Example usage
arr = [1, 2, 3, 4, 5]
print(is_sorted(arr, len(arr)))  # Output: True

arr = [1, 3, 2, 4, 5]
print(is_sorted(arr, len(arr)))  # Output: False