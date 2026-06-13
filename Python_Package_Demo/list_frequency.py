from collections import defaultdict


def calculate_frequency(mylist: list):
    freq_dict = defaultdict(int)

    for n in mylist:
        freq_dict[n] += 1
    
    return freq_dict


if __name__ == "__main__":
    my_list = [2, 3, 3, 2, 1, 6, 2, 1, 3, 16, 3, 4, 3, 4]
    print(calculate_frequency(my_list))