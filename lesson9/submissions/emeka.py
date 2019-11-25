# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 18:05:09 2019

@author: emeka
"""

# !/usr/bin/env python
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
user_temp = input(
    'what temperature do you want to convert? Fahrenheit or Celsius; ')

# Task 2: Ask the user which temperature scale they would like their
# temperature converted to?
# Hint: Save the answer to a variable.
conv_user_temp = input(
    'which temperature scale do you want the tempearture to be converted to? ')

valid_temperature_scales = ('Fahrenheit', 'F', 'Celsius', 'C')
# Task 3: Using a while loop, check whether the desired temperature is in
# among the `valid_temperature_scales` defined above. If it is not, then the
# program should enter into the while loop execution block and prompt the
# user to provide again the desired temperature scale until a valid was is
# given by the user. Perhaps you might also want to print out some helpful
# information to the user, so as letting them know they did not choose a
# valid scale and which scales are valid.
while conv_user_temp not in valid_temperature_scales:
    print('Sorry, I can\'t convert this')
    conv_user_temp = input('''Enter another temperature scale, 
                           e.g., Fahrenheit(F), Celsius(C); ''')

# Task 4: Print back to the user what you plan to do with their request, i.e.
# 'Okay, I will convert 45 Celsius to Fahrenheit for you'
print(f'Okay, I will convert {user_temp} to {conv_user_temp} for you')
# Task 5: Calculate the converted temperature. You can easily find these
# questions online if you are stuck.
if user_temp == 'Fahrenheit':
    fah = float(input('Enter the temperature degree in fahrenheit; '))
    Celsius = (fah - 32) / 1.8
    print(f'{fah} degree Fahrenheit is equal to {Celsius} degree Celsius')
elif user_temp == 'Celsius':
    cel = float(input('Enter the temperature degree in celsius; '))
    Fahrenheit = (cel * 1.8) + 32
    print(f'{cel} degree celsius is equal to {Fahrenheit} degree Fahrenheit')

# Task 6: Print the results to your user.


# Task 7: Use your Celsius to Fahrenheit equation and a for loop to print
# the conversions of Celsius to Fahrenheit for Celsius values -10 to 30.
# Hint: Your for loop should use the `range` function.
for index in range(-10, 31):
    Fahrenheit = (index * 1.8) + 32
    print(f'{index} degree Celsius is equal to {Fahrenheit} degree Fahrenheit')