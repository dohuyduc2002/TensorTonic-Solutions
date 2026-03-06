def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    matched = []
    relevent = set(relevant) # use set for O(1) search

    matched = [item for item in recommended[:k] if item in relevent] # O(k)

    precision = len(matched) / k
    recall = len(matched) / len(relevant)

    return [precision, recall]