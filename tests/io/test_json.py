import json

from airtools.geom.coord import Coord
from airtools.geom.sector import Sector
from airtools.io.json import JsonDecoder, JsonEncoder


FIXES_OBJ: dict[str, Coord] = {
    "ALFA": Coord(8.5, 0),
    "BRAV": Coord(7.5, 0),
    "CHAR": Coord(5, 0),
    "DELT": Coord(2.5, 0),
    "ECHO": Coord(1.5, 0),
    "B000": Coord(7.5, -0.5),
    "B001": Coord(7.5, 0.5),
    "B002": Coord(2.5, 0.5),
    "B003": Coord(2.5, -0.5),
}
FIXES_STR: str = """{"ALFA": {"lat": 8.5, "long": 0}, "BRAV": {"lat": 7.5, "long": 0}, "CHAR": {"lat": 5, "long": 0}, "DELT": {"lat": 2.5, "long": 0}, "ECHO": {"lat": 1.5, "long": 0}, "B000": {"lat": 7.5, "long": -0.5}, "B001": {"lat": 7.5, "long": 0.5}, "B002": {"lat": 2.5, "long": 0.5}, "B003": {"lat": 2.5, "long": -0.5}}"""


def test_encode():

    assert json.dumps(FIXES_OBJ, cls=JsonEncoder) == FIXES_STR


def test_decode():

    fixes = json.loads(FIXES_STR, cls=JsonDecoder)
    assert len(fixes) == len(FIXES_OBJ)
    for id in FIXES_OBJ.keys():
        assert fixes[id].lat == FIXES_OBJ[id].lat
        assert fixes[id].long == FIXES_OBJ[id].long
