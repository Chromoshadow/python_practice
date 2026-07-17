import sys
from ft_filter import ft_filter


def main():
    args = sys.argv[1:]

    if len(args) != 2:
        raise AssertionError("incorrect number of arguments")

    try:
        number = int(args[1])
    except ValueError:
        raise AssertionError("argument is not an integer")

    splitted = args[0].split(" ")

    res = list(filter(lambda e: len(e) > number, splitted))
    ft_res = list(ft_filter(lambda e: len(e) > number, splitted))
    con_res = [e for e in splitted if len(e) > number]

    print(f"filter =             {res}")
    print(f"ft_filter =          {ft_res}")
    print(f"list comprehension = {con_res}")

    print(filter.__doc__)
    print(ft_filter.__doc__)

    return 0


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
