try:
    age = int(input('Age: '))
    print(f'Birth Year: {2019-age}')
except ValueError:
    print('Invalid input!')
# multiple except can be used here.
else:
    print('Program executed successfully.')
finally:
    print('Finally exiting the program.')
