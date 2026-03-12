def k_means_centroid_update(points, assignments, k):
    """
    Compute new centroids as the mean of assigned points.
    """
    # Write code here
    dim = len(points[0])
    sums = [[0.0 for _ in range(dim)] for _ in range(k)]
    counts = [0 for _ in range(k)]
    
    for i in range(len(points)):
        cluster_idx = assignments[i]
        counts[cluster_idx] += 1
        for d in range(dim):
            sums[cluster_idx][d] += points[i][d]
            
    new_centroids = []
    for j in range(k):
        if counts[j] > 0:
            centroid = [sums[j][d] / counts[j] for d in range(dim)]
            new_centroids.append(centroid)
        else:
            new_centroids.append([0.0 for _ in range(dim)])
            
    return new_centroids