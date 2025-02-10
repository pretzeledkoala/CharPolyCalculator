<link href="whirlwind.css" rel="stylesheet">

<whirlheader>
    <p>name</p>
    <p>Calculations</p>
    <p>date</p>
</whirlheader>

# Introduction 

Let $\mathfrak{s}$ be a solvable Lie algebra with Heisenberg nilradical $\mathfrak{h}(m)$ and $f$-dimensional extension. The Heisenberg algebra $\mathfrak{h}(m)$ has basis $\{h, p_1, \ldots, p_m, q_1, \ldots, q_m\}$ with commutation relations:
$$
[p_i, q_j] = \delta_{ij}h, \quad [p_i, p_j] = [q_i, q_j] = 0, \quad [p_i, h] = [q_i, h] = 0.
$$
The solvable extension adds elements $\{f_1, \ldots, f_f\}$ such that $\mathfrak{s} = \mathfrak{h}(m) \oplus \text{span}\{f_1, \ldots, f_f\}$. We investigate the polynomial:
$$
P(z_0, \ldots, z_{2m+f+1}) = \det(M),
$$
where 
$$
M=z_0 I + \sum_{i=1}^m z_i \text{ad}_{p_i} + \sum_{i=1}^m z_{m+i} \text{ad}_{q_i} + z_{2m+1} \text{ad}_{h} + \sum_{\alpha=1}^f z_{2m+\alpha+1} \text{ad}_{f_\alpha}.
$$
In particular, we provide a sharp upper bound for $k(L)$, the number of distinct roots of $P$.

# Theorem 

<theorem>

We have
$$
k(L)\le m+f+1
$$
Equality holds if and only if:
1. The extension elements $\{f_\alpha\}$ form a **commuting set**. That is, $[f_\alpha, f_\beta]=0$.
2. The matrices $X_\alpha \in \mathfrak{sp}(2m, \mathbb{F})$ are **simultaneously diagonalizable** with distinct eigenvalues,
3. The eigenvalues of $X_\alpha$ and $R_\alpha$ (extension commutators) are **distinct and non-overlapping**.

</theorem>

# Proof 

We proceed in 3 steps:

1. Construction of the matrix $M$
2. Diagonalization of $M$
3. Determinant of $M$

## Construction of the Matrix $M$

<theorem>

The adjoint actions for each of the basis elements are given as follows.

- **Adjoint action of $h$**:  
  $$
  \text{ad}_h(h) = 0, \quad \text{ad}_h(p_i) = 0, \quad \text{ad}_h(q_i) = 0, \quad \text{ad}_h(f_\alpha) = 2a_\alpha h.
  $$

- **Adjoint action of $p_i$**:  
  $$
  \text{ad}_{p_i}(h) = 0, \quad \text{ad}_{p_i}(p_j) = 0, \quad \text{ad}_{p_i}(q_j) = \delta_{ij} h, \quad \text{ad}_{p_i}(f_\alpha) = a_\alpha p_i + (X_\alpha)_{ij} p_j.
  $$

- **Adjoint action of $q_i$**:  
  $$
  \text{ad}_{q_i}(h) = 0, \quad \text{ad}_{q_i}(p_j) = -\delta_{ij} h, \quad \text{ad}_{q_i}(q_j) = 0, \quad \text{ad}_{q_i}(f_\alpha) = a_\alpha q_i + (X_\alpha)_{ij} q_j.
  $$

- **Adjoint action of $f_\alpha$**:  
  $$
  \text{ad}_{f_\alpha}(h) = -2a_\alpha h, \quad \text{ad}_{f_\alpha}(p_i) = a_\alpha p_i + (X_\alpha)_{ij} p_j, \quad \text{ad}_{f_\alpha}(q_i) = a_\alpha q_i + (X_\alpha)_{ij} q_j, \quad \text{ad}_{f_\alpha}(f_\beta) = r_{\alpha \beta} h.
  $$

