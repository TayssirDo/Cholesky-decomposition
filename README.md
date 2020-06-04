<script type="text/javascript" async
src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.2/MathJax.js? 
config=TeX-MML-AM_CHTML"
</script>

# Cholesky-decomposition
The Cholesky decomposition is an efficient and reliable way to check if a symmetric matrix is positive definite. If a symmetric matrix is not positive definite, the Cholesky decomposition will fail.

**Theorem:**
If <img src="https://render.githubusercontent.com/render/math?math=A \in \mathbb{R}^{n \times n}"> is symmetric positive definite (SPD), then <img src="https://render.githubusercontent.com/render/math?math=A"> has a unique Cholesky decomposition:
<img src="https://render.githubusercontent.com/render/math?math=A = R^{\text{T}} R">
where <img src="https://render.githubusercontent.com/render/math?math=R \in \mathbb{R}^{n \times n}"> is upper triangular with positive diagonal entries.



