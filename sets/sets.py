# create a set of integer type
student_id = {112, 114, 116, 118, 115}
print('Student ID:', student_id)

# create a set of string type
vowel_letters = {'a', 'e', 'i', 'o', 'u'}
print('Vowel Letters:', vowel_letters)

# create a set of mixed data types
mixed_set = {'Hello', 101, -2, 'Bye'}
print('Set of mixed data types:', mixed_set)


# Add Items to a Set in Python
numbers = {21, 34, 54, 41, 30}
print('Initial Set:', numbers)

# Using add() method
numbers.add(32)

print('Updated Set:', numbers)


# Update Python Set
companies = {'Lacoste', 'Ralph Lauren'}
tech_companies = {'apple', 'google', 'apple'}

# Using update() method
companies.update(tech_companies)
print(companies)


# Remove an Element from Set
languages = {'Swift', 'Java', 'Python'}

print('Initial Set:',languages)

# remove 'Java' from a set
removedValue = languages.discard('Java')

print('Set after remove():', languages)


# Iterate Over a Set in Python
fruits = {'Apple', 'peach', 'Mango'}

# For loop to access elements
for fruit in fruits:
    print(fruit)
