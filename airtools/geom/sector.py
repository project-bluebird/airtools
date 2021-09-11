from shapely.geometry import Polygon, Point

from airtools.consts.convert import DEG_TO_NM
from airtools.core.id import ID
from airtools.core.route import Route
from airtools.geom.coord import Coord


class Sector:
    """
    Area on the globe.
    """

    def __init__(self, boundary: list[ID], waypoints: list[ID], routes: dict[ID, Route]):
        """
        Construct a new instance.
        """
        from airtools.geom.world import World

        self.boundary = Polygon(
            map(lambda id: Point(World.fixes[id].long, World.fixes[id].lat), boundary))
        self.waypoints = waypoints
        self.routes = routes

        return

    def contains(self, coord: Coord) -> bool:
        """
        Calculate if a given coordinate position is contain within the sector boundary.
        """

        return self.boundary.contains(coord.as_point())

    def dist(self, coord: Coord) -> float:
        """
        Calculate the minimum seperation distance [NM] between the given coord and the sector boundary.
        """

        return self.boundary.distance(coord.as_point()) * DEG_TO_NM
