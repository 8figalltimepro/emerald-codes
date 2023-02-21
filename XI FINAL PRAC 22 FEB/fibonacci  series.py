count = int(input("Count: "))
m = 0
x = 0
y = 1
z = 1
print(x, y, end=" ")
while m < (count-2):
    m += 1
    print(z, end=' ')
    x = y
    y = z
    z = x + y
