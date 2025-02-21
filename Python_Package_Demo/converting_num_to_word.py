num_to_word_dict = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}

phone_num = input("Phone No: ")

phone_num_word = ""

for digit in phone_num:
    phone_num_word += num_to_word_dict.get(digit) + " "

print(phone_num_word)
