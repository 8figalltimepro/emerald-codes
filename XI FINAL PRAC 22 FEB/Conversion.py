str = "school"
str2 = ""
count = 0
for i in str:
    count += 1
    if count%2 == 0:
        str2 += f"{i.upper()}"
    else:
        str2 += f"{i}"

print(str2)