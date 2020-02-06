# Assign variables
pets = ["dog", "cat", "bunny", "snake", "rat", "20yo"]
message = 'Hello'
separator = "+-------------------------------------------+"
indent = "\t"

# Itterate through list
for petnum,pet in enumerate(pets):
    print (indent+str(petnum)+" : "+pet)

# Create a separator
print (separator)

for letter in message:
    print (indent+letter)

# Create a separator
print (separator)

for num in range(0,5,1):
    print (indent+str(num))