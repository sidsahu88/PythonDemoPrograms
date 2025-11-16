def compute_moving_average(data, window_size):
    if window_size <= 0:
        raise ValueError("Window size must be positive")
    if window_size > len(data):
        raise ValueError("Window size must not be larger than data length")
    
    moving_avg = []
    for i in range(len(data) - window_size + 1):
        avg = sum(data[i:i+window_size]) / window_size
        moving_avg.append(round(avg, 2))

    return moving_avg


def compute_moving_avg_pandas(data, window_size):
    import pandas as pd

    if window_size <= 0:
        raise ValueError("Window size must be positive")
    if window_size > len(data):
        raise ValueError("Window size must not be larger than data length")

    series = pd.Series(data)
    moving_avg = series.rolling(window=window_size).mean().dropna().tolist()
    
    return moving_avg


if __name__ == "__main__":
    # Example usage
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    window_size = 5
    result = compute_moving_average(data, window_size)
    print(result)

    # Using pandas
    pandas_result = compute_moving_avg_pandas(data, 3)
    print(pandas_result)