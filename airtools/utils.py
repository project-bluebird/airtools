def _validate_latitude(lat):
    """Assert latitude is in the range ``[-90, 90]``."""
    assert abs(lat) <= 90, "Invalid value {} for latitude".format(lat)


def _validate_longitude(lon):
    """Assert longitude is in the range ``[-180, 180)``."""
    assert -180 <= lon < 180, "Invalid value {} for longitude".format(lon)


def _validate_is_positive(val, param_name):
    """Assert val is non-negative."""
    assert val >= 0, "Invalid value {} for {}".format(val, param_name)
