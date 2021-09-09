from airtools.geom.point import Point


def test_init():
    a = Point(-1.23, +4.56)

    assert a.lat == -1.23
    assert a.long == 4.56
