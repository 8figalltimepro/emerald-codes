LST = [10, 20, 30, 10, 40, 50, 60, 40, 50, 60, 40]
element = int(input("Enter the element you want to get the frequency of: "))
count = 0
for i in range(len(LST)):
    if element == LST[i]:
        count += 1
if count != 0:
    print(f"{element} Frequency = {count}")
else:
    print(f"{element} is not present") 
