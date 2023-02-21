# Write a program that reads a line and prints its frequency chart like...
# ...... lower case
# ... upper case
#........ alphabets
#........ digits

msg = input("Enter the line: ")
upper_case = ""
lower_case = ""
alphabets = ""
digits = ""
for i in msg:
    if i.isupper() == True:
        upper_case += i
    elif i.islower() == True:
        lower_case += i
    if i.isalpha() == True:
        alphabets += i
    elif i.isdigit() == True:
        digits += i
    else:
        continue
print(f'''
Frequency Chart

Upper Case Letters:  {len(upper_case)}
Lower Case Letters:  {len(lower_case)}
Alphabets:           {len(alphabets)}
Digits:              {len(digits)}
''')