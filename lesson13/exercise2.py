#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Lesson 13 - Pair Programming
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Exercise 2

In this exercise, you will write a program which handles encoding and
decoding of text.
"""

# Task 1: Update `my_unicode_text` to have some special characters.
my_unicode_text = """
This text doesn't have any special characters, e.g. umlauts. Change this text 
block to have some special characters.
"""

# Task 2: Write `my_unicode_text` to the follow txt file.
unicode_filename = 'my_unicode_file.txt'


# Task 3: Encode `my_unicode_text` into bytes and write it to the following
# txt file. Hint: you need to open the file with 'wb' where 'b' stands for
# bytes.
bytes_filename = 'my_bytes_file.txt'


# Task 4: Load the content from my_bytes_file.txt, save it to the variable
# `bytes_content` print it out to the user. Hint: you need to open the file
# with 'rb'.
bytes_content = 'fix me'
print(f'Here is the content from `my_bytes_file.txt`: {bytes_content}')


# Task 5: Decode `bytes_content` and print it out to the user.
unicode_content = 'fix me'
print(f'Here is the content from `my_unicode_file.txt`: {unicode_content}')


# Task 6: If you have done all of the above correctly, the if-condition
# should be true.
if unicode_content.encode() == bytes_content:
    print('You have done everything correctly')
else:
    print('Something is not right...')
