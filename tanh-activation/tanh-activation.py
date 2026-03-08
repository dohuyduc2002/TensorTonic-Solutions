import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    x = np.array(x)
    # Write code here
    nominator = np.exp(x) - np.exp(-x)
    denominator = np.exp(x) + np.exp(-x)

    return nominator / denominator