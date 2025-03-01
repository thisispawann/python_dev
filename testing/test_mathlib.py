import mathlib

def test_calc_total():
    total = mathlib.calc_total(23, 3)
    assert total == 26


def test_calc_substract():
    result = mathlib.cal_substract(32, 9)
    assert result == 23