import matplotlib.pyplot as plt

X = [1, 2, 3, 4, 5, 6, 7, 8]
Y = [0, 0, 0, 0, 0, 0, 0, 0]

for i, x in enumerate(X):
    Y[i] = X[i] ** 2 + 3 * X[i] + 2
    print(X[i], Y[i])


plt.xlabel('X')
plt.ylabel('Y')

plt.plot(X, Y)
plt.show()
