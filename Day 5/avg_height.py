
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
    total_height = total_height + height

no_students = 0
for student in student_heights:
    no_students += 1

average_heights = round(total_height/no_students)
print(average_heights)

    




