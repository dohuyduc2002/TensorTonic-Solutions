def linear_layer_forward(X, W, b):
    """
    Compute the forward pass of a linear (fully connected) layer.
    """
    # Write code here
    # due to matrix have only 2 dim, we get row and col by idx 0,1
    
    rows_X = len(X) # m
    cols_X = len(X[0]) # n
    cols_W = len(W[0]) # n
    rows_W = len(W) # p
    
    Y = [[0 for _ in range(cols_W)] for _ in range(rows_X)]
    
    for i in range(rows_X):
        for j in range(cols_W):
            dot_sum = 0
            for k in range(cols_X): # shared dim
                dot_sum += X[i][k] * W[k][j]
            
            Y[i][j] = dot_sum + b[j]
            
    return Y


