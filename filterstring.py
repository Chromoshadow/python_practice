import sys
from ft_filter import ft_filter


def main():
    args = sys.argv[1:]

    if len(args) != 2:
        raise AssertionError("incorrect number of arguments")
    
    try:
        number = int(args[1])
    except:
        raise AssertionError("argument is not an integer")

    res = list(filter(lambda x: len(x) > number, args[0].split(" ")))
    ft_res = list(ft_filter(lambda x: len(x) > number, args[0].split(" ")))
    print(f"res = {res}")
    print(f"ft_res = {ft_res}")
    return 0

if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")