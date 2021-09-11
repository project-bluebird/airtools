from pytest import approx
import math

from airtools.geom.coord import Coord
from airtools.consts.convert import DEG_TO_NM


FIXES = {
    "O": Coord(0, 0),
    "N": Coord(1, 0),
    "E": Coord(0, 1),
    "S": Coord(-1, 0),
    "W": Coord(0, -1),
    "NE": Coord(1, 1),
    "SE": Coord(-1, 1),
    "SW": Coord(-1, -1),
    "NW": Coord(1, -1),
}


def test_init():

    assert FIXES["O"].lat == 0
    assert FIXES["O"].long == 0

    assert FIXES["N"].lat == 1
    assert FIXES["N"].long == 0
    assert FIXES["E"].lat == 0
    assert FIXES["E"].long == 1
    assert FIXES["S"].lat == -1
    assert FIXES["S"].long == 0
    assert FIXES["W"].lat == 0
    assert FIXES["W"].long == -1

    assert FIXES["NE"].lat == 1
    assert FIXES["NE"].long == 1
    assert FIXES["SE"].lat == -1
    assert FIXES["SE"].long == 1
    assert FIXES["SW"].lat == -1
    assert FIXES["SW"].long == -1
    assert FIXES["NW"].lat == 1
    assert FIXES["NW"].long == -1


def test_forward():

    origin = Coord(0, 0)
    north_east = origin.forward(math.sqrt(2) * DEG_TO_NM, 45)
    south_east = origin.forward(math.sqrt(2) * DEG_TO_NM, 45 + 90)
    south_west = origin.forward(math.sqrt(2) * DEG_TO_NM, 45 + 180)
    north_west = origin.forward(math.sqrt(2) * DEG_TO_NM, 45 + 270)

    assert north_east.lat == approx(1, 1e-2)
    assert north_east.long == approx(1, 1e-2)
    assert south_east.lat == approx(-1, 1e-2)
    assert south_east.long == approx(1, 1e-2)
    assert south_west.lat == approx(-1, 1e-2)
    assert south_west.long == approx(-1, 1e-2)
    assert north_west.lat == approx(1, 1e-2)
    assert north_west.long == approx(-1, 1e-2)


def test_bearing_to():

    assert FIXES["O"].bearing_to(FIXES["N"]) == approx(0, 1e-2)
    assert FIXES["O"].bearing_to(FIXES["NE"]) == approx(45, 1e-2)
    assert FIXES["O"].bearing_to(FIXES["E"]) == approx(90, 1e-2)
    assert FIXES["O"].bearing_to(FIXES["SE"]) == approx(135, 1e-2)
    assert FIXES["O"].bearing_to(FIXES["S"]) == approx(180, 1e-2)
    assert FIXES["O"].bearing_to(FIXES["SW"]) == approx(225, 1e-2)
    assert FIXES["O"].bearing_to(FIXES["W"]) == approx(270, 1e-2)
    assert FIXES["O"].bearing_to(FIXES["NW"]) == approx(315, 1e-2)

    assert FIXES["N"].bearing_to(FIXES["O"]) == approx(180, 1e-2)
    assert FIXES["NE"].bearing_to(FIXES["O"]) == approx(225, 1e-2)
    assert FIXES["E"].bearing_to(FIXES["O"]) == approx(270, 1e-2)
    assert FIXES["SE"].bearing_to(FIXES["O"]) == approx(315, 1e-2)
    assert FIXES["S"].bearing_to(FIXES["O"]) == approx(0, 1e-2)
    assert FIXES["SW"].bearing_to(FIXES["O"]) == approx(45, 1e-2)
    assert FIXES["W"].bearing_to(FIXES["O"]) == approx(90, 1e-2)
    assert FIXES["NW"].bearing_to(FIXES["O"]) == approx(135, 1e-2)


def test_dist():

    assert FIXES["O"].dist(FIXES["N"]) == approx(60, 1e-2)
    assert FIXES["O"].dist(FIXES["NE"]) == approx(60 * math.sqrt(2), 1e-2)
    assert FIXES["O"].dist(FIXES["E"]) == approx(60, 1e-2)
    assert FIXES["O"].dist(FIXES["SE"]) == approx(60 * math.sqrt(2), 1e-2)
    assert FIXES["O"].dist(FIXES["S"]) == approx(60, 1e-2)
    assert FIXES["O"].dist(FIXES["SW"]) == approx(60 * math.sqrt(2), 1e-2)
    assert FIXES["O"].dist(FIXES["W"]) == approx(60, 1e-2)
    assert FIXES["O"].dist(FIXES["NW"]) == approx(60 * math.sqrt(2), 1e-2)

    assert FIXES["N"].dist(FIXES["O"]) == approx(60, 1e-2)
    assert FIXES["NE"].dist(FIXES["O"]) == approx(60 * math.sqrt(2), 1e-2)
    assert FIXES["E"].dist(FIXES["O"]) == approx(60, 1e-2)
    assert FIXES["SE"].dist(FIXES["O"]) == approx(60 * math.sqrt(2), 1e-2)
    assert FIXES["S"].dist(FIXES["O"]) == approx(60, 1e-2)
    assert FIXES["SW"].dist(FIXES["O"]) == approx(60 * math.sqrt(2), 1e-2)
    assert FIXES["W"].dist(FIXES["O"]) == approx(60, 1e-2)
    assert FIXES["NW"].dist(FIXES["O"]) == approx(60 * math.sqrt(2), 1e-2)


def test_as_point():

    p_north = FIXES["N"].as_point()
    assert p_north.x == 1
    assert p_north.y == 0

    p_north = FIXES["NE"].as_point()
    assert p_north.x == 1
    assert p_north.y == 1

    p_north = FIXES["E"].as_point()
    assert p_north.x == 0
    assert p_north.y == 1

    p_north = FIXES["SE"].as_point()
    assert p_north.x == -1
    assert p_north.y == 1

    p_north = FIXES["S"].as_point()
    assert p_north.x == -1
    assert p_north.y == 0

    p_north = FIXES["SW"].as_point()
    assert p_north.x == -1
    assert p_north.y == -1

    p_north = FIXES["W"].as_point()
    assert p_north.x == 0
    assert p_north.y == -1

    p_north = FIXES["NW"].as_point()
    assert p_north.x == 1
    assert p_north.y == -1


def test_str():

    assert str(FIXES["N"]) == "1N 0E"
    assert str(FIXES["NE"]) == "1N 1E"
    assert str(FIXES["E"]) == "0N 1E"
    assert str(FIXES["SE"]) == "1S 1E"
    assert str(FIXES["S"]) == "1S 0E"
    assert str(FIXES["SW"]) == "1S 1W"
    assert str(FIXES["W"]) == "0N 1W"
    assert str(FIXES["NW"]) == "1N 1W"
