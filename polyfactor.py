import sympy as sp

def count_distinct_roots(polynomial_str):
    # Define the symbolic variables
    z0, z4, z3, z5 = sp.symbols('z0 z4 z3 z5')
    
    # Parse the polynomial from the string
    polynomial = sp.sympify(polynomial_str)

    # Solve the polynomial equation for z0 (find the roots with respect to z0)
    roots = sp.solve(polynomial, z0, domain=sp.CC)  # Solve for z0 in the complex field

    # Return the number of distinct roots
    return len(set(roots))

# Example usage
polynomial_str = "z0^2 + 1"
num_distinct_roots = count_distinct_roots(polynomial_str)
print(f"Number of distinct roots: {num_distinct_roots}")
