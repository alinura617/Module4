exam_one = int(input("Input exam grade one: "))
exam_two = int(input("Input exam grade two: "))  # Corrected int() for exam_two
exam_three = int(input("Input exam grade three: "))  # Corrected int() for exam_three

grades = [exam_one, exam_two, exam_three]  # Corrected ',' between exam_one, exam_two, exam_three
sum_grades = 0  # Changed variable name to avoid confusion with grades
for grade in grades:  # Changed variable name 'grade' in the loop
    sum_grades = sum_grades + grade  # Changed variable name 'grade' to 'sum_grades'

avg = sum_grades / len(grades)  # Corrected variable name 'grdes' to 'grades'

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90:  # Added a colon at the end of the condition
    letter_grade = "B"
elif avg >= 70 and avg < 80:  # Changed '>' to '>=' in the condition
    letter_grade = "C"
elif avg >= 60 and avg < 70:  # Changed '<=' to '>=' in the condition
    letter_grade = "D"
else:  # Removed the unnecessary ':' after 'elif'
    letter_grade = "F"

for grade in grades:
    print("Exam: " + str(grade))

print("Average: " + str(avg))  # Moved this outside the loop to print the average only once

print("Grade: " + letter_grade)

if letter_grade == "F":  # Corrected the comparison operator 'is' to '=='
    print("Student is failing.")
else:
    print("Student is passing.")
