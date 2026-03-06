def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    matched = []
    relevent = set(relevant) # use set for O(1) 

    for i in range(k):
        if recommended[i] in relevant:
            matched.append(recommended[i])

    precision = len(matched) / k
    recall = len(matched) / len(relevant)

    return [precision, recall]