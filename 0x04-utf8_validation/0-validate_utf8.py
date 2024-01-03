#!/usr/bin/python3
""" 0-validate_utf8 """


def validUTF8(data):
    """ Checks if encoding is utf8 """
    for encoding in data:
        if encoding < 128:
            continue
        return False
    return True
