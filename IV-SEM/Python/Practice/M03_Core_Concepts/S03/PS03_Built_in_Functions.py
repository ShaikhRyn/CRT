'''
1)Find largest number (using max() function) --> usiing a list
2) check palindrome (using reversed() & join())  -->  joins a llist of strings into a single string
3) count even numbers (using filter())  --> filters elementsbased on a conditon 
4) remove duplicates (suing set())  --> creates a set from a list, which automatically removes duplicates
5) sum of digits (suing sum())
6) sort words alphabetically (using sorted())  --> returns a sorted list of the specified iterable
7) find common elements (using set())
8) index with value (using enumerate())  --> adds a counter to an iterable and returns it as an enumerate object
9) pair two lists (using zip())  --> combines multiple iterable elem-wise
10) find the seconf largtest number (using sorted())  --> returns a sorted list of the specified iterable
'''


#1)Find largest number (using max() function) 
numbers = [10, 20, 5, 15, 30]
largest = max(numbers)
print("Largest number:", largest)


#2) check palindrome 
word = "Riyan"
reversed_word = ''.join(reversed(word))
if word == reversed_word:
    print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")


#3) count even numbers (using filter()) 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))  
print("Even numbers:", even_numbers)


#4) remove duplicates (suing set()) 
numbers = [1, 2, 3, 4, 5, 2, 3, 1]
unique_numbers = set(numbers)
print("Unique numbers:", unique_numbers)