</theorem>

To prove this, we need to do this in 3 parts:

1. The adjoints between the generators of the Heisenberg Lie algebra is easily recovered from the definition and is well known. 

2. To compute the adjoints with one $f_\alpha$, we use Theorem 11.1 of *Snobl and Winternitz*:

<theorem>

Every indecomposable solvable Lie algebra $s$ (over the field $F = \mathbb{C}$ or $F = \mathbb{R}$), containing the Heisenberg algebra $h(m)$ as its nilradical, can be written in a canonical basis $(h, p_1, \dots, p_m, q_1, \dots, q_m, f_1, \dots, f_f)$ with the commutation relations (11.4), supplemented by
$$
[f_\alpha, h], [f_\alpha, \xi] = (h, \xi) \cdot M_\alpha,
$$
$$
M_\alpha = \begin{pmatrix} 2a_\alpha & 0 \\ 0 & a_\alpha 1_{2m \times 2m} + X_\alpha \end{pmatrix},
$$
$$
[f_\alpha, f_\beta] = r_{\alpha \beta} h, \quad \alpha, \beta = 1, \dots, f.
$$
The vector $\xi$ is defined as
$$
\xi = (p_1, \dots, p_m, q_1, \dots, q_m).
$$

</theorem>

Using these adjoints, we now aim to construct
$$ 
M=z_0 I + \sum_{i=1}^m z_i \text{ad}_{p_i} + \sum_{i=1}^m z_{m+i} \text{ad}_{q_i} + z_{2m+1} \text{ad}_{h} + \sum_{\alpha=1}^f z_{2m+\alpha+1} \text{ad}_{f_\alpha}.
$$

From the adjoint actions, we can write the adjoint matrices in block form. Each generator acts as follows:

$$
  \text{ad}_h =  
  \begin{bmatrix} 
  0 & 0 & 0 & 0 \\ 
  0 & 0 & 0 & 0 \\ 
  0 & 0 & 0 & 0 \\ 
  0 & 0 & 0 & 0  
  \end{bmatrix}, \quad
  \text{ad}_{p_i} =  
  \begin{bmatrix} 
  0 & 0 & 0 & 0 \\ 
  0 & 0 & I_m & 0 \\ 
  0 & 0 & 0 & 0 \\ 
  0 & 0 & 0 & 0  
  \end{bmatrix},
  \quad
  \text{ad}_{q_i} =  
  \begin{bmatrix} 
  0 & 0 & 0 & 0 \\ 
  0 & 0 & 0 & 0 \\ 
  -I_m & 0 & 0 & 0 \\ 
  0 & 0 & 0 & 0  
  \end{bmatrix}, \quad
  \text{ad}_{f_\alpha} =
  \begin{bmatrix}
  -2a_\alpha & 0 & 0 & 0 \\ 
  0 & a_\alpha I_m + X_\alpha & 0 & 0 \\ 
  0 & 0 & a_\alpha I_m + X_\alpha & 0 \\ 
  0 & 0 & 0 & R
  \end{bmatrix}.
$$


Now, we build $M$ as:

$$
M = z_0 I + \sum_{i=1}^{m} z_i \text{ad}_{p_i} + \sum_{i=1}^{m} z_{m+i} \text{ad}_{q_i} + z_{2m+1} \text{ad}_h + \sum_{\alpha=1}^{f} z_{2m+\alpha+1} \text{ad}_{f_\alpha}.
$$

Expanding this using the block forms above:
$$
M =
\begin{bmatrix}
z_0 - 2\sum_{\alpha} z_{2m+\alpha+1} a_\alpha & 0 & 0 & 0 \\ 
0 & z_0 I_m + \sum_{\alpha} z_{2m+\alpha+1} (a_\alpha I_m + X_\alpha) & \sum_i z_i I_m & 0 \\ 
0 & -\sum_i z_{m+i} I_m & z_0 I_m + \sum_{\alpha} z_{2m+\alpha+1} (a_\alpha I_m + X_\alpha) & 0 \\ 
0 & 0 & 0 & z_0 I_f + \sum_{\alpha} z_{2m+\alpha+1} R
\end{bmatrix}
$$
where $R=(r_{\alpha \beta})$.





