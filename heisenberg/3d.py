import numpy as np

# Define corrected 3x3 matrices
p1 = np.array([[0, 1, 0],
               [0, 0, 0],
               [0, 0, 0]])

q1 = np.array([[0, 0, 0],
               [0, 0, 1],
               [0, 0, 0]])

h = np.array([[0, 0, 1],
              [0, 0, 0],
              [0, 0, 0]])

# Function to compute commutator
def commutator(A, B):
    return np.dot(A, B) - np.dot(B, A)

# Check the Heisenberg Lie algebra conditions
check1 = np.allclose(commutator(p1, q1), h)
check2 = np.allclose(commutator(p1, q1), np.zeros((3, 3)))  # No q2 or p2 to check against
check3 = np.allclose(commutator(p1, p1), np.zeros((3, 3))) and np.allclose(commutator(q1, q1), np.zeros((3, 3)))
check4 = np.allclose(commutator(p1, h), np.zeros((3, 3)))
check5 = np.allclose(commutator(q1, h), np.zeros((3, 3)))

# Print results
if check1 and check2 and check3 and check4 and check5:
    print("The corrected matrices satisfy the 3D Heisenberg Lie algebra relations.")
else:
    print("The corrected matrices do NOT satisfy the 3D Heisenberg Lie algebra relations.")

# Print computed commutators for verification
print("\nComputed Commutators:")
print("[p1, q1]:\n", commutator(p1, q1))
print("[p1, p1]:\n", commutator(p1, p1))
print("[q1, q1]:\n", commutator(q1, q1))
print("[p1, h]:\n", commutator(p1, h))
print("[q1, h]:\n", commutator(q1, h))
