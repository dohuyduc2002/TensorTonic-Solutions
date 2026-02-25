import numpy as np

def rmsprop_step(w, g, s, lr=0.001, beta=0.9, eps=1e-8):
    """
    Perform one RMSProp update step.
    """
    # Write code here
    s = np.array(s)
    w = np.array(w)
    g = np.array(g)
    
    s = beta * s + np.dot((1-beta), np.power(g,2))
    delta_w = lr / np.sqrt(s + eps) * g
    
    w = w - delta_w
    return (w,s)