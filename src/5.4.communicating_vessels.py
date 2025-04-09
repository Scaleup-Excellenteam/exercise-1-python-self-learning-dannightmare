"""Solution 5.4"""


def generator_interleave(*iters):
    """internal module function"""
    if len(iters) <= 0:
        return

    max_len = max(map(len, iters))
    for i in range(max_len):
        for j in iters:
            if i < len(j):
                yield j[i]


def interleave(*iters):
    """Interleave"""
    return list(generator_interleave(*iters))
