import numpy as np

def dropout(x, p=0.5, rng=None):
    """
    Apply dropout to input x with probability p.
    Returns (output, dropout_pattern).
    """
    x = np.array(x)
    
    if p == 0:
        pattern = np.ones_like(x, dtype=float)
        return x, pattern

    if rng is not None:
        rand_vals = rng.random(x.shape)
    else:
        rand_vals = np.random.random(x.shape)

    mask = rand_vals < (1 - p)
    
    dropout_pattern = mask * 1 / (1 - p)
    output = x * dropout_pattern
    
    return output, dropout_pattern