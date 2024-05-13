student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for grade in student_scores:
  scores = student_scores[grade]
  if scores <= 70:
    student_grades[grade] = "Fail"
  elif scores >= 71 and scores <= 80:
    student_grades[grade] = "Acceptable"
  elif scores >= 81 and scores <= 90:
    student_grades[grade] = "Exceeds Expectations"
  else:
    student_grades[grade] = "Outstanding"


# 🚨 Don't change the code below 👇
print(student_grades)