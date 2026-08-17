def target_encoding(categories, targets):
    """
    Replace each category with the mean target value for that category.
    """
    stats = {}

    # 1 pass to calculate both sum and count with nested dict
    for cat, target in zip(categories, targets):
        if cat in stats:
            stats[cat][0] += target # sum
            stats[cat][1] += 1 # count
        else:
            stats[cat] = [target, 1]
            
    return [stats[cat][0] / stats[cat][1] for cat in categories]
    