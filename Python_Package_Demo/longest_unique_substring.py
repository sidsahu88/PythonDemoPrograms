def longest_unique_substring(s: str) -> int:
    max_len = 0
    start = 0
    char_set = set()

    for end in range(len(s)):
        while s[end] in char_set:
            char_set.remove(s[start])
            start += 1

        char_set.add(s[end])
        str_len = end - start + 1
        max_len = max(max_len, str_len)

    return max_len


if __name__ == "__main__":
    s = "abcabcbb"
    print(s, longest_unique_substring(s))

    s = "bbbbb"
    print(s, longest_unique_substring(s))
    
    s = "pwwkew"
    print(s, longest_unique_substring(s))

    s = "dvdf"
    print(s, longest_unique_substring(s))

    s = "tmmzuxt"
    print(s, longest_unique_substring(s))
