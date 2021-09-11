from airtools.geom.sector import Sector

from airtools.geom.world import World


def test_init():

    World.load_fixes("res/scenarios/test/boundary.json")
    World.load_fixes("res/scenarios/test/waypoints.json")

    sector = Sector(
        ["B000", "B001", "B019", "B020"],
        ["ALFA", "BRAV", "CHAR", "ECHO", "FOXT"],
        {
            "northbound": ["ALFA", "BRAV", "CHAR", "ECHO", "FOXT"],
            "southbound": ["FOXT", "ECHO", "CHAR", "BRAV", "ALFA"],
        }
    )
