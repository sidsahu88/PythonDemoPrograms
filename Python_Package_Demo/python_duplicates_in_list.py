numbers = [4, 1, 2, 3, 6, 4, 5, 9, 6, 7, 8]
unique = []

for i in numbers:
    if i not in unique:
        unique.append(i)

print(f'Original List: {numbers}')
print(f'Unique List: {unique}')
