def find_max(numbers):
    largest_num = 0

    for number in numbers:
        if number > largest_num:
            largest_num = number

    return largest_num
