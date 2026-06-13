from collections import defaultdict
from collections import Counter


def top_k_freq(num_list, k: int) -> list:
    freq_dict = defaultdict(int)
    
    for num in num_list:
        freq_dict[num] += 1

    sorted_freq_list = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)

    return [k for k, v in sorted_freq_list[:k]]


def top_k_freq_counter(num_list, k: int) -> list:
    freq_dict = Counter(num_list)
    return [k for k, _ in freq_dict.most_common(k)]

    

if __name__ == "__main__":
    num_list = [1, 1, 1, 2, 2, 3, 3, 3, 3]
    k = 2
    print(top_k_freq(num_list, k))
    print(top_k_freq_counter(num_list, k))