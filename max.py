import numpy as np

def commutator(X, Y):
    """Calculate the commutator [X, Y] = XY - YX."""
    return np.dot(X, Y) - np.dot(Y, X)

def adjoint_representation(element, lie_algebra):
    """
    Calculate the adjoint representation of a Lie algebra element.
    Args:
    - element: A matrix corresponding to the Lie algebra element.
    - lie_algebra: A list of matrices corresponding to the generators of the Lie algebra.
    
    Returns:
    - The matrix representation of the adjoint of `element`.
    """
    adj_matrix = []
    for e in lie_algebra:
        adj_matrix.append(commutator(element, e))
    
    return np.array(adj_matrix)

def distinct_eigenvalues(matrix):
    """Return the number of distinct eigenvalues of a matrix."""
    eigenvalues = np.linalg.eigvals(matrix)
    distinct_eigenvalues = len(np.unique(np.round(eigenvalues, decimals=10)))  # rounding to avoid floating point issues
    return distinct_eigenvalues

def max_distinct_eigenvalues(lie_algebra):
    """
    For each element of the Lie algebra, compute the adjoint representation and the number of distinct eigenvalues,
    then return the maximum number of distinct eigenvalues.
    """
    max_distinct = 0
    
    for element in lie_algebra:
        # Compute the adjoint representation for the element
        adj_matrix = adjoint_representation(element, lie_algebra)
        
        # Compute the number of distinct eigenvalues
        num_distinct = distinct_eigenvalues(adj_matrix)
        
        # Update the maximum number of distinct eigenvalues
        max_distinct = max(max_distinct, num_distinct)
    
    return max_distinct

# Example: 1D extension input in the requested format

# Define each generator as an individual variable
x1 = np.array([[0,1,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]])  # P₁
x2 = np.array([[0,0,1,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]])  # B₁
x3 = np.array([[0,0,0,1,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]])  # P₂
x4 = np.array([[0,0,0,0,1], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]])  # B₂
x5 = np.array([[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]])  # H (central)

# Case F6: Non-nilpotent, non-diagonal
S1 = np.array([
    [2, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1]
    ])

S2 = np.array([
        [0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, -1, 0],
        [0, 0, 0, 0, 0]
        ])

S3 = np.array([
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, -1]
        ])

# Now compute the maximum distinct eigenvalues from the adjoint representation
extended = [x1, x2, x3, x4, x5, S1, S2, S3]

# Compute the result
result = max_distinct_eigenvalues(extended)
print("Maximum number of distinct eigenvalues:", result)
