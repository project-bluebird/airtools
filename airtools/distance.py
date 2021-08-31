import numpy as np
from geopy import distance
from scipy.spatial.distance import euclidean

from . import utils

# Default for major (equatorial) radius and flattening are 'WGS-84' values.
major_semiaxis, minor_semiaxis, _FLATTENING = distance.ELLIPSOIDS["WGS-84"]
_EARTH_RADIUS = major_semiaxis * 1000  # convert to metres


def geodesic_distance(from_lat, from_lon, to_lat, to_lon, **kwargs):
    """
    Get geodesic distance between two (lat, lon) points in metres.
    Parameters
    ----------
    from_lat : double
        A double in the range ``[-90, 90]``. The `from` point's latitude.
    from_lon : double
        A double in the range ``[-180, 180)``. The `from` point's longitude.
    to_lat : double
        A double in the range ``[-90, 90]``. The `to` point's latitude.
    to_lon : double
        A double in the range ``[-180, 180)``. The `to` point's longitude.
    **kwargs:
        major_semiaxis : double, optional
            The major (equatorial) radius of the ellipsoid. The default value is for WGS84.
        flattening : double, optional
            Ellipsoid flattening. The default value is for WGS84.
    Returns
    -------
    geodesic_distance : double
        The geodesic distance between two points.
    Examples
    --------
    >>> >>> pydodo.geodesic_distance(from_lat = 51.5 , from_lon = 0.12, to_lat = 50.6, to_lon = -1.9)
    """
    major_semiaxis = (
        _EARTH_RADIUS if "major_semiaxis" not in kwargs else kwargs["major_semiaxis"]
    )
    flattening = _FLATTENING if "flattening" not in kwargs else kwargs["flattening"]

    utils._validate_latitude(from_lat)
    utils._validate_longitude(from_lon)
    utils._validate_latitude(to_lat)
    utils._validate_longitude(to_lon)
    utils._validate_is_positive(major_semiaxis, "major_semiaxis")
    utils._validate_is_positive(flattening, "flattening")

    # For GeoPy need to provide (major_semiaxis, minor_semiaxis, flattening) but
    # only major_semiaxis & flattening vals are used --> ignore minor_semiaxis
    return distance.geodesic(
        (from_lat, from_lon),
        (to_lat, to_lon),
        ellipsoid=(major_semiaxis / 1000, minor_semiaxis, flattening),  # convert to km
    ).meters


def great_circle_distance(from_lat, from_lon, to_lat, to_lon, **kwargs):
    """
    Get great-circle distance between two (lat, lon) points in metres.
    Parameters
    ----------
    from_lat : double
        A double in the range ``[-90, 90]``. The `from` point's latitude.
    from_lon : double
        A double in the range ``[-180, 180)``. The `from` point's longitude.
    to_lat : double
        A double in the range ``[-90, 90]``. The `to` point's latitude.
    to_lon : double
        A double in the range ``[-180, 180)``. The `to` point's longitude.
    **kwargs
        radius : double, optional
            The radius of the earth in metres. The default value is for WGS84.
    Returns
    -------
    great_circle_distance : double
        The great-circle distance between two points.
    Examples
    --------
    >>> pydodo.great_circle_distance(from_lat = 51.5 , from_lon = 0.12, to_lat = 50.6, to_lon = -1.9)
    """
    radius = _EARTH_RADIUS if "radius" not in kwargs else kwargs["radius"]

    utils._validate_latitude(from_lat)
    utils._validate_longitude(from_lon)
    utils._validate_latitude(to_lat)
    utils._validate_longitude(to_lon)
    utils._validate_is_positive(radius, "radius")

    return distance.great_circle(
        (from_lat, from_lon), (to_lat, to_lon), radius=radius / 1000  # convert to km
    ).meters


