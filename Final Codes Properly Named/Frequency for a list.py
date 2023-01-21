l1 = [100, 200, 200, 400, 100]
print(l1)
count = 0
element = int(input("Enter the Number: "))
for i in range(len(l1)):
    if element == l1[i]:
        count += 1
if count == 0:
    print("Element not found")
else:
    print(f"{element} appears {count} times")