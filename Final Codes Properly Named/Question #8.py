#WAP a pyhton program to input any twpo tuples & swap their values
a = tuple(input("Input Tuple 1: "))
b = tuple(input("Input Tuple 2: "))
a = b + a
b = a[len(b):]
print(b)
a = a[0:len(b)]
print(a)
