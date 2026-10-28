students = []
subjects = ["English","Math","Hindi","Physics","DBMS"]


n = int(input("Enter number of students: "))

for i in range(n):
    print("Enter Details of Student")
    name = input("Enter Name of student: ")
    roll_no = int(input("Enter Roll number: "))
    marks = []

    for subject in subjects:
        while True:
            try:
                mark = float(input("Enter your marks in " +subject+ ": "))
                if 0<=mark<=100:
                   marks.append(mark)
                   break
                else:
                   print("Invalid! Number,Pls Enter a number b/w 0-100")
            except ValueError:
                print("Invalid! Number,Pls Enter a Valid number")
                


    student = {
                "name":name,
                "roll":roll_no,
                "marks":marks
            }
    students.append(student)

    total = sum(marks)
    percentage = (total/500)*100
    average = total/5
    highest = max(marks)
    lowest = min(marks)

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80 :
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 40: 
        grade = "D"
    else:
        grade = "F"


    if all (mark >= 40 for mark in marks):
        result = "Pass"
    else:
        result = "Fail"


    count = 0
    for mark in marks:
        if mark>= 75:
            count+=1


    if percentage >= 85 and result == "Pass":
        merit = "Eligible"
    else:
        merit = "Not Eligible"
            

    print("Display Student reports")
    print("Name : ",name)
    print("Roll no :",roll_no)
    print("Marks : ",marks)
    print("Total marks is ",total)
    print("Percentage is : ",percentage,"%")
    print("Average is : ",round(average,2))
    print("Grade:",grade)
    print("Result : ",result)
    print("Subjects with marks 75 or above : ",count)
    print("Merit Certificate :",merit)


    for j in range(5):
        if marks[j] == highest:
             print("Highest marks is : ",marks[j],"in",subjects[j])
        if marks[j] == lowest:
            print("Lowest Marks is : ",marks[j], "in ", subjects[j])        
    
   

print("Details of Student")
for student in students:
    print(student)


topper = max(students,key = lambda student: (sum(student["marks"])/500)*100)
topper_percentage = (sum(topper["marks"])/500)*100
print("Class topper : ",topper["name"])
print("Roll no:  ",topper["roll"])
print("Percentage : " ,round(topper_percentage,2),"%")


total_percentage = 0
for student in students:
    total_marks = sum(student["marks"])
    percentage = (total_marks/500)*100
    total_percentage+=percentage
class_average = total_percentage/len(students)

print("Class Average is : ",round(class_average,2))

passed = 0
failed = 0
for student in students:
    if all(mark >= 40 for mark in student["marks"]):
        passed+=1
    else:
        failed+=1
print("Total Passed Students: ",passed)
print("Total Failed Students: ",failed)

