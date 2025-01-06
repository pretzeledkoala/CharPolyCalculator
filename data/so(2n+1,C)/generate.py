import numpy as np

# Create a list to store the matrices
so3_basis = []

# Generate the matrices x_ij where 1 <= i < j <= 3
for i in range(3):
    for j in range(i+1, 3):
        # Initialize a 3x3 zero matrix
        x_ij = np.zeros((3, 3), dtype=complex)
        
        # Set the (i, j) position to 1 and (j, i) position to -1
        x_ij[i, j] = 1
        x_ij[j, i] = -1
        
        # Append the matrix to the list
        so3_basis.append(x_ij)

# Print the resulting basis matrices
for idx, matrix in enumerate(so3_basis, 1):
    print(f"x{idx} = np.array({matrix.tolist()})\n")
