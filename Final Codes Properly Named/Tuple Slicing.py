t1 = ('myt Book', [1,2,3], 'z', (3,4,6), 'Desk', 50)
print(t1[2:3])
print(t1[1:2])
print(t1[3][1])

# Tuple Addition
x = (1, 3, 4, 6)
y = (5, 7, 8, 9)
z = x + y
print(z)
print(x[1:3] + (5, 6))

# Error
# print(x[1:3] + x[0])
# Error will be brought up as you cant add tuple and Integer

print(x[-3:-1] + (x[0],))

# Tuple Mult
print(x * 2)
print(x[1:3] * x[3])


