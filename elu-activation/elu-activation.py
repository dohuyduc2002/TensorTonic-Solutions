def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    # Write code here
    result = []
    for i in x:
        if i > 0:
            result.append(i)
        else:
            out = alpha * (math.exp(i) - 1)
            result.append(out)
    return result