# Ask the user how many grades they want to enter

grades_number = int (input ("How many grades you want to enter?: "))
grades = []

for i in range (grades_number):
    grade_value = float(input (f"Enter grade {i}: "))
    grades.append(grade_value)

total = 0
for grade in (grades):
    total = total + grade

print(total/grades_number)