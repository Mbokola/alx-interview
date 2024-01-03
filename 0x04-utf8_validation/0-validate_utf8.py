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
                continue
            elif binary.startswith('1110'):
                continue
            elif binary.startswith('11110'):
                continue
            else:
                return False

    return True
