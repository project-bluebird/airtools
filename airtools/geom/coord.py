from __future__ import annotations

from pyproj import Geod
from shapely.geometry import Point

from airtools.consts.convert import M_TO_NM, NM_TO_M


class Coord:
    """
    (Latitude, Longitude) position on the globe.
    """

    geodesic: Geod = Geod(ellps="WGS84")

    def __init__(self, lat: float, long: float):
        """
            Construct a new instance.
            """

        self.lat = lat       # [deg]
        self.long = long     # [deg]

    def forward(self, dist: float, heading: float) -> Coord:
        """
        Determine the coordinate position a given distance away [NM]
        from the current position, following a given heading [deg].
        """

        proj_long, proj_lat, _ = self.geodesic.fwd(
            self.long, self.lat, heading, dist * NM_TO_M)

        return Coord(proj_lat, proj_long)

    def bearing_to(self, other: Coord) -> float:
        """
        Calculate the bearing [deg] to another coordinate position.
        """

        _fwd_azimuth, back_azimuth, _distance = self.geodesic.inv(
            other.long, other.lat, self.long, self.lat)

        return back_azimuth % 360

    def dist(self, other: Coord) -> float:
        """
        Calculate the geodesic distance [NM] to another coordinate position.
        """

        _fwd_azimuth, _back_azimuth, dist = self.geodesic.inv(
            self.long, self.lat, other.long, other.lat)

        return dist * M_TO_NM

    def as_point(self) -> Point:
        """
        Create a corresponing cartesian Point representation.
        """

        return Point(self.lat, self.long)

    def __str__(self) -> str:
        """
        Create a string representation of the coordinate.
        """
        v = 'N'
        if self.lat < 0:
            v = 'S'

        h = 'E'
        if self.long < 0:
            h = 'W'

        return f"{abs(self.lat)}{v} {abs(self.long)}{h}"

    def as_json(self) -> dict[str, Coord]:
        """
        Create a JSON representation of the coordinate.
        """

        return self.__dict__
