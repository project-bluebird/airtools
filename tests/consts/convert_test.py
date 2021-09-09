from pytest import approx

from airtools.consts.convert import METERS_IN_FEET, FEET_IN_METERS, METERS_IN_NAUTICAL_MILES, NAUTICAL_MILES_IN_METERS, METERS_PER_SECOND_IN_KNOTS, KNOTS_IN_METERS_PER_SECOND


def test_meters_in_feet():
    assert METERS_IN_FEET * 6 == approx(2, 1e-1)


def test_feet_in_meters():
    assert FEET_IN_METERS * 2 == approx(6, 1e-1)


def test_meters_in_nautical_miles():
    assert METERS_IN_NAUTICAL_MILES * 1 == approx(2000, 1e-1)


def test_nautical_miles_in_meters():
    assert NAUTICAL_MILES_IN_METERS * 2000 == approx(1, 1e-1)


def test_meters_per_second_in_knots():
    assert METERS_PER_SECOND_IN_KNOTS * 0.5 == approx(1, 1e-1)


def test_knots_in_meters_per_second():
    assert KNOTS_IN_METERS_PER_SECOND * 1 == approx(0.5, 1e-1)
