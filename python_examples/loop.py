
names = ["Adarsh", "Advika", "Kunika"]

#--------------------------------------------------------------
# For Loop
#--------------------------------------------------------------

# Looping through the list
for name in names:
    print (name)

# Looping through range
x = 0
for index in range(10):
    x += 10
    if index == 5:
        print("Index is 5 so continuing...")
        continue
    if index == 7:
        print("Breaking the loop")
        break
    print("10 * {0} = {1}".format(index + 1, x))

# Range with starting and end index
range(5, 10) == [5, 6, 7, 8 ,9]

# Range with increament counter
range(5, 10, 2) == [5, 7, 9]

#--------------------------------------------------------------
# While Loop
#--------------------------------------------------------------

x = 0
while True:
    x += 1
    if x > 5:
        break
    print(x)

