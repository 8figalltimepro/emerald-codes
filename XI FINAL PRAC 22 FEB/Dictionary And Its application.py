# Dictionaries are:
# 1) Sequence Data Type [STructure database]
# 2) Unordered Collection of Types
# 3) Key : Value Pair
# 4) inside {}
# 5) Multiple Data Types
# 6) Key should be always unique
# 7) Key should be immutable []

# Methods to create a Dictionary
#1
d1 = {1 : 'One', 2 : 'Two', 3 : 'Three'}
print(d1)
#2 Using Builtin dict() fn
a = {1:2, 2:3, 3:4}
a = dict(a)
print(a)
#Creating a Dictionary by passing nested List as an arguement to dict() function
a = [[1, "One"], [2, "Two"]]
c = dict(a)
print(c)
# Method
D = {}
D[1] = "Hi"
D[2] = "Bro"
D[3] = "!!!"
print(D)

#Accessing Element in Dictionary
D = D
print(D[1])

# Traversing a Dictionary
D = D
for i in D:
    print(f"{i}: {D[i]}")

# Appending Values in Dictionary
D = D
D["Clay"] = "Water"
print(D)
D["Clay"] = "Oil"
print(D)
# Updating a Dictionary
d1 = {1: 10, 2: 10, 3: 30, 4: 30, 5: 30, 6: 30, 7: 30}
d2 = {1: 10, 2: 10, "new": "Old"}
d1.update(d2)
print(d1)



