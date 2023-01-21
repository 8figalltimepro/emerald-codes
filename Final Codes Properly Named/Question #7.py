# WAP to input 6 num from users, store these number in a tuple and print the max and min and  sum and mean
# of all the elements from the tuple

base = ()

for i in range(1, 7):
    n = int(input(f"Input Number {i}: "))
    n = (n, )
    base += n
print(base)
print(max(base))
print(min(base))
print(sum(base))
print((sum(base)/6))