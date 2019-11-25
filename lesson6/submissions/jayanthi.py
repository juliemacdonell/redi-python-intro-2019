# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 10:04:56 2019

@author: arunkumar.chinnamani
"""

print(f"Here's a report about the Introduction to Magic course.\n")

# Here, we define a list of students in the class.
students = ['michael', 'kate', 'scott', 'lauren', 'christopher']
print(f'The students in our class are:\n {students}\n')

# Here, we define a list of grades for a mid-term exam.
grades = [100, 60, 55, 82, 90]
print(f'The grades on the mid-term exam are: {grades}\n')

# 1. Using the function `max` on the `grades` list, assign the variable
# `best_grade` to the max score of the students.
best_grade = max(grades)
print(f'The best grade in the class is: {best_grade}')

# 2. Using the function `min` on the `grades` list, assign the variable
# `worst_grade` to the min score of the students.
worst_grade = min(grades)
print(f'The worst grade in the class is: {worst_grade}')

# 3. Using the functions `sum` and `len` on the `grades` list as well as basic
# math operations, assign the variable `avg_grade` to the average grade of the
# students.

sum = 0
for num in grades:
    sum = num + sum

avg_grade = sum / len(grades)
print(f'The average grade in the class is: {avg_grade}\n')

# 4. Let's assume 'alice' just joined the class. Add a line of code below,
# which modifies the `students` list using the `append` operation in order to
# add 'alice' to the list of students.

print(f'A new student, Alice, just joined the class!')
students.append("alice")
print('The students in our class are now:\n ', students)

# Let's try a different data structure for storing final exam grades. We'll
# user a dictionary.
final_grades = {
    'michael': 89,
    'kate': 100,
    'scott': 75,
    'lauren': 90,
    'christopher': 60,
    'alice': 84,
}

# 5. Fix the print statement to print Michael's final exam grade by using the
# 'michael' key to look up his grade in the `final_grades` dictionary
print(f"Michael's final exam grade is  :", final_grades['michael'])

print(f"Michael's final exam grade is  : {final_grades['michael']}")

# 6. Print the other students' final exam grades the same way you printed
# Michael's.
print(f"kate's final exam grade is  :", final_grades['kate'])
print(f"scott's final exam grade is  :", final_grades['scott'])

print(f"lauren's final exam grade is :", final_grades['lauren'])

print(f"christopher's finalexam grade is :", final_grades['christopher'])

print(f"alice's final exam grade is  :", final_grades['alice'])

# 7. One teacher realizes she made an error with Christopher's final exam
# grade. He actually got a 87. Fix his grade in the `final_grades` dictionary
# by updating the value for the key 'christopher' (not by recreated a new
# dictionary).
final_grades['christopher'] = 87
print(f"Whoops, I made a mistake with Christopher's final exam grade.\n"
      f"His grade is actually {final_grades['christopher']}.\n")

# This `set` function creates a set from the list of students.
all_students = {'michael', 'kate', 'scott', 'lauren', 'christopher'}
print(' All_students are in the class now:\n ', all_students)
print('\n')
passed = {'michael', 'lauren', 'christopher'}
print(f'The students who passed my class are:\n {passed}')

# 8. Using the `difference` set operation, assign `failed` the set of
# students who passed the class.
failed = all_students.difference(passed)
print(f'The students who failed my class are: {failed}')

women = {'kate', 'lauren'}
# 9. Using the `intersection` set operation, assign `passing_women` the set of
# women who passed the class.
passing_women = passed.intersection(women)
print(f'The women who passed my class are: {passing_women}\n')

teachers = {'harry', 'emma'}
# 10. Using the `union` set operation, assign `all_people` the set of
# all people, i.e. students and teachers, who are participating in this class.
all_people = all_students.union(teachers)
print(f'The students and teachers participating in this class are:\n '
      f'{all_people}\n')
print('My extra work :\n')
men_passed = passed.difference(women)
print('men passed in the exam are:', men_passed)
# Adding one more person in the list:
final_grades.update({'Jayanthi': 100})
print(f'after adding one more person , the new grades list:\n{final_grades}')
sum = final_grades['kate'] + final_grades['Jayanthi']
print('Addition of kate and jayanthi marks:', sum)

# MY OUTPUT::
# Here's a report about the Introduction to Magic course.

# The students in our class are:
# ['michael', 'kate', 'scott', 'lauren', 'christopher']

# The grades on the mid-term exam are: [100, 60, 55, 82, 90]

# The best grade in the class is: 100
# The worst grade in the class is: 55
# The average grade in the class is: 77.4

# A new student, Alice, just joined the class!
# The students in our class are now:
#  ['michael', 'kate', 'scott', 'lauren', 'christopher', 'alice']
# Michael's final exam grade is  : 89
# kate's final exam grade is  : 100
# scott's final exam grade is  : 75
# lauren's final exam grade is : 90
# christopher's finalexam grade is : 60
# alice's final exam grade is  : 84
# Whoops, I made a mistake with Christopher's final exam grade.
# His grade is actually 87.

# All_students are in the class now:
# {'lauren', 'kate', 'michael', 'christopher', 'scott'}


# The students who passed my class are:
# {'michael', 'lauren', 'christopher'}
# The students who failed my class are: {'scott', 'kate'}
# The women who passed my class are: {'lauren'}

# The students and teachers participating in this class are:
# {'michael', 'lauren', 'emma', 'harry', 'scott', 'christopher', 'kate'}

# My extra work :

# men passed in the exam are: {'michael', 'christopher'}
# after adding one more person,the new grades list:
# {'michael': 89, 'kate': 100, 'scott': 75, 'lauren': 90, 'christopher': 87, 'alice': 84, 'Jayanthi': 100}
# Addition of kate and jayanthi marks: 200