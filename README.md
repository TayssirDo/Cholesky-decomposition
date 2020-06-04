# Cholesky decomposition
The Cholesky decomposition is an efficient and reliable way to check if a symmetric matrix is positive definite. If a symmetric matrix is not positive definite, the Cholesky decomposition will fail.

**Theorem:**
If <img src="https://render.githubusercontent.com/render/math?math=A \in \mathbb{R}^{n \times n}"> is symmetric positive definite (SPD), then <img src="https://render.githubusercontent.com/render/math?math=A"> has a unique Cholesky decomposition:
<img src="https://render.githubusercontent.com/render/math?math=A = R^{\text{T}} R">
where <img src="https://render.githubusercontent.com/render/math?math=R \in \mathbb{R}^{n \times n}"> is upper triangular with positive diagonal entries.


## Example
```python
A = np.array([[7.3, 1, 0], [1, 20, 3.5], [0, 3.5, 2]])
print('----- Matrix A: -----\n' + str(A) + '\n')

# compute cholesky decomposition
R = cholesky_decomposition(A)

print('----- Matrix R: -----\n' + str(R) + '\n')
print('--> Verification: \n' + str(R.transpose() @ R))
```

## Notes
1. G.H. Golub and C.F. Van Loan. Matrix Computations. The Johns Hopkins University Press, Baltimore, Maryland, 4th edition, 2013.

2. Å. Björck. Numerical Methods in Matrix Computations. Springer,2015.
