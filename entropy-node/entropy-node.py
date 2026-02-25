import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    _, counts = np.unique(y, return_counts=True)
    p = counts / len(y)
    log_p = np.where(p > 0, np.log2(p), 0)
    
    h = -np.sum(p * log_p)

    return h