<link href="../whirlwind.css" rel="stylesheet">

<whirlheader>
<p>name</p>
<p>Calculations</p>
<p>date</p>
</whirlheader>

# Spectral Equivalence for Matrices 
Consider $M\in \text{Mat}_{k\times k}$, and define 
$$
\det(z_0I+z_1M).
$$

<definition>

Two matrices $M_1$ and $M_2$ are spectrally equivalent if there exixists A\in GL$ such that $P_1(z)=P_2(zA)$. We write $M_1 \stackrel{SE}{\sim} M_2$ if $M_1$ and $M_2$ are spectrally equivalent.

</definition>

<proposition>

$M_1 \stackrel{SE}{\cong} M_2$ if and only if $|\sigma(M_1)|=|\sigma(M_2)|$ and up to permutation $\sigma(M_1)$ and $\sigma(M_2)$ have the same sequence of multiplicities.

</proposition>

<definition>

The spectral data is defined as given $|\sigma(M)|=d$, the sequence $(k_1,...,k_d)$ where $k_i \le k_{i+1}$ and $k_i$'s are the multiplicities of the eigenvalues.

</definition>

<example>

$\sigma(M)=\{2,2,\pi, \pi, \pi, 1, 4\}$, then $|\sigma(M)|=4$ and the spectral data is $(1,1,2,3)$

</example>

<conjecture>

$M_1 \stackrel{SE}{\cong} M_2$ if and only if they have the same spectral data.

</conjecture>


## Proof 
Backward direction: Assume $M_1 \stackrel{SE}{\sim} M_2$, meaning there exists an invertible matrix $A \in GL_k$ such that  
$$
P_1(z) = P_2(zA).
$$  
By definition, the characteristic polynomials satisfy  
$$
\det(z_0 I + z_1 M_1) = \det(z_0 I + z_1 M_2 A).
$$  
Since determinant operations preserve eigenvalues, this transformation does not alter the set of absolute values of the eigenvalues of $M_1$, nor does it change their multiplicities. Hence, $M_1$ and $M_2$ must have the same eigenvalue multiplicities when counted appropriately. By definition of spectral data, this means $M_1$ and $M_2$ share the same spectral data.

Converse direction: Now, suppose $M_1$ and $M_2$ have the same spectral data. By definition, this means their eigenvalues have the same absolute values, appearing with the same multiplicities. From the proposition, two matrices satisfying this condition must be spectrally equivalent, meaning there exists $A \in GL_k$ such that  
$$
P_1(z) = P_2(zA).
$$  
By the definition of spectral equivalence, this confirms that $M_1 \stackrel{SE}{\sim} M_2$, completing the proof.


# Applying the Matrices to Our Problem

<problem>

Suppose $L$ is solvable Lie algebra that is a 1-dimensional extension of an $n$-dimensional nilrdadical $\{x_1,...,x_n, x_{n+1}\} =L$. We define $Q_L(z) = \det \left( z_0 I + z_1 \text{ad} \, x_1 + \dots + z_n \text{ad} \, x_n \right).$ $L$ and $L'$ are spectrally equivalent if and only if $\text{ad}x_{n+1}$ and $\text{ad}x_{n+1}'$ are spectrally equivalent. 

</problem>