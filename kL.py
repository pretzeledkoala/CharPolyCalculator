import numpy as np
import sympy as sp

class LieAlgebraRootCalculator:
    def __init__(self, generators):
        """
        Initialize the Lie algebra calculator
        
        Parameters:
        generators (list of numpy.ndarray): List of matrices generating the Lie algebra
        """
        self.generators = generators
        self.dim = generators[0].shape[0]
    
    def compute_adjoint_representations(self):
        """
        Compute the adjoint representations of the generators
        
        Returns:
        list of numpy.ndarray: Adjoint representations of each generator
        """
        adjoint_reps = []
        for gen in self.generators:
            # Compute adjoint representation as a matrix
            adj_rep = np.zeros_like(gen, dtype=complex)  # Use complex dtype
            for other_gen in self.generators:
                # Compute the commutator [gen, other_gen]
                adj_rep += np.matmul(gen, other_gen) - np.matmul(other_gen, gen)
            adjoint_reps.append(adj_rep)
        return adjoint_reps
    
    def symbolic_characteristic_polynomial(self):
        """
        Compute the symbolic characteristic polynomial
        
        Returns:
        sympy expression: The characteristic polynomial
        """
        # Create symbolic variables
        z = [sp.Symbol(f'z_{i}') for i in range(len(self.generators)+1)]
        
        # Create symbolic matrix
        I = sp.eye(self.dim)
        symbolic_matrix = z[0] * I
        
        # Add adjoint representations
        adjoint_reps = self.compute_adjoint_representations()
        for i, adj_rep in enumerate(adjoint_reps, 1):
            symbolic_matrix += z[i] * sp.Matrix(adj_rep)
        
        # Compute determinant
        char_poly = sp.simplify(sp.det(symbolic_matrix))
        return char_poly
    
    def count_distinct_roots(self):
        """
        Count the number of distinct roots of the characteristic polynomial
        
        Returns:
        int: Number of distinct roots
        """
        # Create symbolic variables
        z = [sp.Symbol(f'z_{i}') for i in range(len(self.generators)+1)]
        
        # Get the characteristic polynomial
        char_poly = self.symbolic_characteristic_polynomial()
        
        # Expand the polynomial
        expanded_poly = sp.expand(char_poly)
        
        # Solve the polynomial equation
        try:
            # Use solve to find roots
            roots = sp.solve(expanded_poly, z[0])
            
            # Convert roots to a set of unique values
            distinct_roots = set(map(str, roots))
            
            return len(distinct_roots)
        except Exception as e:
            print(f"Error finding roots: {e}")
            return 0

# Example usage
def main():
    # Use `1j` for complex numbers in Python (instead of `1i`)
    # x1 = np.array([[0, 1], [1, 0]], dtype=complex)
    # x2 = np.array([[0, -1j], [1j, 0]], dtype=complex)  # Correct complex number
    # x3 = np.array([[1, 0], [0, -1]], dtype=complex)

    x1 = np.array([[0, 1], [0, 0]], dtype=complex)  # x1
    x2 = np.array([[0, 0], [0, 0]], dtype=complex)  # x2
    x3 = np.array([[1, 0], [0, 0]], dtype=complex)  # x3 (central element)

    calculator = LieAlgebraRootCalculator([x1, x2])
    
    print("Adjoint Representations:")
    for i, adj_rep in enumerate(calculator.compute_adjoint_representations(), 1):
        print(f"ad(x_{i}):\n", adj_rep)
    
    print("\nCharacteristic Polynomial:")
    char_poly = calculator.symbolic_characteristic_polynomial()
    print(char_poly)
    
    print("\nNumber of Distinct Roots:")
    num_roots = calculator.count_distinct_roots()
    print(num_roots)

if __name__ == "__main__":
    main()
