from pyproj import Geod

from airtools.consts.convert import METERS_IN_NAUTICAL_MILES, NAUTICAL_MILES_IN_METERS


class Coord:
    """
    (Latitude, Longitude) position on the globe.
    """

    geodesic = Geod(ellps="WGS84")

    def __init__(self, lat, long):
        """
        Construct a new instance.
        """

        self.lat = lat      # [deg]
        self.long = long    # [deg]

    def forward(self, dist, heading):
        """
        Determine the coordinate position a given distance away [NM]
        from the current position, following a given heading [deg].
        """

        proj_long, proj_lat, _ = self.geodesic.fwd(
            self.long, self.lat, heading, METERS_IN_NAUTICAL_MILES * dist)

        return Coord(proj_lat, proj_long)

    def bearing_to(self, other):
        """
        Calculate the bearing [deg] to another coordinate position.
        """

        fwd_azimuth, _back_azimuth, _distance = self.geodesic.inv(
            self.long, self.lat, other.long, other.lat)

        return fwd_azimuth

    def dist(self, other):
        """
        Calculate the geodesic distance [NM] to another coordinate position.
        """

        _fwd_azimuth, _back_azimuth, dist = self.geodesic.inv(
            self.long, self.lat, other.long, other.lat)

        return NAUTICAL_MILES_IN_METERS * dist 
