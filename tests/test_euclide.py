import pytest

from euclide import gcd


@pytest.mark.parametrize(
        "a, b, expected_gcd",
        [
            (1, 1, 1),
            (1, 5, 1),
            (5, 1, 1),
            (15, 21, 3),
            (21, 15, 3),
            (7, 13, 1),
            (354224848179261915075, 573147844013817084101, 1),
        ],
        # ids = ...
)
def test_gcd_ok(a: int, b: int, expected_gcd: int):
    # when
    actual_gcd = gcd(a, b)
    # then
    assert actual_gcd == expected_gcd


# TODO: cases a ou b negatifs ou nul