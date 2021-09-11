from pytest import approx

from airtools.geom.world import World


def test_load():
    World.load_fixes("res/scenarios/test/boundary.json")
    World.load_fixes("res/scenarios/test/waypoints.json")
    World.load_sectors("res/scenarios/test/sectors.json")

    assert World.fixes["INDI"].lat == 0
    assert World.fixes["INDI"].long == 0

    assert World.fixes["B000"].lat == approx(-1.507397952721816)
    assert World.fixes["B000"].long == approx(0.08321259947807313)
