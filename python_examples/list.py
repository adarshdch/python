# Creating a list
names = []

# Overriding list
names = ["Adarsh", "Rohit"]

# Accessing List Item by index
names[0] = "Advika"

# Accessing Last Element
print(names[-1] == "Rohit")

# Print current list of items
print("Valid list items" if names == ["Advika", "Rohit"] else "Invalid")

# Append new item to the list
names.append("Suresh")

# Check if item exists / contains - Parenthesis is necessary
print(("Suresh" in names) == True)

# Length of the list
print(len(names) == 3)

# Remove list item
del names[1]

# Slice to ignore 1st elements
print(names[1:])

# Slice to ignore 1st and last
print(names[1:-1])
