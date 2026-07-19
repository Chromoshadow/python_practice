def ft_tqdm(lst: range) -> None:
    """Decorate an iterable object, returning an iterator which acts exactly
    like the original iterable, but prints a dynamically updating
    progress bar every time a value is requested."""
    total = len(lst)
    width = 50  

    for elem in lst:
        percent = (elem + 1) / total
        filled = int(width * percent)
        bar = "=" * filled + "-" * (width - filled)

        print(f"\r[{bar}] {percent:.0%}", end="", flush=True)

        yield elem
