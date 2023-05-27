def catAndMouse(x, y, z):
    """
    Determines which cat will reach the mouse first or if the mouse escapes.

    Args:
        x (int): Position of Cat A.
        y (int): Position of Cat B.
        z (int): Position of Mouse C.

    Returns:
        str: Either 'Cat A', 'Cat B', or 'Mouse C' based on the outcome.

    Raises:
        ValueError: If any of the positions (x, y, z) are not within the range [1, 100].

    """
    if not (1 <= x <= 100) or not (1 <= y <= 100) or not (1 <= z <= 100):
        raise ValueError("Positions should be between 1 and 100 (inclusive)")

    distance_a = abs(z - x)
    distance_b = abs(z - y)

    if distance_a < distance_b:
        return "Cat A"
    elif distance_b < distance_a:
        return "Cat B"
    else:
        return "Mouse C"
