import numpy as np
import sympy as sp

def adjoint_representation(x, basis):
    """
    Calculate the adjoint representation of a matrix x for any Lie algebra.
    ad(x)(y) = [x,y] = xy - yx
    """
    n = len(basis)
    ad_x = sp.zeros(n, n)  # Initialize as a symbolic matrix
    
    # Convert `x` and `basis` elements to sympy matrices
    x_sp = sp.Matrix(x)
    basis_sp = [sp.Matrix(b) for b in basis]
    
    # Calculate the action of x on each basis element
    for i, e in enumerate(basis_sp):
        # Calculate [x,e] = xe - ex
        commutator = x_sp * e - e * x_sp
        # Convert the result into coordinates with respect to the basis
        for j, b in enumerate(basis_sp):
            # Calculate the inner product using symbolic matrix multiplication
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
            sp.pprint(ad_mat)
    
    # Create symbolic variables
    n = len(basis)
    z = [sp.Symbol(f'z{i}') for i in range(n+1)]
    
    # Construct the matrix
    dim = len(basis)  # dimension of the Lie algebra
    matrix = z[0] * sp.eye(dim)  # Start with z_0 * I
    for i, ad_mat in enumerate(ad_matrices):
        matrix += z[i+1] * sp.Matrix(ad_mat)
    
    # Print the matrix before calculating the determinant
    print("\nMatrix before determinant:")
    sp.pprint(matrix)
    
    # Calculate and expand the determinant
    det_poly = sp.expand(matrix.det())
    
    # Factor the characteristic polynomial
    factored_poly = sp.factor(det_poly)
    
    return factored_poly, det_poly, z[0]

if __name__ == "__main__":
    # Define the basis here with the new 3x3 matrices
    p1 = np.array([[0, 1, 0], [0, 0, 0], [0, 0, 0]]) # p₁
    q1 = np.array([[0, 0, 0], [0, 0, 1], [0, 0, 0]]) # p₁
    h = np.array([[0, 0, 1], [0, 0, 0], [0, 0, 0]]) # p₁
    e1 = np.array([[2, 0, 0], [0, 1, 0], [0, 0, 1]]) # p₁
    e2 = np.array([[0, 0, 0], [0, 1, 0], [0, 0, -1]]) # p₁

    # Specify number of terms in the basis
    basis = [p1, q1, h, e1, e2]
    
    print("Original basis matrices:")
    for i, b in enumerate(basis):
        print(f"\nx_{i+1} =")
        print(b)
    
    factored_poly, det_poly, z0 = characteristic_polynomial(basis, debug=True)
    
    # Print the factored form of the characteristic polynomial
    print("\nFactored form of the characteristic polynomial:")
    print(factored_poly)
    
    # Count distinct roots
    num_roots = count_distinct_roots(det_poly, z0)
    print(f"\nNumber of distinct roots over C: {num_roots}")