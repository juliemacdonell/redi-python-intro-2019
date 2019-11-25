# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 21:10:26 2019

@author: emeka
"""

# -*- coding: utf-8 -*-
"""
Homework 6
~~~~~~~~~~
Let's pretend there is a course at ReDI called "Introduction to Magic".
Let's say Yoana at ReDI asks you to write a report about the course results.

Fix the code as instructed in the numbered tasks.
Be sure that the code you submit runs without errors!

If you run the code as is, without modifications, it should run without errors;
however, the report information will be wrong. Your job is to correct the 
'fix me's.
"""
print(f"Here's a report about the Introduction to Magic course.")

# Here, we define a list of students in the class.
students = ['michael', 'kate', 'scott', 'lauren', 'christopher']
print(f'The students in our class are: {students}')

# Here, we define a list of grades for a mid-term exam.
grades = [100, 60, 55, 82, 90]
print(f'The grades on the mid-term exam are: {grades}')

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
avg_grade = sum(grades)/len(grades)
print(f'The average grade in the class is: {avg_grade}')

# 4. Let's assume 'alice' just joined the class. Add a line of code below,
# which modifies the `students` list using the `append` operation in order to
# add 'alice' to the list of students.
students.append('alice')
print(f'A new student, Alice, just joined the class!')
print(f'The students in our class are now: {students}')

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
final_grades['michael']

# 6. Print the other students' final exam grades the same way you printed
# Michael's.
final_grades['kate']
final_grades['scott']
final_grades['lauren']
final_grades['christopher']
final_grades['alice']

# 7. One teacher realizes she made an error with Christopher's final exam
# grade. He actually got a 87. Fix his grade in the `final_grades` dictionary
# by updating the value for the key 'christopher' (not by recreated a new
# dictionary).
final_grades['christopher'] = 87
print(f"Whoops, I made a mistake with Christopher's final exam grade. His "
      f"grade is actually {final_grades['christopher']}.")

# This `set` function creates a set from the list of students.
all_students = set(students)
passed = {'michael', 'lauren', 'christopher'}
print(f'The students who passed my class are: {passed}')

# 8. Using the `difference` set operation, assign `failed` the set of
# students who passed the class.
failed = all_students.difference(passed)
print(f'The students who failed my class are: {failed}')

women = {'kate', 'lauren'}
# 9. Using the `intersection` set operation, assign `passing_women` the set of
# women who passed the class.
passing_women = passed.intersection(women)
print(f'The women who passed my class are: {passing_women}')

teachers = {'harry', 'emma'}
# 10. Using the `union` set operation, assign `all_people` the set of
# all people, i.e. students and teachers, who are participating in this class.
all_people = all_students.union(teachers)
print(f'The students and teachers participating in this class are: '
      f'{all_people}')

# Optional BONUS: Create a few other report information. Feel free to be
# creative by creating new sets or writing new statistics!
print(all_students)