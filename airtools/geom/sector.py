from shapely.geometry import Polygon, Point


class Sector:
    """
    Area on the globe.
    """

    def __init__(self, fixes, boundary, waypoints):
        """
        Construct a new instance.
        """

        self.boundary = Polygon(
            map(lambda id: Point(fixes[id].long, fixes[id].lat), boundary))
        self.waypoints = waypoints

    def contains(self, coord):
        """
        Calculate if a given coordinate position is contain within the sector boundary.
        """

        return self.boundary.contains(Point(coord.long, coord.lat))
