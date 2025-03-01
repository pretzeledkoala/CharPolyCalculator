<link href="whirlwind.css" rel="stylesheet">

<whirlheader>
<p>name</p>
<p>Calculations</p>
<p>date</p>
</whirlheader>


# Spectral Equivalence of Parameterized Families of Solvable Lie Algebras with Heisenberg Nilradical

# Heisenberg Algebras and Polynomials

# Background

## Solvable Lie Algebras with Heisenberg Nilradical

The Heisenberg algebra is a nilpotent Lie algebra that plays a fundamental role in quantum mechanics, symplectic geometry, and representation theory. It is defined as follows:

<definition>  

The **Heisenberg algebra** $\mathfrak{h}(m)$ has a basis 

$$
\{h, p_1, \dots, p_m, q_1, \dots, q_m\}
$$  

with the commutation relations:  

$$
[p_i, q_j] = \delta_{ij}h, \quad [p_i, p_j] = [q_i, q_j] = 0, \quad [p_i, h] = [q_i, h] = 0.
$$  

</definition>  

We will work mostly in the $\mathfrak{h}(1)$ and $\mathfrak{h}(2)$ cases, which correspond to the 3d and 5d Heisenberg algebras. Their generators can be explicitly written as 
$$p_1 =
\begin{bmatrix}
0 & 1 & 0 \\
0 & 0 & 0 \\
0 & 0 & 0
\end{bmatrix}
\quad
q_1 =
\begin{bmatrix}
0 & 0 & 0 \\
0 & 0 & 1 \\
0 & 0 & 0
\end{bmatrix}
\quad
h =
\begin{bmatrix}
0 & 0 & 1 \\
0 & 0 & 0 \\
0 & 0 & 0
\end{bmatrix}$$
for the 3d case and 
$$
p_1 = \begin{bmatrix}
0 & 1 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0
\end{bmatrix}, \quad 
p_2 = \begin{bmatrix}
0 & 0 & 1 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0
\end{bmatrix}, \quad
q_1 = \begin{bmatrix}
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 1 \\
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0
\end{bmatrix}
$$

$$
q_2 = \begin{bmatrix}
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 1 \\
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0
\end{bmatrix}, \quad
h = \begin{bmatrix}
0 & 0 & 0 & 0 & 1 \\
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0
\end{bmatrix}
$$
for the 5d case. One can verify that these satisfy the Heisenberg relations.

Although the Heisenberg algebra is interesting and rich in theory in its own right, our primary focus lie in the study of extending these Lie algebras to make them solvable. Following \cite{Rubin1993}, let $\mathfrak{s}$ be a solvable Lie algebra with Heisenberg nilradical $\mathfrak{h}(m)$ and an $f$-dimensional extension. To construct this solvable extension, we introduce additional elements $\{f_1, \dots, f_f\}$ such that  
$$
\mathfrak{s} = \mathfrak{h}(m) \oplus \text{span}\{f_1, \dots, f_f\}.
$$  

The classification of such Lie algebras $\mathfrak{s}$ over $\mathbb{C}$ has been extensively carried out in the low-dimensional cases, particularly for those with nilradicals $\mathfrak{h}(1)$ and $\mathfrak{h}(2)$. More comprehensive classification results are also available (see \cite{Rubin1993}), including those over $\mathbb{R}$. However, explicit constructions of solvable Lie algebras with higher-dimensional Heisenberg nilradicals over any field remain absent in the literature. For the purposes of this paper, we restrict our attention to the base field $\mathbb{C}$.

There are 25 such families of $\mathfrak{s}$. A summary of the results found in \cite{?} is presented in the table below.

<center>

| The Pair $(\dim \mathfrak{h},\dim f)$ | Total Dimension | Number of Families |
|---|---|---|
| (3, 1) | 4 | 3 |
| (3, 2) | 5 | 1 |
| (5, 1) | 6 | 12 |
| (5, 2) | 7 | 8 |
| (5, 3) | 8 | 1 |

</center>

11 of the families are parameterized, which are of particular interest for this paper.

<center>

| The Pair $(\dim \mathfrak{h}, \dim f)$ | 1 Parameter Families | 2 Parameter Families |
|---|---|---|
| (3, 1) | 1 | 0 |
| (5, 1) | 4 | 2 |
| (5, 2) | 3 | 1 |

</center>

