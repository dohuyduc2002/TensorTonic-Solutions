import numpy as np

def roc_curve(y_true, y_score):
    """
    Compute ROC curve from binary labels and scores.
    """
    # Write code here
    y_true = np.array(y_true)
    y_score = np.array(y_score)

    # sort the idx of label corespond to score
    # make score negative cuz we need to sort in desc order
    indices = np.lexsort((y_true, -y_score))
    y_score_sorted = y_score[indices]
    y_true_sorted = y_true[indices]
    
    tps = np.cumsum(y_true_sorted)
    fps = np.cumsum(1 - y_true_sorted)
    
    # calculate denominator of tpr and fpr
    num_pos = np.sum(y_true)
    num_neg = len(y_true) - num_pos
    
    tpr = tps / num_pos
    fpr = fps / num_neg
    
    # handle ties in ROC curve
    distinct_indices = np.where(np.diff(y_score_sorted) != 0)[0]
    indicies = np.append(distinct_indices, len(y_score_sorted) - 1) # get the last idx in the list due to limitation of discrete difference
    
    tpr_filtered = tpr[indicies]
    fpr_filtered = fpr[indicies]
    thresholds_filtered = y_score_sorted[indicies]
    
    final_tpr = np.concatenate(([0], tpr_filtered))
    final_fpr = np.concatenate(([0], fpr_filtered))
    final_thresholds = np.concatenate(([np.inf], thresholds_filtered))
    
    return final_fpr, final_tpr, final_thresholds