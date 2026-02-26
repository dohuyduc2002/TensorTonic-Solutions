import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    """
    Return PE of shape (seq_len, d_model) using sin/cos formulation.
    Odd d_model -> last column is sin.
    """
    # Write code here
    pos = np.arange(0, seq_len).reshape(seq_len, 1)
    denominator = np.exp(np.arange(0, d_model, 2) * -(np.log(base) / d_model))

    pe = np.zeros((seq_len, d_model))

    pe[:, 0::2] = np.sin(pos * denominator)
    pe[:, 1::2] = np.cos(pos * denominator[:d_model // 2])

    return pe