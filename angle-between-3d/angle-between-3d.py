import numpy as np

def angle_between_3d(v, w):
    """
    Compute the angle (in radians) between two 3D vectors.
    """
    # Your code here
    v = np.asarray(v)
    w = np.asarray(w)

    norm_v = np.linalg.norm(v)
    norm_w = np.linalg.norm(w)

    if norm_v < 1e-8 or norm_w < 1e-8:
        return np.nan
    cos_theta = np.dot(v, w) / (norm_v * norm_w)
    cos_theta = np.clip(cos_theta, -1.0, 1.0)

    return np.arccos(cos_theta)