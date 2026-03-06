def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    matched = []
    for i in range(k):
        for j in range(len(relevant)):
            if recommended[i] == relevant[j]:
                matched.append(relevant[j])

    precision = len(matched) / k
    recall = len(matched) / len(relevant)

    return [precision, recall]