"""Solution 5.4"""


def generator_interleave(*iter):
    """internal module function"""
    if len(iter) <= 0:
        return

    max_len = max(map(len, iter))
    for i in range(max_len):
        for j in iter:
            if i < len(j):
                yield j[i]


def interleave(*iter):
    """Interleave"""
    return list(generator_interleave(*iter))