def vertical_distance(from_alt, to_alt, **kwargs):
    """
    Get vertical distance in metres between two altitudes (provided in metres).
    Parameters
    ----------
    from_alt : double
        A non-negatige double. The `from` point's altitude in metres.
    to_alt : double
        A non-negatige double. The `to` point's altitude in metres.
    Returns
    -------
    vertical_distance : double
        The verticle distance between two points.
    Examples
    --------
    >>> pydodo.vertical_distance(from_alt = 200, to_alt = 350)
    """
    utils._validate_is_positive(from_alt, "altitude")
    utils._validate_is_positive(to_alt, "altitude")

    return abs(from_alt - to_alt)


def _lla_to_ECEF(lat, lon, alt=0, radius=_EARTH_RADIUS, f=_FLATTENING):
    """
    Calculates ECEF coordinates of a point from lat, lon and alt.
    Parameters
    ----------
    lat : double
    lon : double
    alt : int
        Altitude in meters
    radius : double, optional
        Earth radius in metres (WGS84).
    f : double, optional
        Ellipsoidal flattening (WGS84).
    Returns
    -------
    (double, double, double)
        The (x, y, z) ECEF coordinates.
    Notes
    -----
    https://en.wikipedia.org/wiki/ECEF
    Examples
    --------
    >>> pydodo.distance_measures.lla_to_ECEF(lat = 51.5 , lon = 0.12, alt = 200)
    """

    lat_r = np.deg2rad(lat)
    lon_r = np.deg2rad(lon)

    e2 = 1 - (1 - f) * (1 - f)
    N = radius / np.sqrt(1 - e2 * np.power(np.sin(lat_r), 2))

    x = (N + alt) * np.cos(lat_r) * np.cos(lon_r)
    y = (N + alt) * np.cos(lat_r) * np.sin(lon_r)
    z = ((1 - e2) * N + alt) * np.sin(lat_r)

    return (x, y, z)


def euclidean_distance(from_lat, from_lon, from_alt, to_lat, to_lon, to_alt, **kwargs):
    """
    Get euclidean distance between two (lat, lon, alt) points in metres. The
    points are converted to ECEF coordinates to calculate distance.
    Parameters
    ----------
    from_lat : double
        A double in the range ``[-90, 90]``. The `from` point's latitude.
    from_lon : double
        A double in the range ``[-180, 180)``. The `from` point's longitude.
    from_alt : double
        A non-negatige double. The from point's altitude in metres.
    to_lat : double
         A double in the range ``[-90, 90]``. The `to` point's latitude.
    to_lon : double
        A double in the range ``[-180, 180)``. The `to` point's longitude.
    to_alt : double
        A non-negatige double. The `to` point's altitude in metres.
    **kwargs:
        major_semiaxis : double, optional
            The major (equatorial) radius of the ellipsoid. The default value is for WGS84.
        flattening : double, optional
            Ellipsoid flattening. The default value is for WGS84.
    Returns
    -------
    euclidean_distance : double
        The euclidean distance between two points.
    Notes
    -----
    https://en.wikipedia.org/wiki/ECEF
    Examples
    --------
    >>> pydodo.euclidean_distance(from_lat = 51.5 , from_lon = 0.12, from_alt = 200, to_lat = 50.6, to_lon = -1.9, to_alt = 350)
    """
    major_semiaxis = (
        _EARTH_RADIUS if "major_semiaxis" not in kwargs else kwargs["major_semiaxis"]
    )
    flattening = _FLATTENING if "flattening" not in kwargs else kwargs["flattening"]

    utils._validate_latitude(from_lat)
    utils._validate_longitude(from_lon)
    utils._validate_is_positive(from_alt, "altitude")
    utils._validate_latitude(to_lat)
    utils._validate_longitude(to_lon)
    utils._validate_is_positive(to_alt, "altitude")
    utils._validate_is_positive(major_semiaxis, " major_semiaxis")

    from_ECEF = _lla_to_ECEF(from_lat, from_lon, from_alt, major_semiaxis, flattening)
    to_ECEF = _lla_to_ECEF(to_lat, to_lon, to_alt, major_semiaxis, flattening)

    return euclidean(from_ECEF, to_ECEF)
