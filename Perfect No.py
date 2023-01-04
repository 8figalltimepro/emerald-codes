n = int(input("Enter a Number: "))
j = 1
s = 0
while j < n:
    if (n%j) == 0:
        s = s + j
    j = j + 1
if s == n:
    print("It is a perfect no")
else:
    print("Not a perfect no")

