"""Solution 5.1"""
from os import listdir


def thats_the_way(path):
    """That's the way

    :param str path
    :return list(str): starting with 'deep'
    """
    return [f for f in listdir(path) if f.startswith("deep")]
