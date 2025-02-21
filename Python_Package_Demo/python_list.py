names = ['Sid', 'San', 'Kanha', 'Lisha']

print(names)
print(names[2])
print(names[-1])
print(names[2:4])

names.append('Srimant')
print(names)

firstnames = names  # Both names and firstnames referring to same list
print(firstnames)

firstnames[0] = "Siddharth"
print(names)
print(firstnames)

clonenames = names[:]  # Cloning the list i.e. clonenames is referring to new list
print(clonenames)

clonenames[1] = 'Sangita'
print(names)
print(clonenames)
