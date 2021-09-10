from shapely.geometry import Polygon, Point

from airtools.geom.airspace import Airspace
from airtools.geom.coord import Coord


DEG_TO_NM: float = 60  # There are 60 nautical miles per degree.


class Sector:
    """
    Area on the globe.
    """

    def __init__(self, boundary: list[str], waypoints: list[str]):
        """
        Construct a new instance.
        """

        self.boundary = Polygon(
            map(lambda id: Point(Airspace.fixes[id].long, Airspace.fixes[id].lat), boundary))
        self.waypoints = waypoints

    def contains(self, coord: Coord) -> bool:
        """
        Calculate if a given coordinate position is contain within the sector boundary.
        """

        return self.boundary.contains(coord.as_point())

    def dist(self, coord: Coord) -> float:
        """
        Calculate the minimum seperation distance between the given coord and the sector boundary.
        """

        return self.boundary.distance(coord.as_point()) * DEG_TO_NM
