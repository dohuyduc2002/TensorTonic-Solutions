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

    shape = (len(seqs), max_len)
    out = np.full(shape, pad_value)

    for i, seq in enumerate(seqs):
        truncate_seq = seq[:max_len]
        out[i, :len(truncate_seq)] = truncate_seq
    return out
    