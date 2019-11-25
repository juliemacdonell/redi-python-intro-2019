# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 22:41:53 2019

@author: Yasmine
"""

print(f'Welcome to my temperature converter!')

# Task 1: Ask the user what temperature they would like to convert.
# Hint: Save this to a variable and be careful with types.
User_temperature = int(input("Enter the temperature degree you want to \
convert, only enter number(S): "))
current_scale = str(input("Specify whether the degree you just entered is \
Fahrenheit or Celsius: "))

# Task 2: Ask the user which temperature scale they would like their
# temperature converted to?
# Hint: Save the answer to a variable.
conversion_scale = input("Enter the scale you want to convert to: ")
valid_temperature_scales = ["Fahrenheit", "F", "Celsius", "C"]

# Task 3: Using a while loop, check whether the desired temperature is in
# among the `valid_temperature_scales` defined above. If it is not, then the
# program should enter into the while loop execution block and prompt the
# user to provide again the desired temperature scale until a valid was is
# given by the user. Perhaps you might also want to print out some helpful
# information to the user, so as letting them know they did not choose a
# valid scale and which scales are valid.
# Task 4: Print back to the user what you plan to do with their request, i.e.
# 'Okay, I will convert 45 Celsius to Fahrenheit for you'

while conversion_scale not in valid_temperature_scales:
    # print(conversion_scale=input("Invalid entry, choose either Fahrenheit,\
    # F, Celsius or C: "))
    conversion_scale = input("Invalid entry, choose either Fahrenheit, "
                             "F, Celsius or C: ")

else:
    print(f"We are going to convert {User_temperature} {current_scale} \
to {conversion_scale} for you. ")

# Task 5: Calculate the converted temperature. You can easily find these
# questions online if you are stuck.
# Task 6: Print the results to your user.


fahrenheit_2_celsius = int(round(((User_temperature - 32) * (5 / 9))))
celsius_2_fahrnheit = int(round(((9 / 5) * (User_temperature) + 32)))

if conversion_scale == "C" or conversion_scale == "Celsius":
    print(f"The tempreature after conversion is, {fahrenheit_2_celsius} C ")

else:
    print(f"The temperature after conversion is, {celsius_2_fahrnheit} F ")

# Task 7: Use your Celsius to Fahrenheit equation and a for loop to print
# the conversions of Celsius to Fahrenheit for Celsius values -10 to 30.
# Hint: Your for loop should use the `range` function.

for celsius in range(-10, 30):
    fahrenheit = int(round(((9 / 5) * celsius + 32)))
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")


