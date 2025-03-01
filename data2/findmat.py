import sympy as sp

# Define variables
z0, z6, b = sp.symbols('z0 z6 b')
B = sp.Matrix(8, 8, lambda i, j: sp.Symbol(f'B{i}{j}'))  # 8x8 matrix with symbolic elements

# Define polynomials
Q1 = z0**3 * (z0 + z6)**3
Q2 = z0**3 * (-b * z6 + z0)**3

# Focus only on the relevant transformed variables (z0 and z6)
z0_transformed = sum(B[0, j] * sp.Symbol(f'z{j}') for j in range(8))
z6_transformed = sum(B[6, j] * sp.Symbol(f'z{j}') for j in range(8))

# Substitute transformed variables into Q2
Q2_transformed = Q2.subs({z0: z0_transformed, z6: z6_transformed})

# Expand polynomials
Q1_expanded = sp.expand(Q1)
Q2_transformed_expanded = sp.expand(Q2_transformed)

# Collect coefficients for comparison
monomials_Q1 = Q1_expanded.as_coefficients_dict()
monomials_Q2 = Q2_transformed_expanded.as_coefficients_dict()

# Set up system of equations to match coefficients
relevant_eqs = [monomials_Q1[mon] - monomials_Q2.get(mon, 0) for mon in monomials_Q1]

# Solve for only the relevant elements of B
solution = sp.solve(relevant_eqs, [B[0, j] for j in range(8)] + [B[6, j] for j in range(8)])

# Check and print results
if solution:
    print("An invertible matrix B exists:")
    sp.pprint(solution)
else:
    print("No such invertible matrix B exists.")
