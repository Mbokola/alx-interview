#!/usr/bin/python3
""" 0-validate_utf8 """


def validUTF8(data):
    """ Checks if encoding is utf8 """
    for encoding in data:
        if encoding < 128:
            continue
        binary = format(encoding, '08b')
        if binary.startswith("10"):
            return False
    return True
