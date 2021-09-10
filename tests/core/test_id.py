from pytest import approx

from airtools.geom.coord import Coord
from airtools.core.id import ID


TEST_OBJ = {
    "ALFA": Coord(8.5, 0),
    "BRAV": Coord(7.5, 0),
    "CHAR": Coord(5, 0),
    "DELT": Coord(2.5, 0),
    "ECHO": Coord(1.5, 0)
}


def test_hint():
    """
    Test hinting usage.
    """
    id: ID = "ALFA"

    assert TEST_OBJ[id].lat == approx(8.5)
    assert TEST_OBJ[id].long == approx(0)
