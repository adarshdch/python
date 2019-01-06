# Creating dictionary
student = {
    "name": "Adarsh",
    "id": 12,
    "feedback": None
}

# Updating dictionary
student["name"] = "Mohit"	

# Accessing the dictionary by key safely
print(student.get("last_name", "Unknown") == "Unknown")

# Get the list of keys
student.keys() == ["name", "id", "feedback"]

# Get the list of values
student.values() == ["Mohit", 12, None]

# Removing the key/value
del student["name"]

# KeyError
# student["notfound"]