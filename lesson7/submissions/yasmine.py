# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 21:52:57 2019

@author: Yasmine
"""

# 7.A
# First you need to get the numbers from the user:
# (remembering to cast them to a number!)


number1 = int(input("Please give me a random number: "))
number2 = int(input("Please give me a random number: "))
number3 = int(input("Please give me a random number: "))


# Now it is time to compare the numbers
# Use nested if conditions to figure out
# which number is the smallest, the biggest, etc.
# Assign the values of variables number1-3 to new variables:

if number1 < number2 and number1 < number3: smallest = number1
elif number2 < number1 and number2 < number3: smallest = number2
elif number3 < number1 and number3 < number2: smallest = number3

if number1 > number2 and number1 < number3 : middle = number1
elif number1 < number2 and number1 > number3 : middle = number1
elif number2 < number1 and number2 > number3 : middle = number2
elif number2 > number1 and number2 < number3 : middle = number2
elif number3 < number1 and number3 > number2 : middle = number3
elif number3 > number1 and number3 < number2 : middle = number3
print(middle)

# the same solution but with fewer lines of code for the middle
if (number1 > number2 and number1 < number3 ) or (number1 < number2 and number1 > number3): middle = number1
elif (number2 < number1 and number2 > number3) or (number2 > number1 and number2 < number3): middle = number2
elif (number3 < number1 and number3 > number2) or (number3 > number1 and number3 < number2): middle = number3
print(middle)


if number1 > number2 and number1 > number3: biggest = number1
elif number2 > number1 and number2 > number3: biggest = number2
elif number3 > number1 and number3 > number2: biggest = number3
print(biggest)


# Use formatted string with {smallest}, {middle}, {biggest}
# to print the results
print(f"The smallest number is {smallest}")
print(f"The middle number is {middle}")
print(f"The largest number is {biggest}")

# 7.B
# There are faster ways of achieving the same results!
# Make a list that contains the numbers1-3
# and use one of the methods we learned to order the numbers.

my_list = [number1, number2, number3]
print(my_list)
my_list.sort()
print(my_list)

#Another way of creating the list

my_list = []
my_list.append(number1)
my_list.append(number2)
my_list.append(number3)
print(my_list)
my_list.sort()
print(my_list)



# Use formatted string with {my_list} to print the result
print(f'The acsending sorting of the list is {my_list}')