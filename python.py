#Students List(List)
students = ["Bhadra","Alice","Bob"]
print(students)

#Student Location(Tuple)
college_location = (11.588, 75.7804) #Kozhikode coordinates
print(college_location)

#Clubs(Set)
clubs = {"Dance","Music","Art","Drama","Art"}
print(clubs)

#Student Records(Dictionary)
student_records = { 
    "Bhadra" : { "roll.no": 101, "marks": 98, "Sci" : 88 },
    "Alice" : { "roll.no": 102, "marks": 67, "Sci" : 45 },
    "Bob " : { "roll.no": 103, "marks": 72, "Sci" : 60 } 
    }
print(student_records)


#ACCESS FROM LIST
print(students[0])

#ADD VALUE TO LIST
students.append("Jack")
print(students)
students.insert(2,"Mary")
print(students)

#SORT
students.sort()
print(students)

#LENGTH_COUNT
print(len(students))