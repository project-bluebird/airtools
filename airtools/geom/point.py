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

    def forward(self, distance, bearing):
        """
        Relative to the current position,
        create a position a given distance away following a given bearing.
        """

        proj_longitude, proj_latitude, _ = self.geodesic.fwd(
            self.longitude, self.latitude, bearing, distance)

        return Point(proj_longitude, proj_latitude)

    def bearing_to(self, other):
        """
        Calculate the bearing to another fix.
        """

        fwd_azimuth, _back_azimuth, _distance = self.geodesic.inv(
            self.long, self.lat, other.long, other.lat)

        return fwd_azimuth

    def distance(self, other):
        """
        Calculate the geodesic distance to another fix.
        """

        _fwd_azimuth, _back_azimuth, distance = self.geodesic.inv(
            self.long, self.lat, other.long, other.lat)

        return distance
