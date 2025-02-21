'''
Created on 13-Jul-2019

@author: siddharthsahu
'''
import random

for i in range(3):
    print(f'Random no.: {random.random()}')
    print(f'Random no. between 10 to 20: {random.randint(10,20)}')
    print('\n')

members = ['Siddharth', 'Srimant', 'Sangita', 'Kanha', 'Lisha']
print(f'Leader of team: {random.choice(members)}')
