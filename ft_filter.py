def ft_filter(func, elements):
    """Return an iterator yielding those items of iterable for which function(item) is true. 
    If function is None, return the items that are true."""
    if func is None:
        return (e for e in elements if e)

    return [e for e in elements if func(e)]
