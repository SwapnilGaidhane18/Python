c = "hello"
print(c)

#Concept of indexing
print(c[4]) # Positive Indexing
print(c[-5])  # Negative Indexing

#Slicing
a = 'swapnil'
print(a[0:4]) # last index is not included
print(a[:4])
print(a[2:])
print(a[:])
print(a[2:7:2])
print(a[2:4:-1]) # with positive indexing negative skiping not allowed [ampty string]
print(a[-5:-1:2])
print(a[::-1]) # reverse of string 
print(a[-1:-5:-1])

# How to Edit and Delete string
b = "hello world"
print(b) 

# Strings are a immutable data type, But you can reassign it, Not able to change in exiting strings
b = "hello guys.."
print(b) 

del b # Deletion
x = "yash"

# You cann't delete a specific character or portion from existing strings,
# Because it makes changes in strings, which is allowed in string because strings are immutable data type
# del x[0] (error)

# String functions
st = "kolkata"
print(len(st))
print(max(st))
print(min(st))
print(sorted(st))

y = "it is raining today"
print(y.capitalize())
print(y.title())
print(y.upper())
print(y.lower())
print(y.swapcase())
print(y.count("i"))

print(y.find("r"))
print(y.index("n")) # findi() and index() are almost same, small difference is when you pass
# a character in both these 2 functions
# So, find() returns -1 and index() returns an error

print("my name is swapnil!".startswith("my")) # returns boolen value
print("my name is swapnil!".endswith("my") )  # returns boolen value

# format function (very usefull function): agar tumhe string me kuch value add karna hai
# but vo aapko abhi nahi pata future me pata chalega is situation me tum format() function use kar sakte ho
# For Example: 
print("hello, my name is {}, my age is {}".format("swapnil",19))
print("hello, my name is {1}, my age is {0}".format("swapnil",19))
print("hello, my name is {name}, my age is {age}".format(name = "swapnil", age = 19))

# isalnum/isalpha/isdecimal/isdigit/isidentifier
print("FLAT20".isalnum())
print("FLAT20&".isalnum())

print("FLAT20".isalpha())






