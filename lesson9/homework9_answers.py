#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Lesson 9 - Temperature Conversion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this homework, you will write a program which will convert a temperature
given by the user into Fahrenheit or Celsius depending on what the user
requests.
-
"""
print(f'Welcome to my temperature converter!')

# Task 1: Ask the user what temperature they would like to convert.
# Hint: Save this to a variable and be careful with types.
user_temperature = float(input('What temperature would you like to convert? '))

# Task 2: Ask the user which temperature scale they would like their
# temperature converted to?
# Hint: Save the answer to a variable.
scale = input('Which temperature scale would you like to convert to? ')

valid_temperature_scales = ('Fahrenheit', 'F', 'Celsius', 'C')
# Task 3: Using a while loop, check whether the desired temperature is in
# among the `valid_temperature_scales` defined above. If it is not, then the
# program should enter into the while loop execution block and prompt the
# user to provide again the desired temperature scale until a valid was is
# given by the user. Perhaps you might also want to print out some helpful
# information to the user, so as letting them know they did not choose a
# valid scale and which scales are valid.
while scale not in valid_temperature_scales:
    print(f'The scale `{scale}` you provided is not valid.')
    print(f'These are the valid temperature scales: '
          f'{valid_temperature_scales}')
    scale = input('Which temperature scale would you like to convert to? ')

# Task 4: Print back to the user what you plan to do with their request, i.e.
# 'Okay, I will convert 45 Celsius to Fahrenheit for you'
if scale == 'Fahrenheit' or scale == 'F':
    print(f'Okay, I will convert {user_temperature} Celsius to Fahrenheit...')
else:
    print(f'Okay, I will convert {user_temperature} Fahrenheit to Celsius...')

# Task 5: Calculate the converted temperature. You can easily find these
# questions online if you are stuck.
if scale == 'Fahrenheit' or scale == 'F':
    converted_temperature = user_temperature * (9 / 5) + 32
else:
    converted_temperature = (user_temperature - 32) * (5 / 9)

# Task 6: Print the results to your user.
print(f'Your converted temperature is: {converted_temperature}')

# Task 7: Use your Celsius to Fahrenheit equation and a for loop to print
# the conversions of Celsius to Fahrenheit for Celsius values -10 to 30.
# Hint: Your for loop should use the `range` function.
for celsius in range(-10, 32):
    fahrenheit = celsius * (9 / 5) + 32
    print(f'{celsius} Celsius is {fahrenheit} Fahrenheit')

