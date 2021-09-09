from re import T
from pytest import approx

from airtools.geom.sector import Sector
from airtools.geom.coord import Coord


FIXES = {
    "north_west_bound": Coord(1.0, -0.5),
    "north_east_bound": Coord(1.0, 0.5),
    "south_east_bound": Coord(-1.0, 0.5),
    "south_west_bound": Coord(-1.0, -0.5),
    "spirit": Coord(1.2, 0.0),
    "air": Coord(1.0, 0.0),
    "water": Coord(0.0, 0.0),
    "earth": Coord(-1.0, 0.0),
    "fire": Coord(-1.2, 0.0),
}

BOUNDARY = [
    "north_west_bound",
    "north_east_bound",
    "south_east_bound",
    "south_west_bound"
]
WAYPOINTS = [
    "north_west_bound",
    "north_east_bound",
    "south_west_bound",
    "south_east_bound"
]


def test_init():
    sector = Sector(FIXES, BOUNDARY, WAYPOINTS)


def test_contains():
    sector = Sector(FIXES, BOUNDARY, WAYPOINTS)

    assert sector.contains(FIXES["spirit"]) == False
    assert sector.contains(FIXES["air"]) == False
    assert sector.contains(FIXES["water"]) == True
    assert sector.contains(FIXES["earth"]) == False
    assert sector.contains(FIXES["fire"]) == False
