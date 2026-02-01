import numpy as np
import math
from scipy.special import erf 
def gelu(x):
    """
    Compute the Gaussian Error Linear Unit (exact version using erf).
    x: scalar, list, or np.ndarray
    Return: np.ndarray of same shape (dtype=float)
    """
    # Write code here
    x = np.array(x)
    v_erf = np.vectorize(math.erf)
    var = x / np.sqrt(2)
    erf_val = v_erf(var)
    return x / 2 * (1 + erf_val)