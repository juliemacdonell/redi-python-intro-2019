#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Lesson 9 - Pair Programming
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Exercise 1

Create a "Guess My Number" game using a while loop. The idea of this game is
that you, as the clever programmer, has determined a secret number. The user
of your game will have to keep guessing a number until the number the user
guesses matches your number, muahaha!

Note: User is prompted to enter a guess. If the user guesses wrong then the
prompt appears again until the guess is correct, on successful guess, user will
get a congratulatory message, and the program will exit.

First try on your own, but then use these hints if you are having trouble
getting started:
- Assign the variable `my_secret_number` to your secret number
- Assign the variable `user_guess` to the first guess of the user
- Use a while loop and check the condition, in this case, whether the secret
number and the user's guess don't match, in which case, ask the user to
guess again.
- If the condition is false, i.e. the user guessed your number, then the
while loop will exit, and you should congratulate the clever user!
"""
# Simple implementation
print('Hello, friendly user! Welcome to my amazing game!')
print("I've picked a super secret number, amd I'll give you unlimited "
      "guesses--isn't that generous of me?! Have fun!")

my_secret_number = 11782

user_guess = int(input('Please enter your first guess: '))
while user_guess != my_secret_number:
      print('Wrong!!! But I will give you another try...')
      user_guess = int(input('Guess again: '))

print('Congratulations, you are so smart!!')
print('Good bye!')


# Here is a more advanced implementation
import random

input('Hello, friendly user! Welcome to my amazing game! Press any key to '
      'continue...')
input("I've picked a super secret number, amd I'll give you unlimited "
      "guesses--isn't that generous of me?! Press any key to continue...")
answer = input('Do you want to play my game? Type yes if you would like to '
               'play: ')
answer = answer.replace(' ', '')  # Remove whitespace from string
answer = answer.lower()  # Be forgiving with the user's answer in case s/he
                         # answers with YES

if answer == 'yes':
      my_secret_number = 11782

      try:
            user_guess = int(input('Please enter your first guess: '))
      except ValueError:
            print('You did not enter a number!')
            user_guess = int(input('Please enter your first guess: '))

      while user_guess != my_secret_number:
            print(random.choice([
                  'Wrong!!! But I will give you another try...',
                  'Nope!',
                  'You really are not good at this game, are you?',
                  'Falsch!!',
            ]))
            user_guess = int(input('Guess again: '))

      print('Congratulations, you are so smart!!')
      print('Good bye!')
else:
      print("I'm sorry you do not want to play my amazing game! You're loss!")

