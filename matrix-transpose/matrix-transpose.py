import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    arr = np.array(A)
    rows, cols = arr.shape
    transposed = np.zeros((cols,rows))
    for x in range(rows):
        for y in range(cols):
            transposed[y, x]= arr[x,y]
    return transposed
