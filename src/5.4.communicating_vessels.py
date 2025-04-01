def generator_interleave(*iter):
    """"""
    if len(iter) <= 0:
        return

    max_len = max(map(len, iter))
    for i in range(max_len):
        for j in iter:
            if i < len(j):
                yield j[i]


def interleave(*iter):
    """"""
    return list(generator_interleave(*iter))