From now on, we will let $\mathfrak{s}_{\dim \mathfrak{h}, \dim f}^{e_1,e_2}$ denote the solvable Lie algebra $\mathfrak{s}$ with Heisenberg nilradical $\mathfrak{h}$ and $f$-dimensional extension, the $e_2$th case of such Lie algebra with $e_1$ parameters. We write $\mathfrak{s}_{\dim \mathfrak{h}, \dim f}^{e_1,e_2,e_3}$ if we want to evaluate this family at a specific parameter $e_3$, where $e_3$ is a number for 1 parameter cases and an unordered pair for 2 parameter cases.

## The Invariant $k(L)$ and Spectral Equivalence

\cite{Yang2020} introduced an analogue of the characteristic polynomial specifically for solvable Lie algebras $L$ with a basis ${x_1, x_2, \dots, x_n}$, defined as follows:

<definition>

[\cite{Yang2020}]

For a solvable Lie algebra, the **characteristic polynomial** $Q_L(z)$ is given by the determinant of the linear pencil
$$
Q(z) = \det \left( z_0 I + z_1 \text{ad} \, x_1 + \dots + z_n \text{ad} \, x_n \right).
$$

</definition>

We discuss the number of distinct factors of the characteristic polynomial, denoted $k(L)$, of the characteristic polynomial for solvable Lie algebras $\mathfrak{s}$ with Heisenberg nilradical $\mathfrak{h}(m)$ and an $f$-dimensional extension over the base field $\mathbb{C}$. There are known formulas for calculating $k(L)$ for any solvable Lie algebra with 1d extension and inequalities for any dimension, but higher dimension extensions remain unknown.

Following \cite{Yang2020}, we can use this invariant $k(L)$ to define a notion of spectral equivalence. 

<definition>

Two $n$-dimensional solvable Lie algebras $L_1$ and $L_2$ are **spectrally equivalent** if
$$Q_{L_2}(z) = Q_{L_1}(zB)$$
for some non-singular matrix $B$.

</definition>

If $L_1$ and $L_2$ are spectrally equivalent, we write $L_1 \stackrel{\text{SE}}{\cong} L_2$.

This is a weaker notion than isomorphism:

<theorem> 

If $L_1\cong L_2$ are isomorphic Lie algebras, then $L_1$ is spectrally equivalent to $L_2$.

</theorem>

The converse does not hold.

## Results 

<problem>

