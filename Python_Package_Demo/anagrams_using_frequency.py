from list_frequency import calculate_frequency


def check_anagrams(word1:str, word2: str):
    if word1 == word2 or len(word1) != len(word2):
        return False

    chr_freq1 = calculate_frequency(list(word1))
    chr_freq2 = calculate_frequency(list(word2))

    return chr_freq1 == chr_freq2

if __name__ == "__main__":
    tests = [('sidebar', 'seabird'), ('silent','listen'), ('this', 'this'), ('get', 'tar')]

    for words in tests:
        print(f'{words} : {check_anagrams(words[0], words[1])}')

