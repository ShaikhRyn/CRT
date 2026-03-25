# PS04_Strings.py - Comprehensive Guide to Strings in Python
# This file teaches you everything about strings in Python with examples

# ===========================================
# 1. INTRODUCTION TO STRINGS
# ===========================================
# Strings in Python are sequences of characters enclosed in quotes.
# They are immutable (cannot be changed after creation).

# Creating strings
single_quote = 'Hello World'  # Single quotes
double_quote = "Hello World"  # Double quotes
triple_quote = '''This is a
multi-line string'''  # Triple quotes for multi-line

print("=== Basic String Creation ===")
print(f"Single quote: {single_quote}")
print(f"Double quote: {double_quote}")
print(f"Triple quote: {triple_quote}")

# ===========================================
# 2. STRING OPERATIONS
# ===========================================

# Concatenation (joining strings)
str1 = "Hello"
str2 = "World"
concatenated = str1 + " " + str2
print(f"\n=== Concatenation ===")
print(f"str1 + ' ' + str2 = {concatenated}")

# Repetition
repeated = "Ha" * 3
print(f"\n=== Repetition ===")
print(f"'Ha' * 3 = {repeated}")

# Indexing (accessing individual characters)
text = "Python"
print(f"\n=== Indexing ===")
print(f"text = '{text}'")
print(f"text[0] = '{text[0]}'")  # First character
print(f"text[-1] = '{text[-1]}'")  # Last character

# Slicing (getting substrings)
print(f"\n=== Slicing ===")
print(f"text[0:3] = '{text[0:3]}'")  # Characters 0 to 2
print(f"text[2:] = '{text[2:]}'")   # From index 2 to end
print(f"text[:4] = '{text[:4]}'")   # From start to index 3
print(f"text[::-1] = '{text[::-1]}'")  # Reverse string

# ===========================================
# 3. STRING METHODS (Built-in String Functions)
# ===========================================
# String methods are called on string objects: string.method()

sample_text = "  Hello, World! Welcome to Python programming.  "
print(f"\n=== String Methods Demo ===")
print(f"Sample text: '{sample_text}'")

# Case conversion
print(f"\n--- Case Conversion ---")
print(f"upper(): '{sample_text.upper()}'")
print(f"lower(): '{sample_text.lower()}'")
print(f"title(): '{sample_text.title()}'")
print(f"capitalize(): '{sample_text.capitalize()}'")
print(f"swapcase(): '{sample_text.swapcase()}'")

# Whitespace handling
print(f"\n--- Whitespace Handling ---")
print(f"strip(): '{sample_text.strip()}'")  # Remove leading/trailing whitespace
print(f"lstrip(): '{sample_text.lstrip()}'")  # Remove leading whitespace
print(f"rstrip(): '{sample_text.rstrip()}'")  # Remove trailing whitespace

# Searching and finding
search_text = "Python programming is fun and Python is powerful"
print(f"\n--- Searching and Finding ---")
print(f"Search text: '{search_text}'")
print(f"find('Python'): {search_text.find('Python')}")  # First occurrence
print(f"rfind('Python'): {search_text.rfind('Python')}")  # Last occurrence
print(f"index('Python'): {search_text.index('Python')}")  # First occurrence (raises error if not found)
print(f"count('Python'): {search_text.count('Python')}")  # Count occurrences
print(f"startswith('Python'): {search_text.startswith('Python')}")
print(f"endswith('powerful'): {search_text.endswith('powerful')}")

# Replacing
print(f"\n--- Replacing ---")
print(f"replace('Python', 'Java'): '{search_text.replace('Python', 'Java')}'")
print(f"replace('Python', 'Java', 1): '{search_text.replace('Python', 'Java', 1)}'")  # Replace only first occurrence

# Splitting and joining
sentence = "Python,is,a,programming,language"
print(f"\n--- Splitting and Joining ---")
print(f"Original: '{sentence}'")
split_list = sentence.split(',')
print(f"split(','): {split_list}")
joined = '-'.join(split_list)
print(f"'-'.join(split_list): '{joined}'")

# Checking content
test_string = "Python123"
print(f"\n--- Content Checking ---")
print(f"Test string: '{test_string}'")
print(f"isalpha(): {test_string.isalpha()}")  # All alphabetic?
print(f"isdigit(): {test_string.isdigit()}")  # All digits?
print(f"isalnum(): {test_string.isalnum()}")  # All alphanumeric?
print(f"isspace(): {test_string.isspace()}")  # All whitespace?
print(f"isupper(): {test_string.isupper()}")  # All uppercase?
print(f"islower(): {test_string.islower()}")  # All lowercase?
print(f"istitle(): {test_string.istitle()}")  # Title case?

