from pyproj import Geod


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
        Relative to the current coordinate position,
        create a position a given distance away following a given heading.
        """

        proj_long, proj_lat, _ = self.geodesic.fwd(
            self.long, self.lat, heading, dist)

        return Coord(proj_lat, proj_long)

    def bearing_to(self, other):
        """
        Calculate the bearing to another coordinate position [deg].
        """

        fwd_azimuth, _back_azimuth, _distance = self.geodesic.inv(
            self.long, self.lat, other.long, other.lat)

        return fwd_azimuth

    def dist(self, other):
        """
        Calculate the geodesic distance to another coordinate position [m].
        """

        _fwd_azimuth, _back_azimuth, dist = self.geodesic.inv(
            self.long, self.lat, other.long, other.lat)

        return dist
