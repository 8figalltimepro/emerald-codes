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
        upper_case += f"{i}"
    elif i.islower() == True:
        lower_case += f"{i}"
    if i.isalpha() == True:
        alphabets += f"{i}"
    elif i.isdigit() == True:
        digits += f"{i}"
    else:
        continue
print(f'''
Frequency Chart

Upper Case Letters:  {len(upper_case)}
Lower Case Letters:  {len(lower_case)}
Alphabets:           {len(alphabets)}
Digits:              {len(digits)}
''')