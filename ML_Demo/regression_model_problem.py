# Input
# -----
# 2 7                     F = 2, N = 7
# 0.18 0.89 109.85        Features = [0.18, 0.89] Square foot cost = 109.85
# 1.0 0.26 155.72
# 0.92 0.11 137.66
# 0.07 0.37 76.17
# 0.85 0.16 139.75
# 0.99 0.41 162.6
# 0.87 0.47 151.77
# 4                       T = 4
# 0.49 0.18               Features for the first property
# 0.57 0.8
# 0.56 0.64
# 0.76 0.18
#

from sklearn.linear_model import LinearRegression

row1 = [2, 7]
# row1 = list(map(int, input().split()))
f = row1[0]
n = row1[1]

data = [
    [0.18, 0.89, 109.85],   
    [1.0, 0.26, 155.72],
    [0.92, 0.11, 137.66],
    [0.07, 0.37, 76.17],
    [0.85, 0.16, 139.75],
    [0.99, 0.41, 162.6],
    [0.87, 0.47, 151.77]
]
# data = []
# for i in range(n):
#     row = list(map(float, input().split()))
#     data.append(row)

X = [row[:-1] for row in data]
y = [row[-1] for row in data]

# Read test data
t = 4
# t = int(input())

test_data = [
    [0.49, 0.18],
    [0.57, 0.8],
    [0.56, 0.64],
    [0.76, 0.18]
]
# test_data = []
# for i in range(t):
#     row = list(map(float, input().split()))
#     test_data.append(row)

linearReg = LinearRegression()

linearReg.fit(X, y)

predictions = linearReg.predict(test_data)

prices = [round(prediction, 2) for prediction in predictions]
print(*prices, sep="\n")
