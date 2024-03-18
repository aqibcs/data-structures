# Creating an empty dictionary named myMap
myMap = {}
# Adding a key-value pair ('alice', 88) to the dictionary
myMap["alice"] = 88
myMap["jhon"] = 77
print(myMap)
print(len(myMap))

# Updating the value associated with the key 'alice' to 80
myMap["alice"] = 80
print(myMap["alice"])

# Checking if 'alice' is a key in the dictionary
print("alice" in myMap)
myMap.pop("alice")
print("alice" in myMap)

# Reinitializing myMap with two key-value pairs directly
myMap = {"alice": 90, "bob": 70}
print(myMap)

# Using dictionary comprehension to create a dictionary
# Keys are integers from 0 to 2, and values are twice the keys
myMap = {i: 2 * i for i in range(3)}
print(myMap)

# Looping through the dictionary by keys and printing key-value pairs
myMap = {"alice": 90, "bob": 70}
for key in myMap:
    print(key, myMap[key])

# Looping through the dictionary by values and printing them
for val in myMap.values():
    print(val)

# Looping through the dictionary by key-value pairs and printing them
for key, val in myMap.items():
    print(key, val)