#### **Step 1: Block Triangularization of $M$**
After applying allowed transformations (symplectic alignment, scaling, and basis redefinition), the matrix $M$ becomes block upper triangular:
$$
M = \begin{pmatrix}
A & \mathbf{0} & \mathbf{0} & \mathbf{0} \\
\mathbf{0} & B & 0 & \mathbf{0} \\
\mathbf{0} & 0 & D & \mathbf{0} \\
\mathbf{0} & \mathbf{0} & \mathbf{0} & E
\end{pmatrix},
$$
where:
- $A = z_0 + 2 \sum_{\alpha=1}^f z_{2m+\alpha} a_\alpha$,
- $B = z_0 I + \sum_{\alpha=1}^f z_{2m+\alpha} (a_\alpha I + \Lambda_\alpha)$,
- $D = z_0 I + \sum_{\alpha=1}^f z_{2m+\alpha} (a_\alpha I - \Lambda_\alpha)$,
- $E = z_0 I + \sum_{\alpha=1}^f z_{2m+\alpha} R_\alpha$,
- $\Lambda_\alpha = \text{diag}(\lambda_\alpha^{(1)}, \ldots, \lambda_\alpha^{(m)})$ are diagonal symplectic eigenvalues.

#### **Step 2: Determinant Factorization**
The determinant factors as:
$$
\det(M) = \det(A) \cdot \det(B) \cdot \det(D) \cdot \det(E).
$$
- **Central term $A$:** Contributes $1$ root: $z_0 + 2 \sum_{\alpha=1}^f z_{2m+\alpha} a_\alpha$.
- **Heisenberg blocks $B/D$:** Each pair $(\lambda_\alpha^{(k)}, -\lambda_\alpha^{(k)})$ contributes $m$ distinct roots: 
  $$
  \prod_{k=1}^m \left(z_0 + \sum_{\alpha=1}^f z_{2m+\alpha} (a_\alpha + \lambda_\alpha^{(k)})\right) \left(z_0 + \sum_{\alpha=1}^f z_{2m+\alpha} (a_\alpha - \lambda_\alpha^{(k)})\right).
  $$
- **Extension block $E$:** Contributes $f$ distinct roots: 
  $$
  \prod_{\alpha=1}^f \left(z_0 + \sum_{\beta=1}^f z_{2m+\beta} r_{\alpha\beta}\right).
  $$

#### **Step 3: Distinctness of Roots**
Under the theorem’s assumptions:
1. **No eigenvalue overlaps**: The linear forms from $A$, $B/D$, and $E$ are distinct.
2. **Commutativity**: $R_\alpha$ are diagonal with distinct eigenvalues.

Thus, the total number of distinct roots is:
$$
k(L) = 1 + m + f.
$$

#### **Step 4: General Case (Non-Ideal Conditions)**
If the assumptions fail:
- Non-commuting extensions $\Rightarrow$ overlaps in $E$.
- Non-diagonalizable $X_\alpha$ $\Rightarrow$ repeated roots in $B/D$.
- Overlapping eigenvalues $\Rightarrow$ merged roots.

This reduces $k(L)$, so in general:
$$
k(L) \leq m + f + 1.
$$

---

### **Conclusion**
The equality $k(L) = m + f + 1$ holds **if and only if** the extension elements commute, act diagonally on the Heisenberg generators, and have distinct eigenvalues. The code’s counterexample violates these conditions (non-commuting $S_\alpha$), hence $k(L) < m + f + 1$. The refined theorem captures both ideal and general cases.

$$
\boxed{k(L) \leq m + f + 1}
$$