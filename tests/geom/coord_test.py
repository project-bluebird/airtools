from pytest import approx

from airtools.geom.coord import Coord


def test_init():
    exeter = Coord(50.73497, -3.414952)

    assert exeter.lat == 50.73497
    assert exeter.long == -3.414952


def test_forward():
    exeter = Coord(50.73497, -3.414952)
    london = exeter.forward(152.83, 71.71)

    assert london.lat == approx(51.4700, 1e-3)
    assert london.long == approx(0.4543, 1e-3)


def test_bearing_to():
    exeter = Coord(50.73497, -3.414952)
    london = Coord(51.4700, 0.4543)

    assert exeter.bearing_to(london) == approx(71.71, 1e-3)


def test_distance():
    exeter = Coord(50.73497, -3.414952)
    london = Coord(51.4700, 0.4543)

    assert exeter.dist(london) == approx(152.83, 1e-3)
