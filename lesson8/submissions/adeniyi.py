# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 19:54:01 2019

@author: adeniyi
"""

people_name = ['segun', 'elizabeth', 'moyin', 'jola']
if peoples_name > 3:
    print('The room is Crowded!')
peoples_name.pop(0)
print(peoples_name)
new_names = ['elizabeth', 'moyin', 'jola']
new_names.remove('jola')
print(new_names)
modified_names = ['elizabeth', 'moyin']
if modified_names < 3:
    print('the room is available:not crowded')

rooms = {'big_room': {room_capacity: 20, room_number: 1}
         big_room = {'room_capacity': 20, 'room_number': 1}
big_room['room_capacity'] = 40
print(big_room)
big_room['room_room'] = 2
print(big_room)
big_room['tables_number'] = 20
print(big_room)
rooms = {
    'big_rooms': {'room_capacity': 40, 'room_number': 2, 'table_number': 20}}
rooms['second_room'] = 'conference_room'
print(rooms)
conference_room = {}
conference_room['room_capacity'] = 12
print(conference_room)
conference_room['table_number'] = 2
print(conference_room)
print(rooms)
rooms = {
    'big_rooms': {'room_capacity': 40, 'room_number': 2, 'table_number': 20},
    'conference_room': {'room_capacity': 12, 'table_number': 2}}
rooms.pop('conference_room')
print(room)
