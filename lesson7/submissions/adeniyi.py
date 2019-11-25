# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 21:32:27 2019

@author: adeniyi
"""

number1 = int(input('what is your house number?'))
number2 = int(input('when is your wedding day?'))
number3 = int(input('what is your favourite number?'))
largest = {number1, number2, number3}
if number1 > number2 and number1 > number3:
    print('number1 is the largest')
elif number2 > number1 and number2 > number3:
    print('number2 is the largest')
else:
    print('number3 is the largest')
smallest = {number1, number2, number3}
if number1 < number2 and number1 < number3:
    print('number1 is the smallest')
elif number2 < number1 and number2 < number3:
    print('number2 is the smallest')
else:
    print('number3 is the smallest')
