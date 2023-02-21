# 1) break statement will come out of the loop completely


for val in "String":
    if val == "i":
        break
    print(val, end="")
print(" Hi")


# observe in this function the break will come out of the loop completely making the else statement not run when the i is iterated

for val in "String":
    if val == "i":
        break
    print(val, end="")
else:
    print("Hi")

# 2) continue statement
print("\n")
for val in "String":
    if val == "i":
        continue
    print(val, end="")

# 3) pass statement
for i in "String":
    pass
