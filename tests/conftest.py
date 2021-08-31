import math
import pytest

import numpy as np

from geopy import distance

major_semiaxis, _, _ = distance.ELLIPSOIDS["WGS-84"]
_EARTH_RADIUS = major_semiaxis * 1000


def great_circle(from_lat, from_lon, to_lat, to_lon):
    """Calculate great circle distance using the Haversine formula"""
    dlat = from_lat - to_lat
    dlon = from_lon - to_lon

    a = (math.sin(np.deg2rad(dlat) / 2)) ** 2 + math.cos(np.deg2rad(from_lat)) * math.cos(
        np.deg2rad(to_lat)
    ) * (math.sin(np.deg2rad(dlon) / 2)) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    expected = _EARTH_RADIUS * c
    return expected


@pytest.fixture
def expected_great_circle():
    return great_circle


@pytest.fixture
def earth_radius():
    return _EARTH_RADIUS
