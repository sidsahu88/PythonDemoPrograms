def find_list_intersection(list1, list2):
    return set(list1) & set(list2)

if __name__ == "__main__":
    list_a = [1, 2, 3, 4, 5, 6]
    list_b = [4, 5, 6, 7, 8, 9]
    intersection = find_list_intersection(list_a, list_b)
    print("Intersection:", intersection)