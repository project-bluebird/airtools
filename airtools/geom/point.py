from pyproj import Geod


class Point:
    """
    Position on the globe.
    """

    geodesic = Geod(ellps="WGS84")

    def __init__(self, lat, long):
        """
        Construct a new instance.
        """

        self.lat = lat
        self.long = long

    def forward(self, distance, heading):
        """
        Relative to the current position,
        create a position a given distance away following a given heading.
        """

        proj_long, proj_lat, _ = self.geodesic.fwd(
            self.long, self.lat, heading, distance)

        return Point(proj_lat, proj_long)

    def bearing_to(self, other):
        """
        Calculate the bearing to another point.
        """

        fwd_azimuth, _back_azimuth, _distance = self.geodesic.inv(
            self.long, self.lat, other.long, other.lat)

        return fwd_azimuth

    def distance(self, other):
        """
        Calculate the geodesic distance to another point.
        """

        _fwd_azimuth, _back_azimuth, distance = self.geodesic.inv(
            self.long, self.lat, other.long, other.lat)

        return distance
