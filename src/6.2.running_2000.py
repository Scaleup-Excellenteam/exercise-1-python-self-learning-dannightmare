"""Solution 6.2"""
import time


def running_2000(func, *args, **kwargs):
    """running 2000"""
    curtime = time.time()
    func(*args, **kwargs)
    return time.time() - curtime
