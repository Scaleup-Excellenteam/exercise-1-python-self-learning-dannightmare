"""Solution 5.3"""
import re


def _parsle_tongue():
    """private module function"""
    pattern = re.compile(b'([a-z]{5,})!')
    try:
        with open("./resources/logo.jpg", 'rb') as imgfile:
            buffer = imgfile.read(2048)
            while buffer:
                for match in re.finditer(pattern, buffer):
                    yield match.group(1).decode('ascii')

                tail = buffer[-1024:]
                new_data = imgfile.read(1024)
                if not new_data:
                    break
                buffer = tail + new_data

    except OSError as e:
        print(e)


def parsle_tongue():
    """Parsle tongue"""
    return list(_parsle_tongue())
