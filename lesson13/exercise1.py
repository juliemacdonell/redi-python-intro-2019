#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Lesson 13 - Pair Programming
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Exercise 1

In this exercise, you will write a program which will convert numbers between
binary and decimal and vice-versa.
"""

# Part 1
my_binary_number = '1011001'
my_decimal_number = 0

# `my_binary_number[::-1]` reverses the `my_binary_number` string so
# that you can iterate through the digits from right to left. Enumerate is a
# helpful function which gives us a counter for each iteration of the for loop.
# Try running the code as is to understand how the for loop works.
for index, digit in enumerate(my_binary_number[::-1]):
    if index == 0:
        print(f'The {index}st digit is: {digit}')
    else:
        print(f'The {index}th digit is: {digit}')

# Task 1: Convert `my_binary_number` to `my_decimal_number` by replacing the
# `pass` in the for loop with the correct code.
for index, digit in enumerate(my_binary_number[::-1]):
    pass

# If you have completed the task correctly, the output of this statement
# should be: 1011001 (binary) is 89 (decimal)
print(f'{my_binary_number} (binary) is {decimal} (decimal)')


# Part 2
my_binary_lookup = {}

print('Welcome to my binary number converter. I will prompt you to enter '
      'binary numbers to convert until you enter the value exit.')
user_binary = input('Which binary number should I convert to decimal? ')
# Task 2: While `user_binary` is not 'exit', convert the user's binary to
# decimal and store in `my_binary_lookup` such that the key is binary and the
# value is decimal. When the user inputs 'exit', print the lookup back to
# the user.


