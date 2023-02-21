str = "triathlon"
vowels = "eioua"
vcount = 0
str2 = ""
for i in range(len(str)):
    if str[i] not in "aeiou":
        str2 = str2 + str[i]
    else:
        vcount += 1
print("original string", str)
print("Changed string", str2)
print("Vowel Count: ", vcount)