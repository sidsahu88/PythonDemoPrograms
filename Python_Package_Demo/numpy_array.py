import numpy as np


# Array is a list of same datatype. In python, list can have multiple datatype.
A = np.array([1, 2, 3, 4, 5])

print(A)
print(A[2])
print(type(A))
print(A.dtype)
print(A.size)
print(A.ndim)
print(A.shape)
print(A.max())

a = np.array([4, 1, 6, 8, 3, 7])
print(a.mean())

print(np.pi)
pi = np.pi

x = np.array([0, pi/2, pi])
print(x)

y = np.sin(x)
print(y)

b = np.array([[1], [2], [3]])
print(b**2)