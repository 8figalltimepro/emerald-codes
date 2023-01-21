

l1 = [100, 200, 300, 400]
l2 = [10, 20, 30]


l1.extend(l2)
print(l1)

l1.append(90)
print(l1)

l1 = [100, 200, 300, 400]
l1.insert(2, "Python")
print(l1)

l1 = [100, 200, 300, 400, 100]
print(l1.count(100))
l1 = [100, 200, 300, 400, 100]

l1.pop(1)
print(l1)
l1 = [100, 200, 300, 400, 100]

l1.remove(300)
print(l1)
l1 = [100, 200, 300, 400, 100]

del l1[2]
print(l1)


