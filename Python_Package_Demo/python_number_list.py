numbers = [13, 4, 64, 5, 7, 23, 89, 51]

numbers_copy = numbers.copy()

print(f'Numbers: {numbers}')

print(f'Index of 7 in the List: {numbers.index(7)}')

print(f'64 exists in the list? {64 in numbers}')

print(f'50 exists in the list? {50 in numbers}')

numbers.insert(3, 69)
print(f'Numbers Insert(69): {numbers}')

numbers.remove(64)
print(f'Numbers Remove(64): {numbers}')

numbers.pop()
print(f'Numbers Pop Last Element: {numbers}')

numbers.clear()
print(f'Numbers Clear All: {numbers}')

print(f'Copied List: {numbers_copy}')
