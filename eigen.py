import numpy as np

# Define the matrices
ad_x1 = np.array([
    [0, 0, 0, -1, 1],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
])

ad_x2 = np.array([
    [0, 0, 0, 0, 0],
    [0, 0, 0, -1, -1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
])

ad_x3 = np.array([
    [0, 0, 0, 0, 0],
    [-1, 0, 0, 0, 0],
    [0, 0, 0, 0, -2],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
])

ad_x4 = np.array([
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
])

ad_x5 = np.array([
    [-1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 2, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
])

# Compute eigenvalues for each matrix
eigenvalues_ad_x1 = np.linalg.eigvals(ad_x1)
eigenvalues_ad_x2 = np.linalg.eigvals(ad_x2)
eigenvalues_ad_x3 = np.linalg.eigvals(ad_x3)
eigenvalues_ad_x4 = np.linalg.eigvals(ad_x4)
eigenvalues_ad_x5 = np.linalg.eigvals(ad_x5)

# Print the eigenvalues
print("Eigenvalues of ad(x1):", eigenvalues_ad_x1)
print("Eigenvalues of ad(x2):", eigenvalues_ad_x2)
print("Eigenvalues of ad(x3):", eigenvalues_ad_x3)
print("Eigenvalues of ad(x4):", eigenvalues_ad_x4)
print("Eigenvalues of ad(x5):", eigenvalues_ad_x5)
