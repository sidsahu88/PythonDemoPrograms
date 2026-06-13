from collections import defaultdict

def group_anagrams(words: list) -> list:
    anagram_dict = defaultdict(list)

    for word in words:
        sorted_chars = "".join(sorted(word))
        anagram_dict[sorted_chars].append(word)

    return list(anagram_dict.values())


if __name__ == "__main__":
    words = ["cat", "tar", "eagle", "tac", "listen", "rat", "act", "art", "silent", "acts" ]
    print(group_anagrams(words))