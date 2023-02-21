list = input("List of Value: ").split(",")
listtemp = []
length = 0
if len(list)%2 == 0:
    length = len(list)
else:
    length = len(list) - 1
for i in range(0, length, 2):
    listtemp.append(list[i+1])
    listtemp.append(list[i])
print(listtemp)