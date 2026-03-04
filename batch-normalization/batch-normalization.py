import numpy as np

def batch_norm_forward(x, gamma, beta, eps=1e-5):
    """
    Forward-only BatchNorm for (N,D) or (N,C,H,W).
    """
    # Write code here
    """
    internal covariate shift need due to 
    - layer cannot assume stable input statistics: becuz the params get update after a fwd pass, the param distribution changes
    - gradients vanish or explode either make training params ineffective 
    - normalize for lower lr -> stablize the param distribution 
    """
    x = np.array(x)
    gamma = np.array(gamma)
    beta = np.array(beta)
    if len(x.shape) == 2: 
        axis = 0
    elif len(x.shape) == 4:
        axis = (0, 2, 3)
        gamma = gamma.reshape(1, -1, 1, 1) # reshape to calculate normalize y in each feature
        beta = beta.reshape(1, -1, 1, 1)
    
    mean = np.mean(x, axis=axis, keepdims=True)
    sigma = np.var(x, axis=axis, keepdims=True)
    x_hat = (x - mean) / np.sqrt(sigma + eps)
    y = gamma * x_hat + beta

    return y