Do there exist values $e_3\neq e_3'$ such that 
$$\mathfrak{s}_{\dim \mathfrak{h}, \dim f}^{e_1, e_2, e_3} \not\cong \mathfrak{s}_{\dim \mathfrak{h}, \dim f}^{e_1, e_2, e_3'}$$
but
$$\mathfrak{s}_{\dim \mathfrak{h}, \dim f}^{e_1, e_2, e_3} \stackrel{\text{SE}}{\cong} \mathfrak{s}_{\dim \mathfrak{h}, \dim f}^{e_1, e_2, e_3'}. $$
That is, for two Lie algebras in the same family, do there exist parameters such that the two Lie algebras are spectrally equivalent but not isomorphic?

</problem>

The answer is yes.

<problem>

Does there exist a family of infinitely many $\mathfrak{s}$ such that every pair spectrally equivalent but not isomorphic?

</problem>

# Computations

## $(3,1)$ Model

There is only one family, $\mathfrak{s}_{3,1}^{1,1}$, defined by

$$
x_1 =
\begin{bmatrix}
0 & 1 & 0 \\
0 & 0 & 0 \\
0 & 0 & 0
\end{bmatrix}
\quad
x_2 =
\begin{bmatrix}
0 & 0 & 0 \\
0 & 0 & 1 \\
0 & 0 & 0
\end{bmatrix}
\quad
x_3 =
\begin{bmatrix}
0 & 0 & 1 \\
0 & 0 & 0 \\
0 & 0 & 0
\end{bmatrix}
\quad
x_4 =
\begin{bmatrix}
2 & 0 & 0 \\
0 & b+1 & 0 \\
0 & 0 & 1-b
\end{bmatrix}
$$
where $b \ge 0$.

<proposition>

$$
Q_{\mathfrak{s}_{3,1}^{1,1}}(z) = z_0(z_0 + 2bz_4)(z_0-(b+1)z_4)(z_0+(b+1)z_4). 
$$

</proposition>

<proof>

One can verify that 

$$
\text{ad}(x_1) =
\begin{bmatrix}
0 & 0 & 0 & b-1 \\
0 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 0 & 0
\end{bmatrix}, \qquad
\text{ad}(x_2) =
\begin{bmatrix}
0 & 0 & 0 & 0 \\
0 & 0 & 0 & -2b \\
-1 & 0 & 0 & 0 \\
0 & 0 & 0 & 0
\end{bmatrix}
$$

$$
\text{ad}(x_3) =
\begin{bmatrix}
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & -b-1 \\
0 & 0 & 0 & 0
\end{bmatrix}, \qquad
\text{ad}(x_4) =
\begin{bmatrix}
1-b & 0 & 0 & 0 \\
0 & 2b & 0 & 0 \\
0 & 0 & b+1 & 0 \\
0 & 0 & 0 & 0
\end{bmatrix}.
$$

Thus, 

$$
\begin{align*}
Q_{\mathfrak{s}_{3,1}^{1,1}}(z) &= \begin{bmatrix}
z_0 + z_4(1 - b) & 0 & 0 & z_1(b - 1) \\
0 & 2bz_4 + z_0 & 0 & -2bz_2 \\
-z_2 & z_1 & z_0 + z_4(b + 1) & z_3(-b - 1) \\
0 & 0 & 0 & z_0
\end{bmatrix} \\ 
&= z_0(z_0 + 2bz_4)(z_0 + (-b+1)z_4)(z_0 + (b+1) z_4).
\end{align*}
$$

</proof>

<corollary>

$$
k(\mathfrak{s}_{3,1}^{1,1,b}) = \begin{cases} 2& \text{if }b=0,1 \\ 
3 & \text{if } b=\frac{1}{3}\\ 
4& \text{otherwise}\end{cases}
$$

</corollary>

<proof>

If there are repeated roots, two or more of the elements in the set
$$
\{0, 2b, -b+1, b+1\}
$$ 
must be equal. Since $b\ge 0$, the only repeated roots occur when $b=0, \frac{1}{3}, 1$.

By direct computation, the three cases give us 

-  $b=0: z_0^2(z_0+z_4)^2$

- $b=\frac{1}{3}: z_0\left( z_0 + \frac{2}{3} z_4 \right)^2 \left(z_0+\frac{4}{3}z_4 \right)$

- $b=1: z_0^2(z_0+2z_4)^2$

which give us $k(\mathfrak{s}_{3,1}^{1,1})=2,3,2$, respectively.

</proof>

<proposition>

$\mathfrak{s}_{3,1}^{1,1,0} \stackrel{\text{SE}}{\equiv} \mathfrak{s}_{\dim \mathfrak{h}, \dim f}^{1,1,1}$ but $\mathfrak{s}_{3,1}^{1,1,0} \not\cong \mathfrak{s}_{\dim \mathfrak{h}, \dim f}^{1,1,1}$.

</proposition>

<proof>

Let $Q_{\mathfrak{s}_{3,1}^{1,1,0}}(z)=z_0^2(z_0+z_4)^2$ and $Q_{\mathfrak{s}_{3,1}^{1,1,1}}(z)=z_0^2(z_0+2z_4)^2$. It suffices to show the existence of a non-singular matrix $B$ such that 
$$
Q_{\mathfrak{s}_{3,1}^{1,1,0}}(z)=Q_{\mathfrak{s}_{3,1}^{1,1,1}}(zB).
$$
In particular, 
$$
B= \begin{bmatrix}
1 & 0 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 & 0 \\
0 & 0 & 0 & 1 & 0 \\
0 & 0 & 0 & 0 & \frac{1}{2}
\end{bmatrix}
$$
works, so the two Lie algebras are spectrally equivalent.

</proof>


## TWO PARAMETER (5,2): $\mathfrak{s}_{5,2}^{2,1}$

$\mathfrak{s}_{5,2}^{2,1}$ is defined by
$$
p_1 = \begin{bmatrix}
0 & 1 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0
\end{bmatrix}, \quad 
p_2 = \begin{bmatrix}
0 & 0 & 1 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0
\end{bmatrix}, \quad
q_1 = \begin{bmatrix}
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 1 \\
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0
\end{bmatrix}
$$
$$
q_2 = \begin{bmatrix}
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 1 \\
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0
\end{bmatrix}, \quad
h = \begin{bmatrix}
0 & 0 & 0 & 0 & 1 \\
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0
\end{bmatrix}
$$
$$
e_1 = \begin{bmatrix}
2 & 0 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 & 0 \\
0 & 0 & b+1 & 0 & 0 \\
0 & 0 & 0 & 1 & 0 \\
0 & 0 & 0 & 0 & 1-b
\end{bmatrix}, \quad
e_2 = \begin{bmatrix}
0 & 0 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 & 0 \\
0 & 0 & c & 0 & 0 \\
0 & 0 & 0 & -1 & 0 \\
0 & 0 & 0 & 0 & -c
\end{bmatrix}
$$
where $0\le \text{arg}(b)< \pi$, $|c|\le 1$.

<proposition>

$$
Q_{\mathfrak{s}_{5,2}^{2,1}}(z) = z_0^2 \left( (b+1)z_0 + z_6 - z_7 \right) \left( (2b+1)z_0 + 2b z_6 + 2c z_7 \right) \left( (b+1)z_0 - (b+1) z_6 - c z_7 + z_6 \right) \left( (b+1)z_0 + (b+1) z_6 + c z_7 \right) \left( (b+1)z_0 + (c+1) z_7 \right)  
$$

</proposition>

<proof>

This gives

$$
ad(p_1) = \begin{bmatrix}
0 & 0 & 0 & 0 & 0 & -1 & 1 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0
\end{bmatrix}, \quad
ad(p_2) = \begin{bmatrix}
0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & b-1 & c \\
0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 1 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0
\end{bmatrix}
$$

$$
ad(q_1) = \begin{bmatrix}
0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & -b & -c-1 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 \\
-1 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0
\end{bmatrix}, \quad
ad(q_2) = \begin{bmatrix}
0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & -2b & -2c \\
0 & -1 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0
\end{bmatrix}
$$

$$
ad(h) = \begin{bmatrix}
0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & -b-1 & -c \\
0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0
\end{bmatrix}, \quad
ad(e_1) = \begin{bmatrix}
1 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 1-b & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & b & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 2b & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & b+1 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0
\end{bmatrix}
$$

$$
ad(e_2) = \begin{bmatrix}
-1 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & -c & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & c+1 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 2c & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & c & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0
\end{bmatrix}
$$

which gives 

$$
\det \begin{bmatrix}
z_0 + z_6 - z_7 & 0 & 0 & 0 & 0 & -z_1 & z_1 \\
0 & -c z_7 + z_0 + z_6 (1 - b) & 0 & 0 & 0 & z_2 (b - 1) & c z_2 \\
0 & 0 & b z_6 + z_0 + z_7 (c + 1) & 0 & 0 & -b z_3 & z_3 (-c - 1) \\
0 & 0 & 0 & 2 b z_6 + 2 c z_7 + z_0 & 0 & -2 b z_4 & -2 c z_4 \\
-z_3 & -z_4 & z_1 & z_2 & c z_7 + z_0 + z_6 (b + 1) & z_5 (-b - 1) & -c z_5 \\
0 & 0 & 0 & 0 & 0 & z_0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & z_0
\end{bmatrix}
$$
$$
= z_0^2 (z_0 + z_6 - z_7) \left( 2b z_6 + 2c z_7 + z_0 \right) \left( -b z_6 - c z_7 + z_0 + z_6 \right) \left( b z_6 + c z_7 + z_0 + z_6 \right) \left( b z_6 + c z_7 + z_0 + z_7 \right).
$$

</proof>

<proposition>

We have

$$
k(\mathfrak{s}_{5,2}^{2,1}) = \begin{cases}
5 &\text{ if } (b, c) = (0, \pm 1), (1,0), \left( \pm \frac{1}{2}, \pm \frac{\sqrt{3}}{2} \right)\\ 
6 & \text{otherwise}
\end{cases}
$$

</proposition>


<proof>

- $(b, c) = (0, \pm 1)$:
$$
P(z_0) = z_0^2 (z_0 + z_6 - z_7) \left( \pm 2 z_7 + z_0 \right) \left( z_0 + z_6 \right)^2 \left( z_0 + z_7 \right).
$$

- $(b, c) = (1,0)$
$$
P(z_0) = z_0^3 (z_0 + z_6 - z_7) (z_0 + 2z_6) (z_0 + 2z_6) (z_0 + z_7).
$$

- $(b, c) = \left( \pm\frac{1}{2}, \frac{\sqrt{3}}{2} \right)$:
$$
P(z_0) = z_0^2 (z_0 + z_6 - z_7) \left(z_0 \pm z_6 + \sqrt{3}z_7\right)^2 \left(z_0 + z_6 \mp \frac{1}{2}z_6 - \frac{\sqrt{3}}{2}z_7\right) (z_0 + z_7).
$$

- $(b, c) = \left(\frac{1}{2}, \pm \frac{\sqrt{3}}{2}\right)$:
$$
P(z_0) = z_0^2 (z_0 + z_6 - z_7) (z_0 + z_6 \pm \sqrt{3}z_7)^2 \left(z_0 + z_6 - \frac{1}{2}z_6 \mp \frac{\sqrt{3}}{2}z_7\right) (z_0 + z_7).
$$

</proof>


