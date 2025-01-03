# Generators for su(2)
x1 = np.array([[0, 1], [1, 0]], dtype=complex)
x2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
x3 = np.array([[1, 0], [0, -1]], dtype=complex)

# Generators for so(3)
x1 = np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], dtype=complex)
x2 = np.array([[0, 0, 1j], [0, 0, 0], [-1j, 0, 0]], dtype=complex)
x3 = np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], dtype=complex)

# Generators for so(4)
x1 = np.array([[0, 0, 0, 0], [0, 0, -1, 0], [0, 1, 0, 0], [0, 0, 0, 0]])
x2 = np.array([[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 0, 0], [0, -1, 0, 0]])
x3 = np.array([[0, 0, 0, -1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]])
x4 = np.array([[0, 0, 1, 0], [0, 0, 0, 0], [-1, 0, 0, 0], [0, 0, 0, 0]])

# Generators for sp(4)
x1 = np.array([[0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 0, 0], [1, 0, 0, 0]])
x2 = np.array([[0, 0, 0, -1], [0, 0, -1, 0], [0, 0, 0, 0], [-1, 0, 0, 0]])
x3 = np.array([[0, 0, 1, 0], [0, 0, 0, 1], [-1, 0, 0, 0], [0, -1, 0, 0]])
x4 = np.array([[0, 0, -1, 0], [0, 0, 0, -1], [1, 0, 0, 0], [0, 1, 0, 0]])

# Generators for g2
x1 = np.array([[0, 1, 0], [0, 0, 1], [0, 0, 0]])
x2 = np.array([[0, 0, -1], [0, 0, 0], [1, 0, 0]])
x3 = np.array([[0, 0, 0], [1, 0, 0], [0, 1, 0]])
x4 = np.array([[0, -1, 0], [0, 0, 0], [0, 0, 0]])
x5 = np.array([[0, 0, 1], [-1, 0, 0], [0, 0, 0]])
x6 = np.array([[0, 0, 0], [0, 0, -1], [0, 1, 0]])

# Generators for f4
x1 = np.array([[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [0, 0, 0, 0]])
x2 = np.array([[0, 0, -1, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, -1, 0, 0]])
x3 = np.array([[0, 0, 1, 0], [0, 0, 0, -1], [-1, 0, 0, 0], [0, 1, 0, 0]])
x4 = np.array([[0, -1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, -1, 0]])

# Generators for su(3)
x1 = np.array([[0, 1, 0], [0, 0, 0], [0, 0, 0]])
x2 = np.array([[0, 0, 1], [0, 0, 0], [0, 0, 0]])
x3 = np.array([[0, 0, 0], [1, 0, 0], [0, 0, 0]])
x4 = np.array([[0, 0, 0], [0, 0, 1], [0, 0, 0]])
x5 = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])

# Generators for so(5)
x1 = np.array([[0, 0, 0, 0, 1], [0, 0, 0, -1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 1], [1, 0, 0, 0, 0]])
x2 = np.array([[0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [-1, 0, 0, 0, 0], [0, -1, 0, 0, 0], [0, 0, 0, 0, 0]])
x3 = np.array([[0, 0, 0, 1, 0], [0, 0, 0, 0, 1], [0, 0, 0, -1, 0], [1, 0, 0, 0, 0], [0, 1, 0, 0, 0]])
x4 = np.array([[0, 0, 0, 0, 1], [0, 0, 1, 0, 0], [0, -1, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0]])

# Generators for sp(6)
x1 = np.array([[0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, -1], [-1, 0, 0, 0, 0, 0]])
x2 = np.array([[0, 0, 0, 0, 0, -1], [0, 0, 0, 0, -1, 0], [0, 0, 0, 0, 0, -1], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0]])
x3 = np.array([[0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
x4 = np.array([[0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0]])

# Generators for e6
x1 = np.array([[0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0]])
x2 = np.array([[0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, -1], [1, 0, 0, 0, 0, 0]])
x3 = np.array([[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1]])

# Generators for e7
x1 = np.array([[0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0], [1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0]])
x2 = np.array([[0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, -1], [0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0]])
