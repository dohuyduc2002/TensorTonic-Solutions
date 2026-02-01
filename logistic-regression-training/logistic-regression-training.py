import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    # Write code here
    w = np.zeros(X.shape[1])
    b = 0
    for i in range(steps):
        z = np.dot(X, w) + b
        yhat = _sigmoid(z)

        grad_w = np.dot(X.transpose(), yhat-y) / X.shape[0]
        grad_b = np.mean(yhat - y)

        w = w - lr * grad_w
        b = b - lr * grad_b
    return (w,b)