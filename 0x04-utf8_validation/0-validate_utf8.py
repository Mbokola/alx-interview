#!/usr/bin/python3
""" 0-validate_utf8 """


def validUTF8(data):
    """ Checks if encoding is utf8 """
    count = 0
    for encoding in data:
        if encoding < 128:
            continue
        binary = format(encoding, '08b')
        if count == 0:
            if binary.startswith("110") and len(data) == 2:
                count = 1
            elif binary.startswith("1110") and len(data) == 3:
                count = 2
            elif binary.startswith("11110") and len(data) == 4:
                count = 3
            else:
                return False
        else:
            if not binary.startswith("10"):
                return False
            count -= 1
    return True
