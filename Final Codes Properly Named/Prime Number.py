num = int(input("Enter a Number: "))
fact = 0
for i in range(1, num + 1):
    if (num % i == 0) and fact < 3:
        fact += 1
    elif (num % i == 0) and fact > 2:
        break
if fact == 2:
    print(f'Initial number:{num}\nPrime Number: True')
elif fact != 2:
    print(f'Initial number: {num}\nPrime Number: False')
else:
    print(f'Error')
