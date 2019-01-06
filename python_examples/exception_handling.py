# Exception Handling
dictionary = {
    "name": "Adarsh",
    "id": 100
}

try:
    print("Inside try/except block:")
    print(dictionary["invalid_key"])
except KeyError:            # Handle KeyError
    print("Error while retrieving by invalid key")
except TypeError as error:  # Handle TypeError
    print(error)			# Error details
except Exception:           # Generic Handler
    print("Unknown error occured")
