# Strings are similar to arrays
string = "abc"
print(string[0:2])

# But they are immutable
# string[0] = "A"

# So this creates a new string
string += "def"
print(string)

# Valid numeric strings can be converted
print(int(123) + int("123"))

# And numbers can be converted to strings
print(str(123) + str(123))

# In rare cases you may need the ASCII values of a char
print(ord("a"))
print(ord("b"))

# Combine a list of string (with an empty string delimetor)
strings = ["ab", "cd", "ef"]
print("".join(strings))
