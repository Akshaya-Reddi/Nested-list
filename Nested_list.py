n = int(input("Enter range:"))
list_main = []
grade = []

for _ in range(n):
    name = input("Enter name:")
    score = float(input("enter score:"))
    grade.append(score)
    list_main.append([name, score])

unique_grades = sorted(list(set(grade)))

if len(unique_grades) >= 2:
    second_lowest_grade = unique_grades[1]
    students_with_second_lowest = [student[0] for student in list_main if student[1] == second_lowest_grade]
    students_with_second_lowest.sort()
    for name in students_with_second_lowest:
        print(name)
else:
    print("Not enough unique grades to determine the second lowest.")