# Padding and alignment
short_text = "Hi"
print(f"\n--- Padding and Alignment ---")
print(f"Original: '{short_text}'")
print(f"center(10): '{short_text.center(10)}'")
print(f"ljust(10): '{short_text.ljust(10)}'")
print(f"rjust(10): '{short_text.rjust(10)}'")
print(f"zfill(5): '{short_text.zfill(5)}'")

# ===========================================
# 4. BUILT-IN FUNCTIONS THAT WORK WITH STRINGS
# ===========================================

# len() - Get string length
text = "Hello World"
print(f"\n=== Built-in Functions ===")
print(f"len('{text}'): {len(text)}")

# str() - Convert to string
number = 42
boolean = True
print(f"str({number}): '{str(number)}'")
print(f"str({boolean}): '{str(boolean)}'")

# ord() and chr() - Character codes
char = 'A'
code = 65
print(f"ord('{char}'): {ord(char)}")
print(f"chr({code}): '{chr(code)}'")

# min() and max() - Min/max character
word = "Python"
print(f"min('{word}'): '{min(word)}'")
print(f"max('{word}'): '{max(word)}'")

# sorted() - Sort characters
print(f"sorted('{word}'): {sorted(word)}")

# enumerate() - Get index and character pairs
print(f"list(enumerate('{word}')): {list(enumerate(word))}")

# ===========================================
# 5. STRING FORMATTING
# ===========================================

# Old-style formatting (% operator)
name = "Alice"
age = 25
print(f"\n=== String Formatting ===")
print("Old-style: 'Hello, %s! You are %d years old.' % (name, age)")
print("Hello, %s! You are %d years old." % (name, age))

# str.format() method
print(f"\nstr.format(): \"Hello, {{}}! You are {{}} years old.\".format(name, age)")
print("Hello, {}! You are {} years old.".format(name, age))

# Named placeholders
print(f"\nNamed: 'Hello, {name}! You are {age} years old.'")
print("Hello, {name}! You are {age} years old.".format(name=name, age=age))

# f-strings (Python 3.6+)
print(f"\nf-string: f'Hello, {name}! You are {age} years old.'")
print(f"Hello, {name}! You are {age} years old.")

# ===========================================
# 6. ADVANCED STRING OPERATIONS
# ===========================================

# String interpolation with variables
pi = 3.14159
print(f"\n=== Advanced Operations ===")
print(f"Pi value: {pi:.2f}")  # Format to 2 decimal places

# Raw strings (ignore escape sequences)
raw_string = r"C:\Users\Documents\file.txt"
print(f"Raw string: {raw_string}")

# Unicode strings
unicode_str = "Hello 世界 🌍"
print(f"Unicode string: {unicode_str}")
print(f"Length: {len(unicode_str)}")

# String encoding/decoding
text = "Hello World"
encoded = text.encode('utf-8')
decoded = encoded.decode('utf-8')
print(f"Original: {text}")
print(f"Encoded: {encoded}")
print(f"Decoded: {decoded}")

# ===========================================
# 7. COMMON STRING PATTERNS AND EXAMPLES
# ===========================================

print(f"\n=== Common Patterns ===")

# Palindrome check
def is_palindrome(s):
    s = s.lower().replace(' ', '')
    return s == s[::-1]

print(f"is_palindrome('racecar'): {is_palindrome('racecar')}")
print(f"is_palindrome('hello'): {is_palindrome('hello')}")

# Word count
sentence = "This is a sample sentence for word counting."
word_count = len(sentence.split())
print(f"Word count: {word_count}")

# Character frequency
from collections import Counter
text = "hello world"
freq = Counter(text)
print(f"Character frequency in '{text}': {dict(freq)}")

# String reversal (multiple ways)
original = "Python"
print(f"\nString reversal methods for '{original}':")
print(f"Slice: {original[::-1]}")
print(f"reversed(): {''.join(reversed(original))}")
print(f"Loop: {''.join(original[i] for i in range(len(original)-1, -1, -1))}")

# ===========================================
# 8. STRING IMMUTABILITY DEMONSTRATION
# ===========================================
# Strings are immutable - you can't change them directly

immutable_str = "Hello"
print(f"\n=== String Immutability ===")
print(f"Original: {immutable_str}")

# This creates a new string, doesn't modify the original
new_str = immutable_str.replace('H', 'J')
print(f"After replace: original='{immutable_str}', new='{new_str}'")

# Trying to modify a character directly will raise an error
try:
    immutable_str[0] = 'J'  # This will fail
except TypeError as e:
    print(f"Error when trying to modify: {e}")

print("\n=== End of String Tutorial ===")
print("Strings are fundamental in Python programming!")
print("Practice these concepts to master string manipulation.")