import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('./ex1data1.csv', delimiter=',')
X = data[:, 0]
y = data[:, 1]

m = len(X)

plt.xlabel('Population of City in 10,000s')
plt.ylabel('Profit in $10,000s')
plt.scatter(X, y, marker="x", c="red")

plt.show()

X0 = np.ones((m, 1))
X = np.column_stack((X0, X))
init_theta = np.zeros((X.shape[1], 1))

y = y.reshape((-1, 1))
# Also can use np.array([y]) which will make array as (1, 97) size. So while subtracting we will use y.T.


# Computing cost function
def compute_cost(i, o, theta):
    predictions = np.dot(i, theta)
    sqr_err = np.subtract(predictions, o) ** 2
    return sum(sqr_err) / (2 * m)


J1 = compute_cost(X, y, init_theta)
print(J1)

J2 = compute_cost(X, y, [[-1], [2]])
print(J2)


# Computing gradient descent
def compute_gradient_descent(i, o, theta, alpha, num_iters):
    for iter in range(num_iters):
        predict = np.dot(i, theta)
        pred_err = np.subtract(predict, o)
        gradient = np.dot(i.T, pred_err) / m
        theta = theta - alpha * gradient

    return theta


iterations = 1500
alpha = 0.01

final_theta = compute_gradient_descent(X, y, init_theta, alpha, iterations)

print(final_theta)

plt.scatter(X[:, 1], y, marker="x", c="red")
plt.plot(X[:, 1], np.dot(X, final_theta), c="blue")

plt.show()

print(np.dot([1, 3.5], final_theta) * 10000)
print(np.dot([1, 7], final_theta) * 10000)

