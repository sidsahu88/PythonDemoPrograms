numbers = [1, 2, 13, 4, 5, 6, 7, 8]
largest_num = 0

for num in numbers:
    if largest_num < num:
        largest_num = num

print(largest_num)