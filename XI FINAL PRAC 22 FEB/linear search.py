l1 = [100, 200, 300, 400, 600]
element = int(input("Enter the element you want to be searched: "))
for i in range(len(l1)):
    if element == l1[i]:
        print(f"Found {element} at index {i}")
        break
else:
    print(f"{element} not present")