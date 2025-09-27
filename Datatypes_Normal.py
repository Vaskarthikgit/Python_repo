# String data type and methods

# Case Conversion 
text = "hello world"
print(text.upper())      # HELLO WORLD
print(text.capitalize()) # Hello world
print(text.title())      # Hello World
print(text.swapcase())   # HELLO WORLD → hello world

# Alignment & Padding 
text = "cat"
print(text.center(10, "-"))  # ---cat----
print(text.ljust(10, "."))   # cat.......
print(text.rjust(10, "."))   # .......cat
print(text.zfill(5))         # 00cat

# Searching & Counting
text = "banana"
print(text.find("na"))   # 2
print(text.rfind("na"))  # 4
print(text.count("a"))   # 3

# Validation Checks
text = "Python3"
print(text.isalnum())    # True
print(text.isalpha())    # False (contains a digit)
print("123".isdigit())   # True
print("   ".isspace())   # True

# Modification & Splitting
text = "  hello world  "
print(text.strip())      # "hello world"
print(text.replace("world", "Python"))  # "  hello Python  "
print(text.split())      # ['hello', 'world']

# Joining & Formatting
words = ["apple", "banana", "cherry"]
print(", ".join(words))  # apple, banana, cherry

name = "Alice"
age = 30
print("Name: {}, Age: {}".format(name, age))  # Name: Alice, Age: 30
print(f"Name: {name}, Age: {age}")  

# Search a string
text = "Hello, welcome to Python!"
search = "Python"

if search in text:
    print("Found!")
else:
    print("Not found.")

str="Hello Karthik"
print(str[2:12:1])
print(str[2:12:2])


