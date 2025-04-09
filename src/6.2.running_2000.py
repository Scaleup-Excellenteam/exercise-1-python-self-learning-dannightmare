"""Solution 6.2"""


def running_2000(func, *args, **kwargs):
    """running 2000"""
    import time
    curtime = time.time()
    func(*args, **kwargs)
    return time.time() - curtime
