
<link href="../whirlwind.css" rel="stylesheet">

<whirlheader>
<p>name</p>
<p>Calculations</p>
<p>date</p>
</whirlheader>

# Theorem

<proposition>

Consider a solvable Lie algebra $\mathfrak{s}_{\dim \mathfrak{h}, \dim f}^{1, n}$ and parameters $b,b'$ such that $k(\mathfrak{s}_{\dim \mathfrak{h}, \dim f}^{1, n, b}) = k(\mathfrak{s}_{\dim \mathfrak{h}, \dim f}^{1, n, b'})$. Suppose the characterstic polynomial is 
$$
Q_{\mathfrak{s}_{\dim \mathfrak{h}, \dim f}^{1, k, b}}(z) = \prod_{i=1}^{k(\mathfrak{s}_{\dim \mathfrak{h}, \dim f}^{1, k, b})} \left(\sum_{j=0}^n f_{i,j}z_j \right)
$$
If $f_{i,j}(b)=a_{i,j}b+c_{i,j}$ for some $a_{i,j},c_{i,j}\neq 0$, then 
$$\mathfrak{s}_{\dim \mathfrak{h}, \dim f}^{1, n, b}\stackrel{\text{SE}}{\not\cong} \mathfrak{s}_{\dim \mathfrak{h}, \dim f}^{1, n, b'} \Longleftrightarrow b=b'$$

</proposition>

## Proof

$$
\begin{align*}
& Q_{\mathfrak{s}_{\dim \mathfrak{h}, \dim f}^{1, n, b'}}(z) = Q_{\mathfrak{s}_{\dim \mathfrak{h}, \dim f}^{1, n, b}}(zB) \\
\implies & \prod_{i=1}^{k(\mathfrak{s}_{\dim \mathfrak{h}, \dim f}^{1, k, b'})} \left(\sum_{j=0}^n f'_{i,j}(b') z_j \right) = \prod_{i=1}^{k(\mathfrak{s}_{\dim \mathfrak{h}, \dim f}^{1, k, b})} \left(\sum_{j=0}^n f_{i,j}(b) (zB)_j \right) \\
\implies & \prod_{i=1}^{k(\mathfrak{s}_{\dim \mathfrak{h}, \dim f}^{1, k, b'})} \left(\sum_{j=0}^n f'_{i,j}(b') z_j \right) = \prod_{i=1}^{k(\mathfrak{s}_{\dim \mathfrak{h}, \dim f}^{1, k, b})} \left(\sum_{j=0}^n f_{i,j}(b) \sum_{\ell=0}^{n} z_\ell B_{\ell j} \right) \\
\implies & \prod_{i=1}^{k(\mathfrak{s}_{\dim \mathfrak{h}, \dim f}^{1, k, b'})} \left(\sum_{j=0}^n f'_{i,j}(b') z_j \right) = \prod_{i=1}^{k(\mathfrak{s}_{\dim \mathfrak{h}, \dim f}^{1, k, b})} \left(\sum_{\ell=0}^{n} z_\ell \sum_{j=0}^n f_{i,j}(b) B_{\ell j} \right) \\
\implies & \sum_{\ell=0}^{n} z_\ell \sum_{j=0}^n f_{i,j}(b) B_{\ell j} = \sum_{j=0}^n f'_{i,j}(b') z_j \\
\implies & \sum_{\ell=0}^{n} \sum_{j=0}^n f_{i,j}(b) B_{\ell j} z_\ell = \sum_{j=0}^n f'_{i,j}(b') z_j \\
\implies & f'_{i,j}(b') = \sum_{\ell=0}^{n} f_{i,\ell}(b) B_{\ell j} \\
\implies & f'_{i,j}(b') = \sum_{\ell=0}^{n} (a_{i,\ell} b + c_{i,\ell}) B_{\ell j} \\
\implies & f'_{i,j}(b') = \sum_{\ell=0}^{n} a_{i,\ell} b B_{\ell j} + \sum_{\ell=0}^{n} c_{i,\ell} B_{\ell j} \\
\implies & f'_{i,j}(b') = \sum_{\ell=0}^{n} a_{i,\ell} b B_{\ell j} + \sum_{\ell=0}^{n} c_{i,\ell} B_{\ell j} \\
\implies & f'_{i,j}(b') = a_{i,j} b \sum_{\ell=0}^{n} B_{\ell j} + c_{i,j} \sum_{\ell=0}^{n} B_{\ell j} \\
\implies & f'_{i,j}(b') = a_{i,j} b \sum_{\ell=0}^{n} B_{\ell j} + c_{i,j} \sum_{\ell=0}^{n} B_{\ell j} \\
\implies & \sum_{\ell=0}^{n} \left(a_{i,\ell} b + c_{i,\ell}\right) B_{\ell j} = a_{i,j} b \sum_{\ell=0}^{n} B_{\ell j} + c_{i,j} \sum_{\ell=0}^{n} B_{\ell j} \\
\implies & \sum_{\ell=0}^{n} (a_{i,\ell} b + c_{i,\ell}) B_{\ell j} = a_{i,j} b \sum_{\ell=0}^{n} B_{\ell j} + c_{i,j} \sum_{\ell=0}^{n} B_{\ell j} \\
\implies & b' - b \sum_{\ell=0}^{n} B_{\ell j} = \frac{c_{i,j}}{a_{i,j}} \left( \sum_{\ell=0}^{n} B_{\ell j} - 1 \right) \\
\end{align*}
$$
We normalize $B$ such that $\sum_{\ell=0}^{n} B_{\ell j} = 1$ for all $j$. Then:
$$
\begin{align*}
& b' - b \sum_{\ell=0}^{n} B_{\ell j} = \frac{c_{i,j}}{a_{i,j}} \left( \sum_{\ell=0}^{n} B_{\ell j} - 1 \right) \\
\implies & b' - b \sum_{\ell=0}^{n} B_{\ell j} = \frac{c_{i,j}}{a_{i,j}} (1 - 1) \\
\implies & b' - b \sum_{\ell=0}^{n} B_{\ell j} = 0 \\
\implies & b' = b \sum_{\ell=0}^{n} B_{\ell j}
\end{align*}
$$
Since we've normalized $B$ such that $\sum_{\ell=0}^{n} B_{\ell j} = 1$, we have:
$$
b' = b,
$$
completing the proof.
