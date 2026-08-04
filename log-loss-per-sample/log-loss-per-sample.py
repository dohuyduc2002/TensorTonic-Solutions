import math

def log_loss(y_true, y_pred, eps=1e-15):
    """
    Compute per-sample log loss.
    """
    # Write code here
    out = []
    for i in range(len(y_pred)):
        prob = min(max(y_pred[i], eps), 1 - eps)
        log_l = -1 * (y_true[i] * math.log(prob) + ((1-y_true[i]) * math.log(1-prob)))
        out.append(log_l)
    return out