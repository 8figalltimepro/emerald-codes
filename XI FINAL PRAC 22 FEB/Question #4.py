# Calculate the Grade of the student:


def Marks(Eng, math, sci, comp, marks=0, Grade='Pass'):
    marks = int(Eng + math +sci + comp)
    Percentage = (marks / 400) * 100
    if Percentage <= 33:
         Grade = "F"
    elif Percentage <= 50:
        Grade = "D"
    elif Percentage <= 60:
        Grade = "C"
    elif Percentage <= 75:
        Grade = "B"
    elif Percentage <= 90:
        Grade = "A"
    elif Percentage <= 100:
        Grade = "S"
    else:
        print("Invalid Marks Given")
    print(f'''
     REPORT CARD
        
Maths           |   {math} 
Science         |   {sci}  
English         |   {Eng}
Computer        |   {comp}
---------------------------
Total Marks     |   {marks}
Percentage      |   {Percentage}

 ___________
|   Grade   |
|     {Grade}     |
|___________|
    ''')
mathm = int(input("Math Marks: "))
engm = int(input("English Marks: "))
sciem = int(input("Science Marks: "))
compm = int(input("Computer Marks: "))
Marks(engm, mathm, sciem, compm)
