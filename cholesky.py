import numpy as np
from math import sqrt


def cholesky_decomposition(M):
    """
    Compute the cholesky decomposition of a SPD matrix M.

    :param M: (N, N) real valued matrix.
    :return: R: (N, N) upper triangular matrix with positive diagonal entries if M is SPD.
    """

    A = np.copy(M)
    n = A.shape[0]
    R = np.zeros_like(A)

    for k in range(n):
        R[k, k] = sqrt(A[k, k])
        R[k, k + 1:] = A[k, k + 1:] / R[k, k]
        for j in range(k + 1, n):
            A[j, j:] = A[j, j:] - R[k, j] * R[k, j:]

    return R

