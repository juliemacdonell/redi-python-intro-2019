#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Lesson 9 - Pair Programming
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Exercise 2

Write a Python program to find those numbers which are divisible by 7 and
multiple of 5, between 1500 and 2700 (both included).

The program should add all of these numbers to a list and print them out to
the user at the end of the program.

Hint: Use a for loop, the `range` function, an if condition, and the modulo
operator.
"""
my_numbers = []
for number in range(1500, 2701):
    if number % 7 == 0 and number % 5 == 0:
        my_numbers.append(number)

print('Here are the numbers between 1500 and 2700 that are divisible by both '
      '7 and 5:')
print(my_numbers)
