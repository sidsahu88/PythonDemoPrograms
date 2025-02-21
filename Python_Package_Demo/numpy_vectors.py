import numpy as np

u = np.array([1, 0])
v = np.array([0, 1])

z1 = u + v  # Vector addition and subtraction is much faster than adding individual values in list.
z2 = u - v

print(z1)
print(z2)

x = np.array([2, 3])
y = np.array([3, 2])

z3 = 2 * x  # Similarly we can do scalar addition and subtraction
z4 = x * y  # Hadamard product (Multiply each elements with its counterpart)
z5 = np.dot(x, y)  # Dot product
z6 = x.dot(y)      # Dot product

print(z3)
print(z4)
print(z5)
print(z6)

print(np.identity(4))

print(np.ones((10, 1)))
