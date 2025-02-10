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
In particular, we determine $k(L)$, the number of distinct roots of $P$.

# Calculations 

## 3D Heisenberg 
The 3D Heisenberg Lie algebra:
$$
p_1 = \begin{pmatrix} 
0 & 1 & 0 \\
0 & 0 & 0 \\
0 & 0 & 0
\end{pmatrix}
\quad
q_1 = \begin{pmatrix} 
0 & 0 & 1 \\
0 & 0 & 0 \\
0 & 0 & 0
\end{pmatrix}
\quad
h = \begin{pmatrix} 
0 & 0 & 0 \\
0 & 0 & 1 \\
0 & 0 & 0
\end{pmatrix}
$$

### 3D+1D Extension

There are 3 possibilities

1. We have
    $$
    M^{(1)} =
    \begin{pmatrix}
    2 & 0 & 0  \\
    0 & 1+b & 0 \\
    0 & 0 & 1-b
    \end{pmatrix}, \quad b \geq 0,
    $$
    which gives 
    $$\det \begin{pmatrix}
    z_0 + 2z_4 & z_1 & z_2 \\ 
    0 & z_0 +(1+b)z_4 & z_3 \\ 
    0 & 0 & z_0+(1-b)z_4
    \end{pmatrix} = (z_0 + 2z_4)(z_0 + (1+b)z_4)(z_0 + (1-b)z_4)$$
    Then 
    $$
    k(L) = \begin{cases} 2 &\text{if } b=0,1 \\ 
    3 & \text{otherwise}\end{cases}
    $$

2.  We have 
    $$
    M^{(2)} =
    \begin{pmatrix}
    2 & 0 & 0 \\
    0 & 1 & 1 \\
    0 & 0 & 1
    \end{pmatrix},
    $$ 
    which gives
    $$
    \det \begin{pmatrix}
    z_0+2z_4 & z_1 & z_2 \\ 
    0 & z_0+z_4 & z_3+z_4 \\ 
    0 & 0 & z_0+z_4
    \end{pmatrix} =  (z_0+2z_4)(z_0+z_4)^2
    $$
    Then 
    $$ k(L)=2 $$

3. We have 
    $$
    M^{(2)} =
    \begin{pmatrix}
    0 & 0 & 0 \\
    0 & 1 & 0 \\
    0 & 0 & -1
    \end{pmatrix},
    $$ 
    which gives
    $$
    \det \begin{pmatrix}
    z_0+2z_4 & z_1 & z_2 \\ 
    0 & z_0+z_4 & z_3+z_4 \\ 
    0 & 0 & z_0+z_4
    \end{pmatrix} = (z_0+2z_4)(z_0+z_4)^2
    $$
    Then 
    $$ k(L)=2 $$

### 3D+2D Extension

There is 1 possibility:

We have 
$$
M_1 = \begin{pmatrix} 2 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}, \quad M_2 = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & -1 \\ 0 & 1 & 0 \end{pmatrix}
$$
which gives 
$$
\det\begin{pmatrix} 
z_0+2z_4 & z_1 & z_2 \\ 
0 & z_0+z_4 & z_3-z_5 \\ 
0 & z_5 & z_0+z_4
\end{pmatrix} = (z_0+2z_4) \left[ (z_0+z_4)^2 - z_3z_5 + z_5^2 \right].
$$
Then 
$$ k(L)=2 $$

## 5D Heisenberg
The 5D Heisenberg Lie algebra:
$$
p_1= \begin{pmatrix}
0 & 1 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0
\end{pmatrix}, \quad
p_2 = \begin{pmatrix}
0 & 0 & 0 & 1 & 0 \\
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0
\end{pmatrix}, \quad
q_1 =\begin{pmatrix}
0 & 0 & 1 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0
\end{pmatrix}$$
$$
q_2 = \begin{pmatrix}
0 & 0 & 0 & 0 & 1 \\
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0
\end{pmatrix}, \quad
h=\begin{pmatrix}
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0
\end{pmatrix}.
$$

### 5D+1D Extension 


### 5D+2D Extension 


### 5D+3D Extension