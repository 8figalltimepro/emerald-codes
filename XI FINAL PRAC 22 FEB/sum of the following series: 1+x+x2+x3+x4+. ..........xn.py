print("input the value of x and n and print the sum of the following series: 1+x+xˆ2+xˆ3+xˆ4+. ..........xˆn")
x = int(input("Value of x: "))
n = int(input("Value of n: "))
sum = 0
for i in range(0, n+1):
    sum += (x**i)
print(sum)