"""
This module deals with the building enumeration object.
"""
__docformat__ = "google"

from enum import Enum


class Buildings(Enum):  # buildings enum
    BEACH = 'BCH'
    FACTORY = 'FAC'
    HOUSE = 'HSE'
    SHOP = 'SHP'
    HIGHWAY = 'HWY'
    MONUMENT = "MON"
    PARK = "PRK"
