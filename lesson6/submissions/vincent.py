print(f"Here's a report about the Introduction to Magic course.")
students = ['michael', 'kate', 'scott', 'lauren', 'christopher']
print(f'The students in our class are: {students}')
grades = [100, 60, 55, 82, 90]
print(f'The grades on the mid-term exam are: {grades}')
best_grade = max(grades)
print(f'The best grade in the class is: {best_grade}')
worst_grade = min(grades)
print(f'The worst grade in the class is: {worst_grade}')
avg_grade = sum(grades)/len(grades)
print(f'The average grade in the class is: {avg_grade}')
print(f'A new student, Alice, just joined the class!')
students.append("ALice")
print(f'The students in our class are now: {students}')
final_grades = {
    'michael': 89,
    'kate': 100,
    'scott': 75,
    'lauren': 90,
    'christopher': 60,
    'alice': 84,
}
final_grades['michael']
print(f"Michael's final exam grade is: {final_grades['michael']}")
print(f"Kate's final exam grade is: {final_grades['kate']}")
print(f"Scott's final exam grade is: {final_grades['scott']}")
print(f"Lauren's final exam grade is: {final_grades['lauren']}")
print(f"Christopher's final exam grade is: {final_grades['christopher']}")
print(f"Alice's final exam grade is: {final_grades['alice']}")
final_grades['christopher'] = 87
print(f"Whoops, I made a mistake with Christopher's final exam grade. His "
      f"grade is actually {final_grades['christopher']}.")
all_students = set(students)
passed = {'michael', 'lauren', 'christopher'}
print(f'The students who passed my class are: {passed}')
failed = all_students.difference(passed)
print(f'The students who failed my class are: {failed}')
women = {'kate', 'lauren'}
passing_women = passed.intersection(women)
print(f'The women who passed my class are: {passing_women}')
teachers = {'harry', 'emma'}
all_people = all_students.union(teachers)
print(f'The students and teachers participating in this class are: '
      f'{all_people}')
