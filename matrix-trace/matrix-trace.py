import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here
    A = np.array(A)
    rows = A.shape[0]
    trace = 0
    for i in range(rows):
        trace += A[i,i]

    return trace