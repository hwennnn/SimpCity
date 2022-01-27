"""
This module deals with all utility related functions.
"""
__docformat__ = "google"

import time


def current_ms():
    """
    Returns:
        int: The current time in milliseconds

    The method will return the current time in milliseconds.

    """

    return round(time.time() * 1000)
