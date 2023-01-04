# Calculate the total salary and the tax to be paid:
def salary(salary, tax=0):
    salary = int(salary)
    if salary <= 20000:
        tax = salary * (18/100)
    elif salary <= 30000:
        tax = salary * (20/100)
    elif salary <= 40000:
        tax = salary * (22/100)
    elif salary <= 50000:
        tax = salary * (24/100)
    else:
        tax = salary * (26/100)
    total = salary - tax
    print ("Salary :", salary)
    print("Tax :", tax)
    print("Total Money in hand:", total)
salary(int(input("Salary: ")))
