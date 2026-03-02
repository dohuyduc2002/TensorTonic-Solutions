def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    """
    # Write code here

    """
    img dim size = 3
    dim[x]:  H
    dim[x][y] :  W
    dim[x][y][z]:  C
    """
    img_len_C = len(image[0][0])
    img_len_W = len(image[0])
    img_len_H = len(image)
    
    gray_scale = [[0 for w in range(img_len_W)] for h in range(img_len_H)]
                                        
    for h in range(img_len_H):
        for w in range(img_len_W):
            gray_scale[h][w] = image[h][w][0] * 0.299 + image[h][w][1] * 0.587 + image[h][w][2] * 0.114

    return gray_scale