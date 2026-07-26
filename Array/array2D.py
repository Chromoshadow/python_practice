def slice_me(family: list, start: int, end: int) -> list:

    if not isinstance(family, list):
        raise TypeError("Input must be a list.")

    if not all(isinstance(row, list) for row in family):
        raise TypeError("Input must be a 2D list.")

    if len(family) > 0:
        row_length = len(family[0])
        if not all(len(row) == row_length for row in family):
            raise ValueError("All rows must have the same size.")

    print(f"My shape is : ({len(family)}, {len(family[0]) if family else 0})")
    s = slice(start, end)
    sliced = family[s]

    a = len(sliced)
    b = len(sliced[0]) if sliced else 0
    print(f"My new shape is : ({a}, {b})")
    return sliced
