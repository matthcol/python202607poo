def gcd(a: int, b: int) -> int:
    """Compute greatest common divider of 2 strictly positive integers

    Parameters
    ----------
    a: first integer
    b: second integer

    Returns
    -------
    greatest common divider

    Raises
    ------
    ValueError if a or b is negative or zero
    """
    if a <= 0 or b <= 0:
        raise ValueError("arguments must be strictly positive")
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a