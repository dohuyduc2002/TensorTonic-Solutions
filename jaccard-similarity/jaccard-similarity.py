def jaccard_similarity(set_a, set_b):
    """
    Compute the Jaccard similarity between two item sets.
    """
    # Write code here
    if len(set_a) == 0 and len(set_b) == 0:
        return float('nan')
    nominator = set(set_a) & set(set_b)
    denominator = set(set_a + set_b)

    return len(nominator) / len(denominator)
    