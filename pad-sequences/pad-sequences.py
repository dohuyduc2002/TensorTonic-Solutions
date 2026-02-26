import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    if not max_len:
        max_len = max([len(x) for x in seqs])

    out = []
    for x in seqs:
        clipped = x[:max_len]
        padded = np.pad(
            clipped, 
            (0, max_len - len(clipped)), 
            constant_values=pad_value
        )
        out.append(padded)
    
    return np.array(out)
    