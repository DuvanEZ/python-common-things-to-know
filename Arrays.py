# Create an empty list (array)
myList = []

# Add elements to the list
myList.append(88)  # Equivalent to "alice" = 88 in the dictionary
myList.append(77)  # Equivalent to "bob" = 77

# Print the list and its length
print(myList)
print(len(myList))

# Update an element at a specific index (assuming we want to update the first element)
myList[0] = 80
print(myList[0])

# Check if a value exists in the list
print(80 in myList)

# Remove an element by value (removing 80)
myList.remove(80)

# Check again if the value exists in the list
print(80 in myList)

# Create a list with initial elements
myList = [90, 70]
print(myList)

# Create a list using list comprehension
myList = [2*i for i in range(3)]
print(myList)

# Loop through the list and print each value
for val in myList:
  print(val)

# Loop through the list and print each value with its index
for index, val in enumerate(myList):
  print(index, val)