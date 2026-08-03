def perplexity(prob_distributions, actual_tokens):
    """
    Compute the perplexity of a token sequence given predicted distributions.
    """
    import math
    # Write code here
    n = len(actual_tokens)
    log_sum = 0
    for i in range(n):
        prob = prob_distributions[i][actual_tokens[i]] # get prob at each label 
        log_sum += math.log(prob)

    H = -log_sum / n
    perplex = round(math.exp(H),4)
    return perplex