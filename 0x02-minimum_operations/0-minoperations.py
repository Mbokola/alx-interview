#!/usr/bin/python3
""" 0-minoperations """


def minOperations(n):
    """
    Calculates minimum operations required to copy text from
    textfile n times
    """
    if n <= 0:
        return 0

    copy_and_paste = 2
    paste = 1
    clipboard = 1
    text_count = 1
    operations = 0

    while n > text_count:
        if text_count + text_count <= n and text_count != copy_and_paste:
            operations += copy_and_paste
            clipboard = text_count
            text_count += text_count
        else:
            operations += paste
            text_count += clipboard
    return operations
