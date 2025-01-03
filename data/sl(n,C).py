import numpy as np

# Generators for sl(2, C)
x1 = np.array([[0, 1], [0, 0]])
x2 = np.array([[0, 0], [1, 0]])
x3 = np.array([[1, 0], [0, -1]])

# Generators for sl(3, C)
x1 = np.array([[0, 1, 0], [0, 0, 0], [0, 0, 0]])
x2 = np.array([[0, 0, 0], [1, 0, 0], [0, 0, 0]])
x3 = np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]])
x4 = np.array([[0, 0, 1], [0, 0, 0], [0, 0, 0]])
x5 = np.array([[0, 0, 0], [0, 0, 1], [0, 0, 0]])
x6 = np.array([[0, 0, 0], [0, 0, 0], [1, 0, 0]])
x7 = np.array([[0, 0, 0], [0, 0, 0], [0, 1, -1]])
x8 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]])