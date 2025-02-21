'''
Created on 13-Jul-2019

@author: siddharthsahu
'''
import random


class Dice:

    def roll1(self):
        face = (1, 2, 3, 4, 5, 6)
        print(f'({random.choice(face)}, {random.choice(face)})')
    
    def roll2(self):
        return random.randint(1, 6), random.randint(1, 6)
