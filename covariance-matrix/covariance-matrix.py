import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    # Write code here
    x = np.asarray(X)
    if x.ndim == 1 or x.shape[0] == 1:
        return None
    mu = np.mean(x, axis=0)
    x_centered = x - mu

    cov = 1 / (x.shape[0] - 1) * x_centered.T @ x_centered

    return cov