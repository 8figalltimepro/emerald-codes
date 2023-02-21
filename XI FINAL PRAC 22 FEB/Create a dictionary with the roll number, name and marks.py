'''Create a dictionary with the roll number, name and
marks of n students in a class and display the names of students
who have scored marks above 75.
'''

n = int(input("number of students: "))
scorebook = {}
for i in range(1, n+1):
   roll_no = int(input("Roll No: "))
   name = input("Student Name: ")
   marks = int(input("Marks: "))
   scorebook[roll_no] = [name, marks]

print(scorebook)
topscorer = []
for i in scorebook:
   if scorebook[i][1] > 75:
      topscorer.append(scorebook[i][0])
topscorer = str(topscorer).strip("]").strip("[")
print(f"Student's name who get more than 75 marks: {topscorer}")
