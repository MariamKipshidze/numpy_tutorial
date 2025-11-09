import numpy as np

# From Python lists
a = np.array([1, 2, 3])
b = np.array([[1, 2, 3], [4, 5, 6]])

print("a:", a)
print("b:\n", b)

# From built-in functions
zeros = np.zeros((2, 3))
ones = np.ones((2, 2))
rand = np.random.rand(3, 2)
arange = np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]
linspace = np.linspace(0, 1, 5)  # 5 evenly spaced points between 0 and 1

print("\nzeros:\n", zeros)
print("\nones:\n", ones)
print("\nrand:\n", rand)
print("\narange:", arange)
print("\nlinspace:", linspace)
