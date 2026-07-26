def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """
    Calculate BMI for each pair of height and weight.

    BMI = weight / (height ** 2)

    Args:
        height: List of heights.
        weight: List of weights.

    Returns:
        List of BMI values.

    Raises:
        TypeError: If inputs are not lists or contain non-numeric values.
        ValueError: If lists are different sizes or a height is not positive.
    """
    if not isinstance(height, list) or not isinstance(weight, list):
        raise TypeError("Both height and weight must be lists.")

    if len(height) != len(weight):
        raise ValueError("Height and weight lists must have the same length.")

    bmi = []
    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            raise TypeError("Height and weight values must be int or float.")
        if h <= 0:
            raise ValueError("Height values must be greater than zero.")
        bmi.append(w / (h ** 2))
    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Compare BMI values to a limit.

    Args:
        bmi: List of BMI values.
        limit: BMI threshold.

    Returns:
        List of booleans indicating whether each BMI exceeds the limit.

    Raises:
        TypeError: If inputs are invalid.
    """
    if not isinstance(bmi, list):
        raise TypeError("BMI must be a list.")

    if not isinstance(limit, int):
        raise TypeError("Limit must be an integer.")

    result = []
    for v in bmi:
        if not isinstance(v, (int, float)):
            raise TypeError("BMI list must contain only int or float values.")

        result.append(v > limit)
    return result
