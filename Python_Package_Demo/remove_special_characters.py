import re, string

def remove_spl_chars_regex(input_string: str) -> str:
    return re.sub(r'\W+', ' ', input_string)

def remove_spl_chars_string(input_string: str) -> str:
    translator = str.maketrans('', '', string.punctuation)
    return input_string.translate(translator)

if __name__ == "__main__":
    test_string = "Hello, World! Welcome to Python 3.13 @ 2026."
    print(f'Original String: {test_string}')
    print("Test 1: Using regex")
    result = remove_spl_chars_regex(test_string)
    print(f'String after removing special characters: {result}')
    print("Test 2: Using string.punctuation")
    result = remove_spl_chars_string(test_string)
    print(f'String after removing special characters: {result}')