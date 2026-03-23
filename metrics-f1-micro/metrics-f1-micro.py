def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    # Write code here
    tp = 0
    fp = 0
    fn = 0
    for label, pred in zip(y_true, y_pred):
        if label == pred:
            tp += 1
        else:
            fn += 1
            fp += 1
    nominator = 2 * tp
    denominator = (2 * tp) + fp + fn
    return nominator / denominator