
# Functions
print("Print function example")

name  = input("Enter name: ")
print("You have input: " + name)

def welcome(firstName, lastName = "Kumar", *args):
    print(f"{firstName} {lastName}")
    for arg in args:
        print(arg)

welcome("Adarsh", "Reddy", "Age: 34", "Hobby: Many")

def get_key_values(**key_val_args):
    print("Reading Argument Keys/Values:")
    for key, val in key_val_args.items():
        print(f"{key} = {val}")

get_key_values(name= "Vikash", age= 30, feedback= "Very Good")

# Nested Function

def parent():
    parent_var = "Parent Variable"
    print("Inside parent:")
    def child():
        child_var = "Child Variable"
        print("Inside Child:")
        print("Child can access: " + parent_var)
        print("Child can access: " + child_var)
    print("Parent can access: " + parent_var)
    print("Parent can not access child variable")
    child()

parent()

# Lambda Function

# Function without lambda
def double_without_lambda(x):
    return x * 2

print()
# Function with lambda
double_with_lambda  = lambda x: x * 2

print(double_without_lambda(2) == 4)
print(double_with_lambda(2) == 4)
