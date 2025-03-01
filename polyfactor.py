import sympy as sp

def count_distinct_roots(polynomial_str):
    # Define the symbolic variables
    z0, z2, z5, z4 = sp.symbols('z0 z2 z5 z4')
    
    # Parse the polynomial from the string
    polynomial = sp.sympify(polynomial_str)

    # Solve the polynomial equation for z0 (find the roots with respect to z0)
    roots = sp.solve(polynomial, z0, domain=sp.CC)  # Solve for z0 in the complex field

    # Return the number of distinct roots
    return len(set(roots))

# Example usage
polynomial_str = "z0**3*(z0**2 + 2*z0*z4 - z2*z5 + z4**2 + z5**2)"
num_distinct_roots = count_distinct_roots(polynomial_str)
print(f"Number of distinct roots: {num_distinct_roots}")
