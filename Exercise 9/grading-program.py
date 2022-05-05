#Exercise - Grading Program 


student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades={}

#TODO-2: Write your code below to add the grades to student_grades.👇
for i in student_scores.items():
    if i[1]>=91 and i[1]<100:
        student_grades[i[0]]='Outstanding'
    elif i[1]>=81 and i[1]<90:
        student_grades[i[0]]='Exceeds Expectations'
    elif i[1]>=71 and i[1]<80:
        student_grades[i[0]]='Acceptable'
    else:
        student_grades[i[0]]='Fail'
    

# 🚨 Don't change the code below 👇
print(student_grades)
