# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 13:21:13 2019

@author: arunkumar.chinnamani
"""

print(f'Welcome to my temperature converter!')

user_input = float(input('what temperature you would like to convert :'))

user_wish = input('which temperature scale you would like to convert:')

valid_temperature_scales = ('F', 'Fahrenheit', 'Celsius', 'C')

while user_wish not in valid_temperature_scales:
    print(f'''The temperature are measured always as Fahrenheit or Celsius.
          1.Give correct Temperature scale
          2.Valid temp scale is mentioned already''')
    user_wish = input('which temperature scale you would like convert:')
print('\n')

if user_wish == ' F' or user_wish == 'Fahrenheit':
    print(f'Okay, I will convert {user_input} Celsius to Fahrenheit for you')
    user_output = (user_input * 9 / 5) + 32
    print(' The required temp in fahrenheit is :', user_output)

elif user_wish == 'Fahrenheit':
    print(f'Okay, I will convert {user_input} Celsius to Fahrenheit for you')
    user_output = (user_input * 9 / 5) + 32
    print(' The required temp in fahrenheit is :', user_output)

else:
    print(f'Okay, I will convert {user_input} fahrenheit to Celsius for you')
    user_output = (user_input - 32) * 5 / 9
    print(' The required temp in Celsius is :', user_output)

print('\n')
print('By using For loop Celsius to Fahrenheit conversion\n')
my_list = []
for i in range(-10, 30):
    output = (i * 9 / 5) + 32
    my_list.append(output)
print(
    'I have added coverted temperature from celsius to Fahrenheit in my_list :\n',
    my_list)
