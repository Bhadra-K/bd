student={}
n=int(input("No of students :"))
for i in range(n):
    rollno=input("Enter rollno:")
    name=input("Enter name:")
    student[rollno]=name
print("Student Details:",student)

rollno=input("Enter the rollno:")
name=input("Enter new name:")
student[rollno]=name
print("Updated student details:",student)

rollno=input("Enter the student to remove:")
del student[rollno]
print(student)

rollno=input("Enter the rollno:")
if rollno in student:
    print(f"Student with rollno {rollno} is {student[rollno]}")
else:
    print(f"Student not found")
print(f"Total no of students:", len(student))
