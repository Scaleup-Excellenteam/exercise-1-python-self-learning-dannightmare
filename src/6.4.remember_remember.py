"""Solution 6.4"""
from PIL import Image


def _remember_remember(img_path):
    """Internal module function"""

    img = Image.open(img_path)
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            pixel = img.getdata()[j * img.size[0] + i]
            if pixel != 255:
                yield chr(j)


def remember_remember(img_path):
    """Remember Remember"""
    return ''.join(list(_remember_remember(img_path)))
