from airtools.core.id import ID
from airtools.core.route import Route


def test_hint():
    """
    Test hinting usage.
    """
    bravo: ID = "BRAV"
    charlie: ID = "CHAR"
    delta: ID = "DELT"

    route: Route = ["ALFA", bravo, charlie, delta, "ECHO"]

    assert route[0] == "ALFA"
    assert route[1] == "BRAV"
    assert route[2] == "CHAR"
    assert route[3] == "DELT"
    assert route[4] == "ECHO"
