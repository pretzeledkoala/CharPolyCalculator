
<link href="../whirlwind.css" rel="stylesheet">

<whirlheader>
<p>name</p>
<p>Calculations</p>
<p>date</p>
</whirlheader>

# First Version

<proposition>

Consider a solvable Lie algebra $\mathfrak{s}_{\dim \mathfrak{h}, \dim f}^{1, n}$ and parameters $b,b'$ such that $k(\mathfrak{s}_{\dim \mathfrak{h}, \dim f}^{1, n, b}) = k(\mathfrak{s}_{\dim \mathfrak{h}, \dim f}^{1, n, b'})$. Suppose the characterstic polynomial is 
$$
Q_{\mathfrak{s}_{\dim \mathfrak{h}, \dim f}^{1, k, b}}(z) = \prod_{i=1}^{k(\mathfrak{s}_{\dim \mathfrak{h}, \dim f}^{1, k, b})} \left(\sum_{j=0}^n f_{i,j}z_j \right)
$$
If 
- $\exists i,j$ such that $f_{i,j}(b)=a_{i,j}b+c_{i,j}$ for some $a_{i,j},c_{i,j}\neq 0$
- $\exists i' \neq i$ such that $f_{i',j}(b)=a_{i',j}b+c_{i',j}$ for some $a_{i',j},c_{i',j}\neq 0$
- $\exists i'' \neq i, i''$ such that $f_{i'',j}(b)=a_{i'',j}b+c_{i'',j}$ for some $f_{i'',j}(b)\neq 0$

such that $f_{i,j}\neq f_{i',j} \neq f_{i'',j}$, then 
$$\mathfrak{s}_{\dim \mathfrak{h}, \dim f}^{1, n, b}\stackrel{\text{SE}}{\not\cong} \mathfrak{s}_{\dim \mathfrak{h}, \dim f}^{1, n, b'} \Longleftrightarrow b=b'$$

There exists a column $j$ such that in this column, at least 3 entries are equal to the corresponding entries in $Ab+C$.

$$
f_{i,j}(b) = A_{ij}b+C_{i,j}
$$
has at least 3 distinct solutions.

</proposition>

# Second Version

<proposition>

Let $L$ be a solvable Lie algebra with parameters, evaluated at points $b$ and $b'$ such that $k(\mathfrak{s}(b)) = k(\mathfrak{s}(b'))$. In the expansion of the characteristic polynomial, if for some index $i$, the value $z_i$ appears in at least three distinct linear factors, each with distinct coefficients that are linear in $b$, then 
$$\mathfrak{s}(b) \stackrel{SE}{\cong} \mathfrak{s}(b') \Longleftrightarrow b = b'.$$

</proposition>

# Third Version

<definition>

A solvable Lie algebra with parameter is called **triple-occuring** if in the expansion of the characteristic polynomial, for some index $i$, the value $z_i$ appears in at least three distinct linear factors, each with distinct coefficients that are linear in $b$.

</definition>

<proposition>

Let $L$ be a triple-occuring solvable Lie algebra with parameter, evaluated at points $b$ and $b'$. If $k(\mathfrak{s}(b)) = k(\mathfrak{s}(b'))$, then
$$\mathfrak{s}(b) \stackrel{SE}{\cong} \mathfrak{s}(b') \Longleftrightarrow b = b'.$$

</proposition>

## Proof

We begin with the spectral equivalence assumption that $Q_{\mathfrak{s}_{\dim \mathfrak{h}, \dim f}^{1, n, b'}}(z) = Q_{\mathfrak{s}_{\dim \mathfrak{h}, \dim f}^{1, n, b}}(z B)$, where $B$ is a non-singular matrix. This assumption implies the following equality for the characteristic polynomials:
$$
\prod_{i=1}^{k(\mathfrak{s}_{\dim \mathfrak{h}, \dim f}^{1, n, b'})} \left( \sum_{j=0}^n f'_{i,j}(b') z_j \right) = \prod_{i=1}^{k(\mathfrak{s}_{\dim \mathfrak{h}, \dim f}^{1, n, b})} \left( \sum_{j=0}^n f_{i,j}(b) (z B)_j \right)
$$
This can be expanded as:
$$
\prod_{i=1}^{k(\mathfrak{s}_{\dim \mathfrak{h}, \dim f}^{1, n, b'})} \left( \sum_{j=0}^n f'_{i,j}(b') z_j \right) = \prod_{i=1}^{k(\mathfrak{s}_{\dim \mathfrak{h}, \dim f}^{1, n, b})} \left( \sum_{j=0}^n f_{i,j}(b) \sum_{\ell=0}^{n} B_{\ell j} z_\ell \right)
$$
Simplifying this expression further:
$$
\prod_{i=1}^{k(\mathfrak{s}_{\dim \mathfrak{h}, \dim f}^{1, n, b'})} \left( \sum_{j=0}^n f'_{i,j}(b') z_j \right) = \prod_{i=1}^{k(\mathfrak{s}_{\dim \mathfrak{h}, \dim f}^{1, n, b})} \left( \sum_{\ell=0}^{n} z_\ell \sum_{j=0}^{n} f_{i,j}(b) B_{\ell j} \right)
$$
Thus, for each $i$, we have the equality:
$$
\sum_{\ell=0}^{n} z_\ell \sum_{j=0}^{n} f_{i,j}(b) B_{\ell j} = \sum_{j=0}^{n} f'_{i,j}(b') z_j
$$
This leads to:
$$
f'_{i,j}(b') = \sum_{\ell=0}^{n} f_{i,\ell}(b) B_{\ell j}
$$

Now, using the fact that $f_{i,j}(b)$ is linear in $b$, we substitute the expressions for $f_{i,j}(b)$, $f_{i',j}(b)$, and $f_{i'',j}(b)$:
$$
f_{i,j}(b) = a_{i,j} b + c_{i,j}, \quad f_{i',j}(b) = a_{i',j} b + c_{i',j}, \quad f_{i'',j}(b) = a_{i'',j} b + c_{i'',j}
$$
Substituting into the equation for $f'_{i,j}(b')$, we get:
$$
f'_{i,j}(b') = \sum_{\ell=0}^{n} \left( a_{i,\ell} b + c_{i,\ell} \right) B_{\ell j}
$$
Expanding this gives:
$$
f'_{i,j}(b') = \sum_{\ell=0}^{n} a_{i,\ell} b B_{\ell j} + \sum_{\ell=0}^{n} c_{i,\ell} B_{\ell j}
$$
This shows that $f'_{i,j}(b')$ is a linear function of $b$. 

Next, we analyze the linear system that arises from the conditions $f_{i,j} \neq f_{i',j} \neq f_{i'',j}$. Since the functions are distinct, we have a system of three linear equations (one for each $f_{i,j}(b)$, $f_{i',j}(b)$, and $f_{i'',j}(b)$) in the variables $b$. These equations must hold for all values of $z_j$, and they represent a system of linear equations in $b$.

The crucial observation here is that the system of equations has no solutions since we have three distinct functions $f_{i,j}$, $f_{i',j}$, and $f_{i'',j}$. As such, there is no solution for $b \neq b'$, because the system of linear equations cannot simultaneously satisfy all three distinctness conditions unless $b = b'$.

Therefore, we conclude that:
$$
\mathfrak{s}_{\dim \mathfrak{h}, \dim f}^{1, n, b} \stackrel{\text{SE}}{\not\cong} \mathfrak{s}_{\dim \mathfrak{h}, \dim f}^{1, n, b'} \Longleftrightarrow b = b'
$$
This completes the proof.