import numpy as np
from itertools import product
import sympy as sp

def adjoint_representation(x, basis):
    """
    Calculate the adjoint representation of a matrix x for any Lie algebra.
    ad(x)(y) = [x,y] = xy - yx
    """
    n = len(basis)
    ad_x = np.zeros((n, n), dtype=complex)  # Use dtype=complex to store complex numbers
    
    # Convert `x` and `basis` elements to sympy matrices
    x_sp = sp.Matrix(x)
    basis_sp = [sp.Matrix(b) for b in basis]
    
    # Calculate the action of x on each basis element
    for i, e in enumerate(basis_sp):
        # Calculate [x,e] = xe - ex
        commutator = x_sp * e - e * x_sp
        # Convert the result into coordinates with respect to the basis
        for j, b in enumerate(basis_sp):
            # Calculate the inner product
            denominator = sp.trace(b.T * b)  # Use sp.trace for symbolic matrices
            
            # Avoid division by zero
            if denominator != 0:
                ad_x[j, i] = sp.trace(b.T * commutator) / denominator
            else:
                ad_x[j, i] = 0  # You could handle this more carefully, if needed
            
    return ad_x

def count_distinct_roots(poly, z0):
    """
    Count the number of distinct complex roots in the polynomial.
    Uses the fact that the number of distinct roots equals the degree of the polynomial
    minus the degree of the GCD of the polynomial and its derivative.
    """
    # Get the polynomial in terms of z0 only (treating other variables as coefficients)
    z0_poly = sp.Poly(poly, z0)
    
    # Get the derivative with respect to z0
    z0_poly_derivative = z0_poly.diff(z0)
    
    # Calculate the GCD
    gcd = z0_poly.gcd(z0_poly_derivative)
    
    # The number of distinct roots is deg(poly) - deg(gcd)
    total_degree = z0_poly.degree()
    gcd_degree = gcd.degree()
    
    return total_degree - gcd_degree

def characteristic_polynomial(basis, debug=True):
    """
    Calculate det(z_0 I + z_1 ad(x_1) + ... + z_n ad(x_n))
    General version for any Lie algebra
    """
    # Calculate adjoint representations
    ad_matrices = [adjoint_representation(x, basis) for x in basis]
    
    if debug:
        print("\nAdjoint representations:")
        for i, ad_mat in enumerate(ad_matrices):
            print(f"\nad(x_{i+1}):")
            print(ad_mat)
    
    # Create symbolic variables
    n = len(basis)
    z = [sp.Symbol(f'z{i}') for i in range(n+1)]
    
    # Construct the matrix
    dim = len(basis)  # dimension of the Lie algebra
    matrix = z[0] * sp.eye(dim)  # Start with z_0 * I
    for i, ad_mat in enumerate(ad_matrices):
        matrix += z[i+1] * sp.Matrix(ad_mat)
    
    # Calculate and expand the determinant
    return sp.expand(matrix.det()), z[0]

if __name__ == "__main__":
    # Define the basis here with complex numbers

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
    # Specify number of terms in the basis
    basis = [x1, x2, x3, x4, x5, S1, S2, S3]
    
    print("Original basis matrices:")
    for i, b in enumerate(basis):
        print(f"\nx_{i+1} =")
        print(b)
    
    poly, z0 = characteristic_polynomial(basis, debug=True)
    
    print("\nCharacteristic polynomial:")
    print(poly)
    
    # Count distinct roots
    num_roots = count_distinct_roots(poly, z0)
    print(f"\nNumber of distinct roots over C: {num_roots}")
