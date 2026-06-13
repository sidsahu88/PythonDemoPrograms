
def find_max_average(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, len(nums)):
        # window_sum = sum(nums[i-k:i]) # Not optimal
        window_sum += nums[i] - nums[i-k]  # Optimal
        max_sum = max(max_sum, window_sum)

    return max_sum / k


if __name__ == "__main__":
    nums = [1, 12, -5, -6, 50, 3]
    k = 4

    print(find_max_average(nums, k))
