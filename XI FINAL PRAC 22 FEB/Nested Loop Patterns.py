for i in range(1, 5):
    print("*" * i)
for i in range(1, 5):
    for j in range(1, (i+1)):
        print(j, end="")
    print("")
for i in range(1, 5):
    print(str(i) * i, end="\n")
