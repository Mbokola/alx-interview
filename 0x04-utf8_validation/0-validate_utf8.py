#!/usr/bin/python3
""" 0-validate_utf8 """


def validUTF8(data):
    """ Checks if encoding is utf8 """
    count = 0
    for encoding in data:
        binary = format(encoding, '08b')
        if count == 0:
            if binary.startswith('0'):
                continue
            elif binary.startswith('110'):
                count = 1
            elif binary.startswith('1110'):
                count = 2
            elif binary.startswith('11110'):
                count = 3
            else:
                return False
        else:
            if not binary.startswith('10'):
                return False
            count -= 1
    return count == 0
