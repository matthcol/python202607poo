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


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
      "a, b",
      [
          (0, 0),
          (0, 5),
          (5, 0),
          (-1, 5),
          (5, -1),
          (-3, -7),
      ],
      # ids = ...

)
def test_gcd_ko(a: int, b: int):
    with pytest.raises(ValueError) as ex:
        gcd(a, b)
    # TODO: check error message