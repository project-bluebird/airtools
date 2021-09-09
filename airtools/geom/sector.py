from shapely.geometry import Polygon, Point


class Sector:
    """
    Area on the globe.
    """

    def __init__(self, boundary_coords, waypoints):
        """
        Construct a new instance.
        """

        self.boundary = Polygon(map(lambda pos: Point(pos.long, pos.lat), boundary_coords))
        self.waypoints = waypoints

    def contains(self, coord):
        """
        Calculate if a given coordinate position is contain within the sector boundary.
        """

        return self.boundary.contains(Point(coord.longitude, coord.latitude))