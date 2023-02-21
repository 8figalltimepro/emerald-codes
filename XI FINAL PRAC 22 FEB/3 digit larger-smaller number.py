


n1 = int(input("Input Number 1: "))
n2 = int(input("Input Number 2: "))
n3 = int(input("Input Number 3: "))

if n1 > n2 and n1 > n3:
    print("Greater Number", n1)
elif n2 > n1 and n2 > n3:
    print("Greater Number", n2)
else:
    print("Greater Number", n3)