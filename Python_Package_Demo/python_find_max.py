def find_max(numbers:list[int]) -> int:
    largest_num = 0

    for number in numbers:
        if number > largest_num:
            largest_num = number

    return largest_num


if __name__ == "__main__":
    sample_numbers = [3, 5, 7, 2, 8]
    print(f"The largest number in the list is: {find_max(sample_numbers)}")
