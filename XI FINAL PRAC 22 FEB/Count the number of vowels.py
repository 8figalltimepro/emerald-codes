str = "Pineapple"
vowels = "eioua"
count = 0
for i in str:
    for l in vowels:
        if i == l:
            count += 1

print("No of vowels: ", count)