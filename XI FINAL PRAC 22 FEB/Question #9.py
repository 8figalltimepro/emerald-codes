# WAP to input total number of  SEction and Stream Name in 11 class and Display all informayin on the Output screen like this
Class = "XI"
d = dict()
for i in range(1, 4):
    a = input("Enter Section: ")
    b = input("Enter Stream: ")
    d[a] = f"{b}"
print(f'''
Class       Section     Stream

{Class}        A        {d["A"]}
{Class}        B        {d["B"]}
{Class}        C        {d["C"]}
''')

