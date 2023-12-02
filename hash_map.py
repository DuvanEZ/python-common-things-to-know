# Create an empty dictionary (HashMap)
myMap = {}

# Add key-value pairs to the dictionary
myMap["alice"] = 88
myMap["bob"] = 77

# Print the dictionary and its length
print(myMap)
print(len(myMap))

# Update the value for the key "alice"
myMap["alice"] = 80
print(myMap["alice"])

# Check if "alice" is a key in the dictionary
print("alice" in myMap)

# Remove the key-value pair with key "alice"
myMap.pop("alice")

# Check again if "alice" is a key in the dictionary
print("alice" in myMap)

# Create a dictionary with initial key-value pairs
myMap = { "alice": 90, "bob": 70 }
print(myMap)

# Create a dictionary using dictionary comprehension
myMap = { i: 2*i for i in range(3) }
print(myMap)

# Loop through the dictionary and print each key and value
myMap = { "alice": 90, "bob": 70 }
for key in myMap:
  print(key, myMap[key])

# Loop through the dictionary and print each value
for val in myMap.values():
  print(val)

# Loop through the dictionary and print each key-value pair
for key, val in myMap.items():
  print(key, val)