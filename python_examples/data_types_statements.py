
# String data type
name = "Adarsh"

# Boolean data type
trueVariable = True
falseVariable = False

# None data type
noneVariable = None

# Data Type Conversion
age = "34"
print(int(age) == 34)
print(float(age) == 34)

# Format Function
print ("Hello {0}".format(name))

# Format Shorthand
print(f"Hello {name}")

# Type Hinting
def add_numbers(a: int, b: int) -> int:
    return a  + b

print(add_numbers(4, 5) == 9)

# Other Data Types
# complex
# long	# Only in python2
# bytes and bytearray

# Set / FrozenSet
data_set = set([3, 2, 3, 1, 4])
print(data_set)
print(data_set == {1, 2, 3, 4})

print(frozenset([3, 2, 3, 1, 4]) == {1, 2, 3, 4})
