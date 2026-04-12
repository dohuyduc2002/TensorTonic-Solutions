import numpy as np

def clip_gradients(g, max_norm):
    """
    Clip gradients using global norm clipping.
    """
    g = np.asarray(g, dtype=np.float64)
    if max_norm <= 0:
        return g
        
    g_grad = np.linalg.norm(g)
    
    if g_grad > max_norm:
        return g * (max_norm / g_grad)
    
    return g