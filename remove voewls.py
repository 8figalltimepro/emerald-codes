str = "Pineapple"
vowels = "eioua"
str2 = " "
for i in range(len(str)):
    if str[i] not in "aeiou":
        str2 = str2 + str[i]
print("original string", str)
print("Changed string", str2)