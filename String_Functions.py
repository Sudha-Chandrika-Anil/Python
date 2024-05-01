a = input("Enter a String")
# Length of string
print(len(a))

# Find a letter in the given string
e = input("Enter letter to be searched")
print(a.find(e))

# Capitalize the string
print(a.capitalize())

# String in upper case
print(a.upper())

# String in lower case
print(a.lower())

# Whether input is in digits
print(a.isdigit())

# Whether input is of alphabets
print(a.isalpha())

# Count a letter in the given string
e = input("Enter letter to be counted")
print(a.count(e))

# Replace a letter in the given string
r = input("Enter letter to be searched")
print(a.replace(e,r))

print(a*2)
