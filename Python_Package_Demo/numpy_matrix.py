import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(A)
print(A.ndim)
print(A.shape)
print(A.size)
print(A[0:2, :])
print(A[:, 0:2])

M = np.array([[0, 1, 1], [1, 0, 1]])
N = np.array([[1, 1], [1, 1], [-1, 1]])

print(f'M = {M.shape}')
print(f'M = {N.shape}')

print(np.dot(M.transpose(), M))
print(np.dot(M, M.transpose()))

print(np.dot(M, N))   # Matrix multiplication
