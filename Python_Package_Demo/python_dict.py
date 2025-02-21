'''
Created on 01-Aug-2019

@author: siddharthsahu
'''

word_list = ["Good", "Outrageous", "Terrific", "Disgusting", "Best"]

print(dict([(word, "movie") for word in word_list]))

dictionary = {'Sid': 7, 'Sangchi': 9, 'Lisha': 7, 'Kanha': 8}

print(dictionary)
print(dictionary['Sangchi'])

dictionary['Srimant'] = 8

print(dictionary)

print(dictionary.keys())
print(dictionary.values())
