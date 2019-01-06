# Open file in append mode
f = open("deleteme.txt", "w")

# Write to the file
f.write("first line")

# Close file handle. It is mandatory
f.close()

# Open file in read mode
f = open("deleteme.txt", "r")

# Read file line by line
for line in f.readlines():
    print(line)

# Close file handle
f.close()

