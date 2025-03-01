import numpy as np

# Define corrected 5x5 matrices
p1 = np.array([[0, 1, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0]])

p2 = np.array([[0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0]])

q1 = np.array([[0, 0, 0, 0, 0],
               [0, 0, 0, 0, 1],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0]])

q2 = np.array([[0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 1],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0]])

h = np.array([[0, 0, 0, 0, 1],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0]])

# Function to compute commutator
def commutator(A, B):
    return np.dot(A, B) - np.dot(B, A)

# Check the Heisenberg Lie algebra conditions
check1 = np.allclose(commutator(p1, q1), h) and np.allclose(commutator(p2, q2), h)
check2 = np.allclose(commutator(p1, q2), np.zeros((5, 5))) and np.allclose(commutator(p2, q1), np.zeros((5, 5)))
check3 = np.allclose(commutator(p1, p2), np.zeros((5, 5))) and np.allclose(commutator(q1, q2), np.zeros((5, 5)))
check4 = np.allclose(commutator(p1, h), np.zeros((5, 5))) and np.allclose(commutator(p2, h), np.zeros((5, 5)))
check5 = np.allclose(commutator(q1, h), np.zeros((5, 5))) and np.allclose(commutator(q2, h), np.zeros((5, 5)))

# Print results
if check1 and check2 and check3 and check4 and check5:
    print("The corrected matrices satisfy the 5D Heisenberg Lie algebra relations.")
else:
    print("The corrected matrices do NOT satisfy the 5D Heisenberg Lie algebra relations.")

# Print computed commutators for verification
print("\nComputed Commutators:")
print("[p1, q1]:\n", commutator(p1, q1))
print("[p2, q2]:\n", commutator(p2, q2))
print("[p1, q2]:\n", commutator(p1, q2))
print("[p2, q1]:\n", commutator(p2, q1))
print("[p1, p2]:\n", commutator(p1, p2))
print("[q1, q2]:\n", commutator(q1, q2))
print("[p1, h]:\n", commutator(p1, h))
print("[p2, h]:\n", commutator(p2, h))
print("[q1, h]:\n", commutator(q1, h))
print("[q2, h]:\n", commutator(q2, h))