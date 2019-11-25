# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 21:59:57 2019

@author: adeniyi
"""

print(f'Welcome to my temperature converter!')
temperature_user = int(input('state the temperature you want')
temperature_scale_user = input('write the temperature scale you want')
valid_temperature_scales = ('Fahrenheit','F','Celcius','C')
while temperature_scale_user is not in valid_temperature_scales:
    temperature_scale_user = input('write the temperature scale you want')
    print('Hint: try again to choose a valid scale,scale is within Celcius and Fahrenheit')
print('ok, 45 Celsius will be converted to Fahrenheit')
print('The converted temperature you prefer is 113 in Fahrenheit')