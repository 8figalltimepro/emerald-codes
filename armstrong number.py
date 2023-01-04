# armstrong num 153 = (1^3) + (5^3) + (3^3) = 1 + 125 + 27 = 153



org = int(input("Enter a Number: "))
num = org
sum = 0
while num > 0:
    rem = num % 10
    cube = rem * rem * rem
    sum += cube
    num = num//10
if org == sum:
    print("Armstrong no: True")
else:
    print("Armstrong no: False")
