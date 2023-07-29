#!/usr/bin/python3

"""This module contains code for the
utf8 validate interview task
"""


def validUTF8(data):
    """Validates a stream utf8 bytes"""

    if len(data) == 0 or data is None:
        return False

    if max(data) > 255:
        return False

    if min(data) < 0:
        return False

    return True
