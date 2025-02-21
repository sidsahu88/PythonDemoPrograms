numbers = [6, 2, 6, 2, 2]

for x in numbers:
    pattern = ''
    for y in range(x):
        pattern += 'X'
    print(pattern)

print()

for x in numbers:
    print('X' * x)
