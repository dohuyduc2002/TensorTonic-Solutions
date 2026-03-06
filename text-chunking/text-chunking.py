def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    # Write code here
    step = chunk_size - overlap
    out = []
    if chunk_size > len(tokens) and len(tokens) != 0:
        return [tokens]
    # if len(tokens) == 0:
    #     return tokens
    for i in range(0, len(tokens), step):
        if i + chunk_size > len(tokens):
            break
        chunk = tokens[i : i + chunk_size]
        out.append(chunk)
    return out