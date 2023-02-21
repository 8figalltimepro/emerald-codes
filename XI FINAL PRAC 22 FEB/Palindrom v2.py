num = int(input("Number: "))
num = str(num)
bool = True
length = len(num)
for i in range(0, len(num)):
    if num[i] == num[(length-1)-i]:
        continue
    else:
        bool = False
if bool == True:
    print("Palindrome")
else:
    print("No")
