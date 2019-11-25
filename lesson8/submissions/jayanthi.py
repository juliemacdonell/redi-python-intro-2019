# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 22:10:47 2019

@author: arunkumar.chinnamani
"""

print('Exercise :1')
list = ['jay','priya','swathi','lasya']
length = len(list)

if length >= 3 :
    list.remove('priya')
else:
    print(' The room is crowded ')

print('Exercise: 2\n')
rooms_dict= {}
rooms_dict= {'big_room':{'room_capacity':200,'room_number':1}}
print(' My room dictionary is :\n',rooms_dict)

rooms_dict['big_room']['room_capacity'] =( 20 ,40)
rooms_dict['big_room']['room_number'] = 2
print('\n')
print('The newly changed values of  room dictionary :\n',rooms_dict)

print('\n')
print('Add \'Room_tables\' key into  big_room dictionary :\n')
rooms_dict['big_room'].update({'room_tables':20})
print(rooms_dict)

print('\n')
print('Adding one more Key to the Room dictionary :\n ')
name = 'small conference room'
rooms_dict[name]= {'capacity ':12, 'table_name':2}
print(rooms_dict)

print('\n')
print('Due to renovation added key is removed .')
rooms_dict.pop(name)
print(' My room dictionary is :\n',rooms_dict)


print('\n')
print('Exercise :3')

print('case 1: A = True, B = True  ' )
A = True
B = True
list = [(A and B),  (A or B), not A]
print(list)
print('\n')
print('case 2: A = True, B = False  ' )
A = True
B = False
list = [(A and B),  (A or B), not A]
print(list)
print('\n')
print('case 3: A = False, B = True  ' )
A = False
B = True
list = [(A and B),  (A or B), not A]
print(list)
print('\n')
print('case 4: A = False, B = False  ' )
A = False
B = False
list = [(A and B),  (A or B), not A]
print(list)


#for'room_capacity' in 'big_room' :
  #  print(rooms['room_capacity'])
#rooms['big_room'{'room_capacity'}]



#for rooms['big_room'] in rooms:
#a = list(rooms_dict['big_room']['room_capacity'])
#print(rooms_dict[['big_room'[room_capacity]]])