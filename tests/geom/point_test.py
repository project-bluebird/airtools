from pytest import approx

from airtools.geom.point import Point


def test_init():
    exeter = Point(50.73497, -3.414952)

    assert exeter.lat == 50.73497
    assert exeter.long == -3.414952


def test_forward():
    exeter = Point(50.73497, -3.414952)
    london = exeter.forward(283e3, 71.71)

    assert london.lat == approx(51.4700, 1e-2)
    assert london.long == approx(0.4543, 1e-2)


def test_bearing_to():
    exeter = Point(50.73497, -3.414952)
    london = Point(51.4700, 0.4543)

    assert exeter.bearing_to(london) == approx(71.71, 1e-5)


def test_distance():
    exeter = Point(50.73497, -3.414952)
    london = Point(51.4700, 0.4543)

    assert exeter.distance(london) == approx(283e3, 1e-3)
