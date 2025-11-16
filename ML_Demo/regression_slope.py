# Input
# Physics Scores  15  12  8   8   7   7   7   6   5   3
# History Scores  10  25  17  11  13  17  20  13  9   15
import sys

def compute_regression_slope(x, y):
    n = len(x)

    mean_x = sum(x) / n
    mean_y = sum(y) / n

    num_xy = 0
    den_x = 0

    for i in range(n):
        num_xy += (x[i] - mean_x) * (y[i] - mean_y)
        den_x += (x[i] - mean_x) ** 2

    return round(num_xy / den_x, 3)


input_data = sys.stdin.read().splitlines()
physics_scores = list(map(int, input_data[0].split()[2:]))
history_scores = list(map(int, input_data[1].split()[2:]))

# physics_scores = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
# history_scores = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

print(compute_regression_slope(physics_scores, history_scores))