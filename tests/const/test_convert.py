from pytest import approx
import math

from airtools.consts.convert import *


def test_lengths():
    """
    Test hinting usage.
    """
    assert math.pi * M_TO_FT == approx(10.3070625, 1e-3)
    assert math.pi * FT_TO_M == approx(0.95755743972, 1e-3)
    assert math.pi * NM_TO_M == approx(5818.2295878, 1e-3)
    assert math.pi * M_TO_NM == approx(0.001696324325054, 1e-3)
    assert math.pi * DEG_TO_NM == approx(188.495559, 1e-3)
    assert math.pi * NM_TO_DEG == approx(0.0523598776, 1e-3)


def test_speeds():
    """
    Test hinting usage.
    """
    assert math.pi * MPS_TO_KN == approx(6.10676757547, 1e-3)
    assert math.pi * KN_TO_MPS == approx(1.616174884104, 1e-3)
    assert math.pi * MPS_TO_KPH == approx(11.30973354, 1e-3)
    assert math.pi * KPH_TO_MPS == approx(0.8726646250001, 1e-3)
