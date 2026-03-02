import numpy as np

def matrix_inverse(A):
    """
    Returns: A_inv of shape (n, n) such that A @ A_inv ≈ I
    """
    # Write code here
    A = np.array(A)
    shape = A.shape
    det = np.linalg.det(A)
    
    if shape[0] != shape[1]:
        return None
    elif abs(det) < 1e-10:
        return None
    elif A.ndim != 2:
        return None
    else:
        return np.linalg.inv(A)
