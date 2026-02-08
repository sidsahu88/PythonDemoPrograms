import numpy as np

def sigmoid(z):
    return 1/(1 + np.exp(-z))

def log_loss(y, y_hat):
    loss = - (y * np.log(y_hat)) - ((1-y) * np.log(1 - y_hat))
    return np.mean(loss)

def gradient_descent(X, y, learning_rate, n_iter):
    m, n = X.shape
    W = np.zeros(n)
    b = 0
    loss = []

    for i in range(n_iter):
        z = np.dot(X, W) + b
        y_hat = sigmoid(z)

        loss.append(log_loss(y, y_hat))
        dw = (1/m) * np.dot(X.T, (y_hat - y))
        db = (1/m) * np.sum(y_hat - y)

        W -= learning_rate * dw
        b -= learning_rate * db

    return W, b, loss

def predict(X, W, b):
    z = np.dot(W, X) + b
    y_hat = sigmoid(z)
    return [1 if i > 0.5 else 0 for i in y_hat]

if __name__ == "__main__":
    X = np.array([[0.5, 1.5], [1.0, 1.0], [1.5, 0.5], [3.0, 3.5], [2.0, 2.0], [3.5, 2.5]])
    y = np.array([0, 0, 0, 1, 1, 1])

    learning_rate = 0.01
    n_iter = 10

    W, b, loss = gradient_descent(X, y, learning_rate, n_iter)
    print("Weights:", W)
    print("Bias:", b)
    print("Loss over iterations:", loss)

    X_test = np.array([[1.0, 2.0], [3.0, 2.0]])
    predictions = predict(X_test, W, b)

    print("Predictions on test data:", predictions)