"""Solution 6.5"""


def group_by(func, array):
    """group by"""
    ans = {}
    for item in array:
        val = func(item)
        if val not in ans:
            ans[val] = [item]
        else:
            ans[val].append(item)
    return ans
