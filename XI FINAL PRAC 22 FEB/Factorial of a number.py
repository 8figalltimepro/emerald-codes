num = int(input("Enter the number: "))
res = 1
for i in range(1, num + 1):
    res = res * i
print(f"Factorial of {num} is: {res}")