print(f'Welcome to my temperature converter!')
users_temp = int(input('what is your prefered temperature?'))
users_temp_scale = input('what temperature scale would you prefer?')
valid_temperature_scales = ('Fahrenheit', 'F', 'Celsius', 'C')
while users_temp_scale not in valid_temperature_scales:
    users_temp_scale = input('what temperature scale would you prefer?')
    print('Hint: you did not choose a valid scale,scale is between C and F')
print(' Ok, I will convert 45 Celsius to Fahrenheit for you!')
print('Your prefered temperature in Fahrenheit is 113 degrees!')