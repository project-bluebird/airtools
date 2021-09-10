import json

from airtools.geom.coord import Coord
from airtools.io.json import JsonDecoder, JsonEncoder


TEST_OBJ = {
    "ALFA": Coord(8.5, 0),
    "BRAV": Coord(7.5, 0),
    "CHAR": Coord(5, 0),
    "DELT": Coord(2.5, 0),
    "ECHO": Coord(1.5, 0)
}
TEST_STR = """{"ALFA": {"lat": 8.5, "long": 0}, "BRAV": {"lat": 7.5, "long": 0}, "CHAR": {"lat": 5, "long": 0}, "DELT": {"lat": 2.5, "long": 0}, "ECHO": {"lat": 1.5, "long": 0}}"""


def test_encode():
    """
    Test deserialisation from instantiation.
    """
    print(len(TEST_STR))
    print(len(json.dumps(TEST_OBJ, cls=JsonEncoder)))
    print(json.dumps(TEST_OBJ, cls=JsonEncoder))
    assert json.dumps(TEST_OBJ, cls=JsonEncoder) == TEST_STR


def test_decode():
    """
    Test serialisation from json.
    """
    fixes = json.loads(TEST_STR, cls=JsonDecoder)

    assert len(fixes) == len(TEST_OBJ)
    for id in TEST_OBJ.keys():
        assert fixes[id].lat == TEST_OBJ[id].lat
        assert fixes[id].long == TEST_OBJ[id].long
